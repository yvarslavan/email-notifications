# ⚡ Быстрый деплой Email Notifications

## 🪟 Windows - Пошаговые команды

### 1. Подготовка окружения
```cmd
# Переход в рабочую директорию
cd C:\Users\VARSLAVAN.DESKTOP-MNJ5CKG\PythonProjects

# Клонирование репозитория
git clone <repository-url> its.teztour.com
cd its.teztour.com

# Создание виртуального окружения
python -m venv venv

# Активация виртуального окружения
venv\Scripts\activate

# Обновление pip
python -m pip install --upgrade pip
```

### 2. Установка зависимостей
```cmd
# Установка всех зависимостей
pip install -r requirements.txt

# Проверка установки
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

### 3. Настройка конфигурации
```cmd
# Копирование примера конфигурации
copy .env.example .env

# Редактирование конфигурации (замените на ваши данные)
notepad .env
```

**Содержимое .env файла:**
```bash
SMTP_PASSWORD=your_actual_smtp_password
DB_PASSWORD=your_actual_database_password
EXECUTION_INTERVAL=300
EMAIL_NOTIFIC_INTERVAL_SECONDS=60
```

### 4. Тестирование
```cmd
# Тест однократного запуска
python Notific.py

# Если тест прошел успешно, запуск планировщика
python runner.py
```

### 5. Запуск сервиса
```cmd
# Вариант 1: Использование bat файла
start_service.bat

# Вариант 2: Использование менеджера
python manage_service.py

# Вариант 3: Ручной запуск
venv\Scripts\activate
python runner.py
```

---

## 🐧 Linux (Red Hat/CentOS) - Пошаговые команды

### 1. Подготовка системы
```bash
# Обновление системы
sudo yum update -y

# Установка Python 3 и pip (если не установлены)
sudo yum install -y python3 python3-pip git

# Проверка версий
python3 --version
pip3 --version
```

### 2. Создание пользователя и директории
```bash
# Создание пользователя
sudo useradd -m -s /bin/bash yvarslavan

# Создание директории проекта
sudo mkdir -p /opt/www/its.teztour.com
sudo chown yvarslavan:yvarslavan /opt/www/its.teztour.com

# Переход в директорию
cd /opt/www/its.teztour.com
```

### 3. Клонирование и настройка проекта
```bash
# Клонирование репозитория (под пользователем yvarslavan)
sudo -u yvarslavan git clone <repository-url> .

# Создание виртуального окружения
sudo -u yvarslavan python3 -m venv venv

# Активация и установка зависимостей
sudo -u yvarslavan /opt/www/its.teztour.com/venv/bin/pip install --upgrade pip
sudo -u yvarslavan /opt/www/its.teztour.com/venv/bin/pip install -r requirements.txt
```

### 4. Настройка конфигурации
```bash
# Копирование примера конфигурации
sudo -u yvarslavan cp .env.example .env

# Редактирование конфигурации
sudo -u yvarslavan nano .env
```

### 5. Установка systemd сервиса
```bash
# Копирование файла сервиса
sudo cp systemd/email-notific.service /etc/systemd/system/

# Перезагрузка systemd
sudo systemctl daemon-reload

# Включение автозапуска
sudo systemctl enable email-notific.service

# Запуск сервиса
sudo systemctl start email-notific.service

# Проверка статуса
sudo systemctl status email-notific.service
```

### 6. Настройка firewall (если необходимо)
```bash
# Проверка статуса firewall
sudo firewall-cmd --state

# Разрешение сервисов
sudo firewall-cmd --permanent --add-service=mysql
sudo firewall-cmd --permanent --add-service=smtp
sudo firewall-cmd --reload
```

---

## 🧪 Тестирование деплоя

### Тест подключения к базе данных
```bash
# Windows
python -c "import mysql.connector; print('MySQL connector OK')"

# Linux
sudo -u yvarslavan /opt/www/its.teztour.com/venv/bin/python -c "import mysql.connector; print('MySQL connector OK')"
```

### Тест SMTP подключения
```bash
# Windows
python -c "import smtplib; print('SMTP module OK')"

# Linux
sudo -u yvarslavan /opt/www/its.teztour.com/venv/bin/python -c "import smtplib; print('SMTP module OK')"
```

### Тест однократного запуска
```bash
# Windows
venv\Scripts\activate
python Notific.py

# Linux
sudo -u yvarslavan /opt/www/its.teztour.com/venv/bin/python /opt/www/its.teztour.com/Notific.py
```

---

## 📊 Мониторинг после деплоя

### Windows
```cmd
# Просмотр логов
type notific.log
type runner.log

# Мониторинг процессов
tasklist | findstr python.exe
```

### Linux
```bash
# Статус сервиса
sudo systemctl status email-notific.service

# Логи systemd
sudo journalctl -u email-notific.service -f

# Логи приложения
tail -f /opt/www/its.teztour.com/notific.log

# Процессы Python
ps aux | grep python
```

---

## 🔧 Быстрые команды управления

### Windows
```cmd
# Запуск
start_service.bat

# Остановка
stop_service.bat

# Менеджер
python manage_service.py
```

### Linux
```bash
# Запуск сервиса
sudo systemctl start email-notific.service

# Остановка сервиса
sudo systemctl stop email-notific.service

# Перезапуск сервиса
sudo systemctl restart email-notific.service

# Статус сервиса
sudo systemctl status email-notific.service

# Логи в реальном времени
sudo journalctl -u email-notific.service -f
```

---

## ⚠️ Важные замечания

1. **Безопасность**: Никогда не коммитьте файл `.env` с реальными паролями
2. **Права доступа**: Убедитесь, что у пользователя есть права на чтение/запись в директории проекта
3. **Сеть**: Проверьте доступность MySQL и SMTP серверов с сервера
4. **Логи**: Регулярно проверяйте логи на наличие ошибок
5. **Резервное копирование**: Сделайте резервную копию конфигурации перед изменениями

---

## 🆘 Экстренное восстановление

### Если сервис не запускается (Linux)
```bash
# Проверка логов
sudo journalctl -u email-notific.service -n 50

# Перезапуск с очисткой
sudo systemctl stop email-notific.service
sudo systemctl daemon-reload
sudo systemctl start email-notific.service

# Логи в реальном времени
sudo journalctl -u em
# Логи приложения
tail -f /opt/www/email_notifications_current/notific.log

# Проверка конфигурации
sudo systemd-analyze verify /etc/systemd/system/email-notific.service
```

### Если проблемы с зависимостями
```bash
# Переустановка зависимостей
sudo -u yvarslavan /opt/www/its.teztour.com/venv/bin/pip install --force-reinstall -r requirements.txt
```

### Если проблемы с правами доступа
```bash
# Исправление прав
sudo chown -R yvarslavan:yvarslavan /opt/www/its.teztour.com/
sudo chmod +x /opt/www/its.teztour.com/runner.py
```
