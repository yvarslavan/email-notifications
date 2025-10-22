#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import subprocess
import logging
from logging.handlers import RotatingFileHandler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
import signal

# Настройка логирования с ротацией
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Ротация логов: максимум 5MB, 3 файла
file_handler = RotatingFileHandler(
    'runner.log',
    maxBytes=5*1024*1024,  # 5MB
    backupCount=3,
    encoding='utf-8'
)
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Консольный обработчик только для WARNING и выше
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)  # Изменено с INFO на WARNING
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

def get_execution_interval():
    """Получает интервал выполнения из переменной окружения с обработкой ошибок."""
    try:
        interval = int(os.getenv('EXECUTION_INTERVAL', '300'))  # По умолчанию 5 минут
        original_interval = interval

        if interval < 60:  # Минимум 1 минута
            logger.warning("⚠️  Интервал выполнения слишком мал (%d сек), установлен минимум 60 сек" % interval)
            interval = 60
        elif interval > 3600:  # Максимум 1 час
            logger.warning("⚠️  Интервал выполнения слишком велик (%d сек), установлен максимум 3600 сек" % interval)
            interval = 3600

        if original_interval != interval:
            logger.info("📝 Интервал изменен с %d на %d секунд" % (original_interval, interval))

        return interval
    except (ValueError, TypeError) as e:
        logger.error("💥 Ошибка получения интервала выполнения: %s. Используется значение по умолчанию 300 сек" % str(e))
        return 300

def run_once():
    """Выполняет Notific.py один раз с улучшенной обработкой ошибок."""
    start_time = time.time()
    logger.info("🔄 " + "=" * 50)
    logger.info("🚀 ЗАПУСК NOTIFIC.PY")
    logger.info("⏰ Время запуска: %s" % time.strftime("%Y-%m-%d %H:%M:%S"))

    try:
        # Определяем путь к Python и скрипту
        python_executable = sys.executable
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Notific.py')

        # Проверяем существование скрипта
        if not os.path.exists(script_path):
            logger.error("❌ Файл Notific.py не найден по пути: %s" % script_path)
            return False

        logger.info("📁 Путь к скрипту: %s" % script_path)
        logger.info("🐍 Python интерпретатор: %s" % python_executable)

        # Запускаем процесс с таймаутом
        result = subprocess.run(
            [python_executable, script_path],
            capture_output=True,
            text=True,
            timeout=1800,  # 30 минут таймаут
            encoding='utf-8',
            errors='replace'
        )

        execution_time = time.time() - start_time
        logger.info("⏱️  Время выполнения: %.2f секунд" % execution_time)

        if result.returncode == 0:
            logger.info("✅ Notific.py выполнен успешно")
            # Логируем только важные сообщения из stdout
            if result.stdout.strip():
                for line in result.stdout.strip().split('\n'):
                    if any(keyword in line.lower() for keyword in ['error', 'warning', 'exception', 'failed']):
                        logger.warning("⚠️  Вывод Notific.py: %s" % line.strip())
            logger.info("🔄 " + "=" * 50)
            return True
        else:
            logger.error("❌ Notific.py завершился с кодом ошибки %d" % result.returncode)
            if result.stderr:
                logger.error("💥 Ошибки Notific.py: %s" % result.stderr.strip())
            if result.stdout:
                logger.error("📋 Вывод Notific.py: %s" % result.stdout.strip())
            logger.info("🔄 " + "=" * 50)
            return False

    except subprocess.TimeoutExpired:
        execution_time = time.time() - start_time
        logger.error("⏰ Notific.py превысил лимит времени выполнения (30 минут)")
        logger.error("⏱️  Время до таймаута: %.2f секунд" % execution_time)
        logger.info("🔄 " + "=" * 50)
        return False
    except subprocess.CalledProcessError as e:
        execution_time = time.time() - start_time
        logger.error("💥 Ошибка выполнения Notific.py: код %d, сообщение: %s" % (e.returncode, str(e)))
        logger.error("⏱️  Время до ошибки: %.2f секунд" % execution_time)
        logger.info("🔄 " + "=" * 50)
        return False
    except FileNotFoundError:
        execution_time = time.time() - start_time
        logger.error("🐍 Python интерпретатор не найден: %s" % python_executable)
        logger.error("⏱️  Время до ошибки: %.2f секунд" % execution_time)
        logger.info("🔄 " + "=" * 50)
        return False
    except Exception as e:
        execution_time = time.time() - start_time
        logger.error("💥 Неожиданная ошибка при выполнении Notific.py: %s" % str(e))
        logger.error("🔍 Тип ошибки: %s" % type(e).__name__)
        logger.error("⏱️  Время до ошибки: %.2f секунд" % execution_time)
        import traceback
        logger.error("📋 Трассировка ошибки:\n%s" % traceback.format_exc())
        logger.info("🔄 " + "=" * 50)
        return False

def signal_handler(signum, frame):
    """Обработчик сигналов для корректного завершения."""
    logger.info("Получен сигнал %d, завершение работы..." % signum)
    sys.exit(0)

def main():
    """Основная функция планировщика с улучшенной обработкой ошибок."""
    logger.info("=" * 60)
    logger.info("🚀 ЗАПУСК ПЛАНИРОВЩИКА EMAIL УВЕДОМЛЕНИЙ")
    logger.info("=" * 60)
    logger.info("Время запуска: %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    logger.info("Версия Python: %s" % sys.version.split()[0])
    logger.info("Рабочая директория: %s" % os.getcwd())

    # Регистрируем обработчики сигналов
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    try:
        # Получаем интервал выполнения
        interval = get_execution_interval()
        logger.info("⏰ Интервал выполнения: %d секунд (%.1f минут)" % (interval, interval/60))

        # Создаем планировщик
        scheduler = BlockingScheduler()

        # Добавляем задачу
        scheduler.add_job(
            func=run_once,
            trigger=IntervalTrigger(seconds=interval),
            id='notific_job',
            name='Email Notifications Job',
            max_instances=1,  # Только одна задача одновременно
            coalesce=True,    # Объединяем пропущенные запуски
            misfire_grace_time=30  # 30 секунд на опоздание
        )

        logger.info("✅ Планировщик настроен и готов к работе")
        logger.info("📋 Задача 'Email Notifications Job' добавлена")
        logger.info("🔄 Следующий запуск через %d секунд" % interval)
        logger.info("=" * 60)

        # Запускаем планировщик
        scheduler.start()

    except KeyboardInterrupt:
        logger.info("⚠️  Получен сигнал прерывания (Ctrl+C), завершение работы...")
    except SystemExit:
        logger.info("⚠️  Системный выход, завершение работы...")
    except Exception as e:
        logger.error("💥 КРИТИЧЕСКАЯ ОШИБКА ПЛАНИРОВЩИКА: %s" % str(e))
        logger.error("🔍 Тип ошибки: %s" % type(e).__name__)
        import traceback
        logger.error("📋 Трассировка ошибки:\n%s" % traceback.format_exc())
        sys.exit(1)
    finally:
        logger.info("=" * 60)
        logger.info("🛑 ПЛАНИРОВЩИК ОСТАНОВЛЕН")
        logger.info("Время остановки: %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
        logger.info("=" * 60)

if __name__ == "__main__":
    main()
