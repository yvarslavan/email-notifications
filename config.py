import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


def _parse_bool(value: str | None, default: bool) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


@dataclass(frozen=True)
class EmailConfig:
    smtp_server: str | None
    smtp_port: int | None
    smtp_user: str | None
    smtp_password: str | None
    email_recipient: str | None
    email_sender: str | None
    test_email: str | None
    service_start: bool
    service_interval: str | None


def load_email_config() -> EmailConfig:
    smtp_port_raw = os.getenv("SMTP_PORT")
    smtp_port = int(smtp_port_raw) if smtp_port_raw else None
    smtp_user = os.getenv("SMTP_USER")
    email_sender = os.getenv("EMAIL_SENDER") or smtp_user

    return EmailConfig(
        smtp_server=os.getenv("SMTP_SERVER"),
        smtp_port=smtp_port,
        smtp_user=smtp_user,
        smtp_password=os.getenv("SMTP_PASSWORD"),
        email_recipient=os.getenv("EMAIL_RECIPIENT"),
        email_sender=email_sender,
        test_email=os.getenv("TEST_EMAIL"),
        service_start=_parse_bool(os.getenv("SERVICE_START"), True),
        service_interval=os.getenv("SERVICE_INTERVAL"),
    )


class Config:
    SMTP_SERVER = os.getenv("SMTP_SERVER")
    _smtp_port_env = os.getenv("SMTP_PORT")
    SMTP_PORT = int(_smtp_port_env) if _smtp_port_env else None
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

    EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")
    EMAIL_SENDER = os.getenv("EMAIL_SENDER") or SMTP_USER
    TEST_EMAIL = os.getenv("TEST_EMAIL")

    SERVICE_START = _parse_bool(os.getenv("SERVICE_START"), True)
    SERVICE_INTERVAL = os.getenv("SERVICE_INTERVAL")

    @classmethod
    def get_interval_params(cls):
        """Parses 'value unit' into APScheduler compatible kwargs."""
        if not cls.SERVICE_INTERVAL:
            return {"minutes": 60}

        parts = cls.SERVICE_INTERVAL.split()
        if len(parts) != 2:
            return {"minutes": 60}

        try:
            value = int(parts[0])
        except ValueError:
            return {"minutes": 60}

        unit = parts[1].lower()

        mapping = {
            "second": "seconds",
            "seconds": "seconds",
            "minute": "minutes",
            "minutes": "minutes",
            "hour": "hours",
            "hours": "hours",
            "day": "days",
            "days": "days",
            "week": "weeks",
            "weeks": "weeks",
            "month": "months",
            "months": "months",
        }

        arg_name = mapping.get(unit, "minutes")
        value = max(value, 1)
        return {arg_name: value}
