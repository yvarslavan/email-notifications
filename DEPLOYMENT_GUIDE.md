# 🚀 Подробное руководство по деплою и запуску проекта Email Notifications

## 📋 Содержание
1. [Подготовка сервера](#подготовка-сервера)
2. [Установка зависимостей](#установка-зависимостей)
3. [Настройка проекта](#настройка-проекта)
4. [Запуск на Windows](#запуск-на-windows)
5. [Запуск на Linux (systemd)](#запуск-на-linux-systemd)
6. [Мониторинг и обслуживание](#мониторинг-и-обслуживание)
7. [Устранение неполадок](#устранение-неполадок)

---

## 🖥️ Подготовка сервера

### Системные требования
- **Python 3.6+** (рекомендуется Python 3.8+)
- **MySQL/MariaDB** база данных
- **SMTP сервер** для отправки писем
- **Git** (для клонирования репозитория)

### Проверка системы
```bash
# Проверка версии Python
python3 --version
# или
python --version

# Проверка pip
pip3 --version
# или
pip --version

# Проверка Git
git --version
```

---

## 📦 Установка зависимостей

### 1. Клонирование репозитория
```bash
# Переходим в рабочую директорию
cd /opt/www  # для Linux
# или
cd C:\Projects  # для Windows

# Клонируем репозиторий
git clone <repository-url> email_notifications_current
cd email_notifications_current
```

### 2. Создание виртуального окружения

#### Windows:
```cmd
# Создание виртуального окружения
python -m venv venv

# Активация виртуального окружения
venv\Scripts\activate

# Проверка активации (должен показать путь к venv)
where python
```

#### Linux:
```bash
# Создание виртуального окружения
python3 -m venv venv

# Активация виртуального окружения
source venv/bin/activate

# Проверка активации (должен показать путь к venv)
which python
```

### 3. Установка Python зависимостей
```bash
# Обновляем pip до последней версии
pip install --upgrade pip

# Устанавливаем зависимости из requirements.txt
pip install -r requirements.txt

# Проверяем установленные пакеты
pip list
```

**Ожидаемый результат:**
```
Package                Version
---------------------- ---------
APScheduler            3.10.4
mysql-connector-python 8.0.32
python-dotenv          1.1.1
```

---

## ⚙️ Настройка проекта

### 1. Создание файла конфигурации
```bash
# Копируем пример конфигурации
cp .env.example .env

# Редактируем файл .env
nano .env  # Linux
# или
notepad .env  # Windows
```

### 2. Настройка .env файла
```bash
# Пароль для SMTP сервера
SMTP_PASSWORD=your_actual_smtp_password

# Пароль для подключения к базе данных MySQL
DB_PASSWORD=your_actual_database_password

# Дополнительные настройки (опционально)
EXECUTION_INTERVAL=300
EMAIL_NOTIFIC_INTERVAL_SECONDS=60
```

### 3. Проверка конфигурации базы данных
Убедитесь, что в файле `Notific.py` правильно настроены параметры подключения к MySQL:
- Хост базы данных
- Имя пользователя и пароль
- Название базы данных
- Порт (по умолчанию 3306)

### 4. Проверка конфигурации SMTP
В файле `Notific.py` настройте параметры SMTP сервера:
- SMTP хост и порт
- Учетные данные для аутентификации
- Настройки TLS/SSL

---

## 🪟 Запуск на Windows

### Вариант 1: Использование готовых bat файлов

#### Запуск сервиса:
```cmd
# Двойной клик на файл или из командной строки
start_service.bat
```

#### Остановка сервиса:
```cmd
# Двойной клик на файл или из командной строки
stop_service.bat
```

### Вариант 2: Ручной запуск

#### Однократный запуск:
```cmd
# Активируем виртуальное окружение
venv\Scripts\activate

# Запускаем Notific.py один раз
python Notific.py
```

#### Запуск планировщика:
```cmd
# Активируем виртуальное окружение
venv\Scripts\activate

# Запускаем планировщик
python runner.py
```

### Вариант 3: Использование manage_service.py
```cmd
# Активируем виртуальное окружение
venv\Scripts\activate

# Запускаем менеджер сервиса
python manage_service.py
```

**Меню управления:**
1. 📊 Показать статус
2. ⏰ Установить интервал выполнения
3. 🚀 Запустить Notific.py (одноразово)
4. 🔄 Запустить планировщик
5. ❌ Выход

### Вариант 4: Запуск как Windows Service (продвинутый)
```cmd
# Установка NSSM (Non-Sucking Service Manager)
# Скачать с https://nssm.cc/download

# Установка сервиса
nssm install EmailNotifications "C:\path\to\your\project\venv\Scripts\python.exe" "C:\path\to\your\project\runner.py"

# Запуск сервиса
nssm start EmailNotifications

# Остановка сервиса
nssm stop EmailNotifications

# Удаление сервиса
nssm remove EmailNotifications
```

---

## 🐧 Запуск на Linux (systemd)

### 1. Подготовка пользователя и директории
```bash
# Создание пользователя (если не существует)
sudo useradd -m -s /bin/bash yvarslavan

# Создание директории проекта
sudo mkdir -p /opt/www/email_notifications_current
sudo chown yvarslavan:yvarslavan /opt/www/email_notifications_current

# Копирование файлов проекта (предполагается, что файлы уже загружены)
# sudo cp -r /path/to/your/project/* /opt/www/email_notifications_current/
```

### 2. Настройка виртуального окружения
```bash
# Создание виртуального окружения под пользователем yvarslavan
sudo -u yvarslavan python3 -m venv /opt/www/email_notifications_current/venv

# Установка зависимостей
sudo -u yvarslavan /opt/www/email_notifications_current/venv/bin/pip install -r /opt/www/email_notifications_current/requirements.txt
```

### 3. Установка systemd сервиса
```bash
# Копирование файла сервиса
sudo cp /opt/www/email_notifications_current/systemd/email-notific.service /etc/systemd/system/

# Перезагрузка systemd
sudo systemctl daemon-reload

# Включение автозапуска
sudo systemctl enable email-notific.service

# Запуск сервиса
sudo systemctl start email-notific.service

# Проверка статуса
sudo systemctl status email-notific.service
```

### 4. Настройка интервала выполнения
```bash
# Редактирование файла сервиса
sudo nano /etc/systemd/system/email-notific.service

# Изменение строки Environment (например, на 120 секунд):
Environment=EMAIL_NOTIFIC_INTERVAL_SECONDS=120

# Перезагрузка и перезапуск сервиса
sudo systemctl daemon-reload
sudo systemctl restart email-notific.service
```

### 5. Настройка firewall (если необходимо)
```bash
# Проверка статуса firewall
sudo firewall-cmd --state

# Разрешение исходящих соединений
sudo firewall-cmd --permanent --add-service=mysql
sudo firewall-cmd --permanent --add-service=smtp
sudo firewall-cmd --reload
```

---

## 📊 Мониторинг и обслуживание

### Просмотр логов

#### Windows:
```cmd
# Логи основного модуля
type notific.log

# Логи планировщика
type runner.log

# Мониторинг в реальном времени (если установлен tail)
tail -f notific.log
```

#### Linux:
```bash
# Логи systemd
sudo journalctl -u email-notific.service -f

# Логи приложения
tail -f /opt/www/email_notifications_current/notific.log
tail -f /opt/www/email_notifications_current/runner.log

# Логи за последние 24 часа
sudo journalctl -u email-notific.service --since "24 hours ago"
```

### Управление сервисом (Linux)
```bash
# Проверка статуса
sudo systemctl status email-notific.service

# Остановка сервиса
sudo systemctl stop email-notific.service

# Запуск сервиса
sudo systemctl start email-notific.service

# Перезапуск сервиса
sudo systemctl restart email-notific.service

# Отключение автозапуска
sudo systemctl disable email-notific.service

# Включение автозапуска
sudo systemctl enable email-notific.service
```

### Проверка использования ресурсов
```bash
# Информация о процессе
sudo systemctl show email-notific.service --property=MainPID,MemoryCurrent,CPUUsageNSec

# Мониторинг процессов Python
ps aux | grep python
top -p $(pgrep -f runner.py)
```

---

## 🔧 Устранение неполадок

### Частые проблемы и решения

#### 1. Ошибка подключения к базе данных
```bash
# Проверка доступности MySQL
telnet helpdesk.teztour.com 3306

# Проверка учетных данных
mysql -h helpdesk.teztour.com -u easyredmine -p redmine
```

#### 2. Ошибка SMTP
```bash
# Проверка доступности SMTP
telnet mail.tez-tour.com 25

# Тест отправки письма
python -c "
import smtplib
smtp = smtplib.SMTP('mail.tez-tour.com', 25)
smtp.starttls()
smtp.login('help@tez-tour.com', 'your_password')
smtp.quit()
print('SMTP connection successful')
"
```

#### 3. Проблемы с правами доступа (Linux)
```bash
# Проверка прав на файлы
ls -la /opt/www/email_notifications_current/

# Исправление прав
sudo chown -R yvarslavan:yvarslavan /opt/www/email_notifications_current/
sudo chmod +x /opt/www/email_notifications_current/runner.py
```

#### 4. Проблемы с виртуальным окружением
```bash
# Пересоздание виртуального окружения
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 5. Проблемы с systemd
```bash
# Проверка конфигурации
sudo systemd-analyze verify /etc/systemd/system/email-notific.service

# Перезагрузка systemd
sudo systemctl daemon-reload

# Сброс failed состояния
sudo systemctl reset-failed email-notific.service
```

### Тестирование компонентов

#### Тест подключения к базе данных:
```python
# Создайте файл test_db.py
import mysql.connector

try:
    connection = mysql.connector.connect(
        host='helpdesk.teztour.com',
        user='easyredmine',
        password='your_password',
        database='redmine'
    )
    print("✅ Database connection successful")
    connection.close()
except Exception as e:
    print(f"❌ Database connection failed: {e}")
```

#### Тест SMTP:
```python
# Создайте файл test_smtp.py
import smtplib
from email.mime.text import MIMEText

try:
    smtp = smtplib.SMTP('mail.tez-tour.com', 25)
    smtp.starttls()
    smtp.login('help@tez-tour.com', 'your_password')
    print("✅ SMTP connection successful")
    smtp.quit()
except Exception as e:
    print(f"❌ SMTP connection failed: {e}")
```

---

## 📝 Быстрый старт

### Windows (быстрый запуск):
```cmd
git clone <repository-url> email_notifications_current
cd email_notifications_current
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# Отредактируйте .env файл
start_service.bat
```

### Linux (быстрый запуск):
```bash
sudo useradd -m -s /bin/bash yvarslavan
sudo mkdir -p /opt/www/email_notifications_current
sudo chown yvarslavan:yvarslavan /opt/www/email_notifications_current
# Скопируйте файлы проекта
sudo -u yvarslavan python3 -m venv /opt/www/email_notifications_current/venv
sudo -u yvarslavan /opt/www/email_notifications_current/venv/bin/pip install -r /opt/www/email_notifications_current/requirements.txt
sudo cp /opt/www/email_notifications_current/systemd/email-notific.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now email-notific.service
sudo systemctl status email-notific.service
```

---

## 🆘 Поддержка

При возникновении проблем:
1. Проверьте логи приложения (`notific.log`, `runner.log`)
2. Проверьте подключение к базе данных
3. Проверьте настройки SMTP сервера
4. Проверьте переменные окружения
5. Убедитесь, что все зависимости установлены

**Полезные команды для диагностики:**
```bash
# Проверка статуса сервиса (Linux)
sudo systemctl status email-notific.service

# Просмотр логов (Linux)
sudo journalctl -u email-notific.service -n 50

# Проверка процессов Python
ps aux | grep python

# Проверка сетевых соединений
netstat -tulpn | grep :3306  # MySQL
netstat -tulpn | grep :25    # SMTP
```
