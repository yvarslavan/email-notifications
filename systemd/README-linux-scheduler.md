# Постоянный сервис с внутренним планировщиком (APScheduler)

Этот режим запускает постоянный сервис, который каждые 60 секунд (по умолчанию) запускает `Notific.py` через внутренний планировщик APScheduler. Сервис работает под пользователем `yvarslavan`.

## 1) Подготовьте проект на сервере Red Hat

### Создание пользователя (если не существует)
```bash
# Проверить существование пользователя
id yvarslavan || sudo useradd -m -s /bin/bash yvarslavan
```

### Подготовка директории и проекта
```bash
# Создать директорию проекта
sudo mkdir -p /opt/www/email_notifications_current
sudo chown yvarslavan:yvarslavan /opt/www/email_notifications_current

# Скопировать файлы проекта в /opt/www/email_notifications_current/
# (предполагается, что файлы уже загружены на сервер)

# Создать виртуальное окружение под пользователем yvarslavan
sudo -u yvarslavan python3 -m venv /opt/www/email_notifications_current/venv

# Установить зависимости
sudo -u yvarslavan /opt/www/email_notifications_current/venv/bin/pip install -r /opt/www/email_notifications_current/requirements.txt
```

## 2) Установите systemd unit

Скопируйте шаблон из `systemd/` проекта на сервер:

```bash
sudo cp /opt/www/email_notifications_current/systemd/email-notific.service /etc/systemd/system/email-notific.service
```

Содержимое unit файла уже настроено для:
- `WorkingDirectory=/opt/www/email_notifications_current`
- `ExecStart=/opt/www/email_notifications_current/venv/bin/python /opt/www/email_notifications_current/runner.py`
- `User=yvarslavan`
- `Environment=EMAIL_NOTIFIC_INTERVAL_SECONDS=60`

## 3) Активируйте сервис

```bash
sudo systemctl daemon-reload
sudo systemctl start email-notific.service
sudo systemctl status email-notific.service
```

## Включение автозапуска
После успешного тестирования включите автозапуск сервиса:
```bash
sudo systemctl enable email-notific.service
```

## Мониторинг и обслуживание

### Просмотр логов в реальном времени
```bash
# Логи systemd
sudo journalctl -u email-notific.service -f

# Логи приложения
tail -f /opt/www/email_notifications_current/notific.log
```

### Проверка статуса сервиса
```bash
sudo systemctl status email-notific.service
```

### Управление сервисом
```bash
# Остановка сервиса
sudo systemctl stop email-notific.service

# Запуск сервиса
sudo systemctl start email-notific.service

# Перезапуск сервиса
sudo systemctl restart email-notific.service

# Отключение автозапуска
sudo systemctl disable email-notific.service
```

## 4) Настройка интервала выполнения

Интервал между запусками задач настраивается через переменную окружения `EMAIL_NOTIFIC_INTERVAL_SECONDS` в unit файле (по умолчанию 60 секунд).

Для изменения интервала отредактируйте строку в `/etc/systemd/system/email-notific.service`:
```ini
Environment=EMAIL_NOTIFIC_INTERVAL_SECONDS=120
```

После изменения перезапустите сервис:
```bash
sudo systemctl daemon-reload
sudo systemctl restart email-notific.service
```

## 5) Настройка firewall (Red Hat)

Если требуется доступ к внешним ресурсам, убедитесь что firewall настроен:
```bash
# Проверить статус firewall
sudo firewall-cmd --state

# Разрешить исходящие соединения (обычно разрешены по умолчанию)
sudo firewall-cmd --permanent --add-service=mysql
sudo firewall-cmd --permanent --add-service=smtp
sudo firewall-cmd --reload
```

## 6) Замечания по окружению

- Сервис работает непрерывно с внутренним планировщиком APScheduler
- Скрипт ожидает доступ к MySQL (`helpdesk.teztour.com`) и SMTP (`mail.tez-tour.com`). Убедитесь, что сервер имеет доступ/маршрутизацию
- Сервис перезапускается автоматически при сбоях (`Restart=always`)
- Внутренний планировщик гарантирует, что задания не накладываются (`max_instances=1`, `coalesce=True`)
- Рабочая директория важна: от неё зависит путь к `notific.log` и импорт `html_template`

## 7) Как отключить сервис

```bash
sudo systemctl disable --now email-notific.service
```

## Команды для обслуживания

### Просмотр логов за последние 24 часа
```bash
sudo journalctl -u email-notific.service --since "24 hours ago"
```

### Очистка старых логов
```bash
sudo journalctl --vacuum-time=7d
```

### Проверка использования ресурсов
```bash
sudo systemctl show email-notific.service --property=MainPID,MemoryCurrent,CPUUsageNSec
```

---

## Quick Start для Red Hat сервера

```bash
# 1. Создать пользователя и директорию
sudo useradd -m -s /bin/bash yvarslavan
sudo mkdir -p /opt/www/email_notifications_current
sudo chown yvarslavan:yvarslavan /opt/www/email_notifications_current

# 2. Скопировать проект и настроить окружение
# (предполагается что файлы уже загружены)
sudo -u yvarslavan python3 -m venv /opt/www/email_notifications_current/venv
sudo -u yvarslavan /opt/www/email_notifications_current/venv/bin/pip install -r /opt/www/email_notifications_current/requirements.txt

# 3. Установить и запустить сервис
sudo cp /opt/www/email_notifications_current/systemd/email-notific.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now email-notific.service
sudo systemctl status email-notific.service
```
