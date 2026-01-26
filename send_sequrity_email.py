import os
import smtplib
import logging
from dataclasses import dataclass
from datetime import datetime
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

from config import load_email_config

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class QuarterState:
    year: int
    quarter: int


def create_message(sender: str, recipient: str):
    """Creates the MIME message with embedded CID logo."""
    msg = MIMEMultipart("related")
    msg["Subject"] = "Информационная безопасность - TEZ TOUR"
    msg["From"] = sender
    msg["To"] = recipient

    # HTML content
    template_path = os.path.join(os.path.dirname(__file__), "templates", "newsletter.html")
    with open(template_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    msg_html = MIMEText(html_content, "html")
    msg.attach(msg_html)

    # Attach Logo using CID
    logo_path = os.path.join(os.path.dirname(__file__), "logo_tez.jpeg")
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            logo_data = f.read()

        image = MIMEImage(logo_data)
        image.add_header("Content-ID", "<logo_tez>")
        image.add_header("Content-Disposition", "inline", filename="logo_tez.jpeg")
        msg.attach(image)
    else:
        logger.warning(f"Logo file not found at {logo_path}")

    return msg

def _resolve_recipient(config):
    if config.test_email:
        return config.test_email, "test"
    return config.email_recipient, "primary"


def _validate_config(config) -> bool:
    missing = []
    if not config.smtp_server:
        missing.append("SMTP_SERVER")
    if not config.smtp_port:
        missing.append("SMTP_PORT")
    if not config.smtp_user:
        missing.append("SMTP_USER")
    if not config.smtp_password:
        missing.append("SMTP_PASSWORD")
    if not config.email_recipient and not config.test_email:
        missing.append("EMAIL_RECIPIENT")
    if missing:
        logger.error("Отсутствуют обязательные переменные окружения: %s", ", ".join(missing))
        return False
    return True


def send_email(config):
    """Task to send the email via SMTP."""
    recipient, recipient_mode = _resolve_recipient(config)
    if not recipient:
        logger.error("Адрес получателя не задан. Проверьте EMAIL_RECIPIENT или TEST_EMAIL.")
        return

    logger.info(
        "Attempting to send email to %s (mode=%s)...",
        recipient,
        recipient_mode,
    )

    try:
        msg = create_message(config.email_sender, recipient)

        # Connect to SMTP server
        # Note: Using standard SMTP (port 25). Port 587 would typically use starttls()
        with smtplib.SMTP(config.smtp_server, config.smtp_port) as server:
            # server.starttls() # Uncomment if migration to port 587 happens
            server.login(config.smtp_user, config.smtp_password)
            server.send_message(msg)

        logger.info("Successfully sent email to %s at %s", recipient, datetime.now())
    except smtplib.SMTPException as exc:
        logger.error("SMTP ошибка при отправке письма: %s", str(exc))
    except Exception as exc:
        logger.error("Ошибка при отправке письма: %s", str(exc))


def _current_quarter_state(now: datetime) -> QuarterState:
    quarter = (now.month - 1) // 3 + 1
    return QuarterState(year=now.year, quarter=quarter)


def _load_last_quarter_state(state_path: str) -> QuarterState | None:
    if not os.path.exists(state_path):
        return None
    try:
        with open(state_path, "r", encoding="utf-8") as handle:
            raw = handle.read().strip()
        if not raw:
            return None
        year_str, quarter_str = raw.split("-")
        return QuarterState(year=int(year_str), quarter=int(quarter_str))
    except Exception as exc:
        logger.warning("Не удалось прочитать состояние квартала: %s", str(exc))
        return None


def _store_last_quarter_state(state_path: str, state: QuarterState) -> None:
    try:
        with open(state_path, "w", encoding="utf-8") as handle:
            handle.write(f"{state.year}-{state.quarter}")
    except Exception as exc:
        logger.warning("Не удалось сохранить состояние квартала: %s", str(exc))


def should_send_quarterly(state_path: str, now: datetime) -> bool:
    current = _current_quarter_state(now)
    last_sent = _load_last_quarter_state(state_path)
    if last_sent == current:
        logger.info("Отправка за квартал %s/%s уже выполнялась", current.year, current.quarter)
        return False
    return True


def run_quarterly_cycle(config, state_path: str) -> None:
    now = datetime.now()
    if not should_send_quarterly(state_path, now):
        return

    send_email(config)
    _store_last_quarter_state(state_path, _current_quarter_state(now))

def main():
    config = load_email_config()

    if not config.service_start:
        logger.info("Service is disabled (SERVICE_START=False). Exiting.")
        return

    if not _validate_config(config):
        logger.warning("Сервис запущен без обязательной конфигурации. Планировщик не стартует.")
        return

    logger.info("Initializing Email Notification Service...")
    logger.info("SMTP Server: %s:%s", config.smtp_server, config.smtp_port)
    logger.info("Interval: %s", config.service_interval)

    state_path = os.path.join(os.path.dirname(__file__), "quarter_state.txt")

    scheduler = BlockingScheduler()
    trigger_args = {
        "minutes": 60,
    }
    if config.service_interval:
        from config import Config

        trigger_args = Config.get_interval_params()

    interval_trigger = IntervalTrigger(**trigger_args)
    scheduler.add_job(
        run_quarterly_cycle,
        trigger=interval_trigger,
        args=[config, state_path],
        next_run_time=datetime.now(),
    )

    try:
        logger.info("Scheduler started. Press Ctrl+C to stop.")
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logger.info("Service stopped.")

if __name__ == "__main__":
    main()
