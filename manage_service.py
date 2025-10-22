#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт управления сервисом email уведомлений
"""

import os
import sys
import time
import subprocess
import signal
from dotenv import load_dotenv

def load_config():
    """Загружает конфигурацию из .env файла"""
    load_dotenv()
    return {
        'interval': int(os.getenv('EXECUTION_INTERVAL', '300')),
        'smtp_password': os.getenv('SMTP_PASSWORD'),
        'db_password': os.getenv('DB_PASSWORD')
    }

def show_status():
    """Показывает текущий статус сервиса"""
    print("=" * 60)
    print("📊 СТАТУС СЕРВИСА EMAIL УВЕДОМЛЕНИЙ")
    print("=" * 60)

    config = load_config()
    print(f"⏰ Интервал выполнения: {config['interval']} секунд ({config['interval']/60:.1f} минут)")
    print(f"🔐 SMTP пароль: {'✅ Установлен' if config['smtp_password'] else '❌ Не установлен'}")
    print(f"🗄️  DB пароль: {'✅ Установлен' if config['db_password'] else '❌ Не установлен'}")

    # Проверяем запущенные процессы
    try:
        result = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq python.exe'],
                              capture_output=True, text=True)
        python_processes = [line for line in result.stdout.split('\n') if 'python.exe' in line]
        print(f"🐍 Процессов Python: {len(python_processes)}")

        if python_processes:
            print("📋 Запущенные процессы:")
            for process in python_processes[:3]:  # Показываем первые 3
                print(f"   {process.strip()}")
    except:
        print("🐍 Не удалось проверить процессы Python")

    print("=" * 60)

def set_interval():
    """Устанавливает новый интервал выполнения"""
    print("⏰ УСТАНОВКА ИНТЕРВАЛА ВЫПОЛНЕНИЯ")
    print("=" * 40)

    while True:
        try:
            interval = input("Введите интервал в секундах (60-3600): ")
            interval = int(interval)

            if interval < 60:
                print("❌ Минимум 60 секунд")
                continue
            elif interval > 3600:
                print("❌ Максимум 3600 секунд (1 час)")
                continue

            # Обновляем .env файл
            with open('.env', 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # Ищем строку с EXECUTION_INTERVAL
            updated = False
            for i, line in enumerate(lines):
                if line.startswith('EXECUTION_INTERVAL='):
                    lines[i] = f'EXECUTION_INTERVAL={interval}\n'
                    updated = True
                    break

            if not updated:
                lines.append(f'EXECUTION_INTERVAL={interval}\n')

            with open('.env', 'w', encoding='utf-8') as f:
                f.writelines(lines)

            print(f"✅ Интервал установлен: {interval} секунд ({interval/60:.1f} минут)")
            break

        except ValueError:
            print("❌ Введите корректное число")
        except Exception as e:
            print(f"❌ Ошибка: {e}")

def run_once():
    """Запускает Notific.py один раз"""
    print("🚀 ЗАПУСК NOTIFIC.PY (ОДНОРАЗОВО)")
    print("=" * 40)

    try:
        result = subprocess.run([sys.executable, 'Notific.py'],
                              capture_output=True, text=True, timeout=60)

        if result.returncode == 0:
            print("✅ Notific.py выполнен успешно")
        else:
            print(f"❌ Notific.py завершился с ошибкой (код: {result.returncode})")
            if result.stderr:
                print(f"💥 Ошибки: {result.stderr}")
    except subprocess.TimeoutExpired:
        print("⏰ Notific.py превысил лимит времени (60 секунд)")
    except Exception as e:
        print(f"💥 Ошибка запуска: {e}")

def start_scheduler():
    """Запускает планировщик"""
    print("🚀 ЗАПУСК ПЛАНИРОВЩИКА")
    print("=" * 40)

    config = load_config()
    print(f"⏰ Интервал: {config['interval']} секунд ({config['interval']/60:.1f} минут)")
    print("🔄 Планировщик запускается...")
    print("⚠️  Для остановки нажмите Ctrl+C")

    try:
        subprocess.run([sys.executable, 'runner.py'])
    except KeyboardInterrupt:
        print("\n🛑 Планировщик остановлен")

def show_menu():
    """Показывает главное меню"""
    while True:
        print("\n" + "=" * 60)
        print("🎛️  УПРАВЛЕНИЕ СЕРВИСОМ EMAIL УВЕДОМЛЕНИЙ")
        print("=" * 60)
        print("1. 📊 Показать статус")
        print("2. ⏰ Установить интервал выполнения")
        print("3. 🚀 Запустить Notific.py (одноразово)")
        print("4. 🔄 Запустить планировщик")
        print("5. ❌ Выход")
        print("=" * 60)

        choice = input("Выберите действие (1-5): ").strip()

        if choice == '1':
            show_status()
        elif choice == '2':
            set_interval()
        elif choice == '3':
            run_once()
        elif choice == '4':
            start_scheduler()
        elif choice == '5':
            print("👋 До свидания!")
            break
        else:
            print("❌ Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    show_menu()
