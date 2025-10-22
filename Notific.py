#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding=utf8
import smtplib
import sys
import time
import html_template as f
import logging
import ssl
import os
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

# Настройка логирования с ротацией
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Изменено с DEBUG на INFO

# Ротация логов: максимум 10MB, 5 файлов
file_handler = RotatingFileHandler(
    'notific.log',
    maxBytes=10*1024*1024,  # 10MB
    backupCount=5,
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

logger.info("Запуск Notific.py")
# Раскоментить Для Unix

# Код для Python 2 (закомментирован для Python 3)
# try:
#     reload(sys)
#     sys.setdefaultencoding("utf-8")
# except NameError:
#     pass

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import mysql.connector

# import datetime  # не используется
import re

# Константы для конфигурации
EXCLUDED_REDMINE_USERS = ['a.repin@tez-tour.com']
SMTP_SERVER = "mail.tez-tour.com"
SMTP_PORT = 25
SMTP_USER = "help@tez-tour.com"
DB_USER = 'easyredmine'
DB_HOST = 'helpdesk.teztour.com'
DB_NAME = 'redmine'

# Константы для проектов
PROJECT_MOSCOW = [1, 134, 109]  # Входящие (Москва), Входящие (Москва) Бизнес-анализ, Задачи по 1С
PROJECT_UKRAINE = 140
PROJECT_SPAIN = 129
PROJECT_CONTENT = 132
PROJECT_EGYPT = 139
PROJECT_UFA = [153, 154]

# Константы для статусов
STATUS_CLOSED = 'Закрыта'
STATUS_COMPLETED = 'Выполнена'

# Константы для доменов
DOMAIN_VILNIUS = "@teztour.lt"

def validate_email(email):
    """Проверяет корректность email-адреса.

    Args:
        email (str): Email для проверки.

    Returns:
        bool: True если email корректный, False в противном случае.
    """
    if not email or not isinstance(email, str):
        return False

    # Базовая проверка на корректность email
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email))

def is_redmine_user(cursor, email):
    """Проверяет, является ли email пользователем Redmine.

    Args:
        cursor: Объект курсора для выполнения SQL-запросов.
        email (str): Email для проверки.

    Returns:
        bool: True если пользователь является пользователем Redmine, False в противном случае.
    """
    try:
        query = """
            SELECT u.id
            FROM redmine.users u
            INNER JOIN redmine.email_addresses ea ON u.id = ea.user_id
            WHERE ea.address = %s AND u.type = 'User'
        """
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        is_user = result is not None
        # Убираем избыточное логирование - только для отладки
        logger.debug("Проверка пользователя Redmine для %s: %s" % (email, 'является пользователем' if is_user else 'НЕ является пользователем'))
        return is_user
    except Exception as e:
        logger.error("Ошибка проверки пользователя Redmine для %s: %s" % (email, str(e)))
        return False

def should_send_email(email):
    """Проверяет, следует ли отправлять email на указанный адрес.

    Args:
        email (str): Email адрес для проверки.

    Returns:
        bool: True если email должен получать уведомления, False в противном случае.
    """
    # Убираем избыточное логирование
    logger.debug("Проверяем отправку email для: %s" % email)

    # Проверяем, не находится ли email в списке исключений
    if email in EXCLUDED_REDMINE_USERS:
        logger.info("Email %s найден в списке исключений - ПРОПУСКАЕМ отправку" % email)
        return False
    else:
        logger.debug("Email %s НЕ в списке исключений - разрешаем отправку" % email)
        return True

# Настройки SMTP сервера
server = SMTP_SERVER
port = SMTP_PORT
user_name = SMTP_USER
user_passwd = os.getenv('SMTP_PASSWORD')

# Проверяем, что пароль SMTP загружен
if not user_passwd:
    logger.error("SMTP_PASSWORD не найден в переменных окружения!")
    sys.exit(1)

def clean_email_string(email_str):
    """Очищает строку email от лишних символов и валидирует формат.

    Args:
        email_str (str): Строка с email адресом для очистки.

    Returns:
        str: Очищенный email адрес или пустая строка если адрес некорректен.
    """
    if not email_str or not isinstance(email_str, str):
        return ""

    # Убираем лишние пробелы и переводы строк
    cleaned = email_str.strip().replace('\n', '').replace('\r', '')

    # Базовая валидация email
    if '@' not in cleaned or '.' not in cleaned.split('@')[-1]:
        return ""

    # Проверяем на недопустимые символы
    invalid_chars = ['<', '>', '"', "'", ';', ',']
    for char in invalid_chars:
        if char in cleaned:
            return ""

    return cleaned

def send_email(me, you, text, subj):
    """Отправляет email с улучшенной обработкой ошибок и валидацией адресов."""

    # Очищаем и валидируем email получателя
    clean_recipient = clean_email_string(you)
    if not clean_recipient:
        logger.error("Некорректный email получателя: %s. Отправка пропущена." % you)
        return False

    # Если email был очищен, логируем это
    if clean_recipient != you:
        logger.warning("Email получателя очищен с '%s' на '%s'" % (you, clean_recipient))

    # Проверяем, следует ли отправлять email
    if not should_send_email(clean_recipient):
        logger.info("Пропускаем отправку email на %s - адрес исключен" % clean_recipient)
        return False

    try:
        # Формируем заголовок письма
        msg = MIMEMultipart('mixed')
        msg['Subject'] = Header(subj, 'utf-8')
        msg['From'] = me
        msg['To'] = you

        # Проверяем, что text является строкой
        if not isinstance(text, str):
            text = str(text)

        # Формируем письмо
        part = MIMEText(text, 'html', "utf-8")
        msg.attach(part)

        # Подключение с обработкой ошибок
        context = ssl.create_default_context()
        try:
            context.minimum_version = ssl.TLSVersion.TLSv1_2
            context.maximum_version = ssl.TLSVersion.TLSv1_2
            context.set_ciphers('DEFAULT:@SECLEVEL=1')
        except Exception as ssl_err:
            logger.warning("Ошибка настройки SSL контекста: %s" % str(ssl_err))

        # SMTP соединение с обработкой ошибок
        s = smtplib.SMTP(server, port)
        s.ehlo()
        s.starttls(context=context)
        s.ehlo()
        s.login(user_name, user_passwd)
        s.sendmail(me, you, msg.as_string())
        s.quit()

        logger.debug("Email успешно отправлен на %s" % you)
        time.sleep(1)  # делаем небольшую паузу

    except smtplib.SMTPException as smtp_err:
        logger.error("SMTP ошибка при отправке email на %s: %s" % (you, str(smtp_err)))
        raise
    except Exception as e:
        logger.error("Общая ошибка при отправке email на %s: %s" % (you, str(e)))
        raise

def Double_rows(): #Пометка заявок с одинаковой темой для Уфы (Заказчик Наталья Яковлева)
    logger.info("🔄 Выполняем функцию Double_rows...")
    sql = """SELECT i.ID FROM issues i
             INNER JOIN custom_values cv ON i.id = cv.customized_id
             WHERE i.project_id = 154 AND cv.custom_field_id = 20 AND cv.value = ''
             GROUP BY i.subject HAVING count(*) > 1 ORDER BY count(*)"""
    cursor.execute(sql)
    res = cursor.fetchall()
    logger.info("📊 Найдено дублирующихся заявок: %d" % len(res))
    if res:
        for row in res:
            issueID = row[0]
            logger.info("🔧 Обновляем заявку ID: %s" % issueID)
            # Используем параметризованный запрос для защиты от SQL-инъекций
            update_custom_values = """UPDATE redmine.custom_values
                                     SET value = 1
                                     WHERE custom_field_id = 20 AND customized_id = %s"""
            cursor.execute(update_custom_values, (issueID,))

    del_subject = "DELETE FROM u_subject"
    cursor.execute(del_subject)
    logger.info("✅ Выполнен запрос: DELETE FROM u_subject")

def Show_notes (issueID) :
    # Используем параметризованный запрос для защиты от SQL-инъекций
    query = """SELECT notes FROM redmine.journals
               WHERE journalized_id = %s
               AND user_id = (SELECT assigned_to_id FROM redmine.issues i WHERE id = %s)
               AND notes LIKE '%%<p>%%'
               AND created_on = (SELECT MAX(created_on) FROM redmine.journals
                                WHERE journalized_id = %s
                                AND user_id = (SELECT assigned_to_id FROM redmine.issues i WHERE id = %s)
                                AND notes LIKE '%%<p>%%')"""
    cursor.execute(query, (issueID, issueID, issueID, issueID))
    result = cursor.fetchone()
    if result is not None:
        note = result[0]
    else:
        note = ''
    return note

# Настройки подключения к базе данных
db_password = os.getenv('DB_PASSWORD')
if not db_password:
    logger.error("DB_PASSWORD не найден в переменных окружения!")
    sys.exit(1)

try:
    logger.info("Подключение к базе данных %s@%s/%s..." % (DB_USER, DB_HOST, DB_NAME))
    cnx = mysql.connector.connect(
        user=DB_USER,
        password=db_password,
        host=DB_HOST,
        database=DB_NAME,
        connection_timeout=10,  # 10 секунд таймаут
        autocommit=True
    )
    logger.info("✅ Подключение к базе данных установлено")
except mysql.connector.Error as e:
    logger.error("❌ Ошибка подключения к базе данных: %s" % str(e))
    logger.error("🔍 Проверьте доступность сервера %s и правильность пароля" % DB_HOST)
    sys.exit(1)
except Exception as e:
    logger.error("💥 Неожиданная ошибка при подключении к БД: %s" % str(e))
    sys.exit(1)
cursor = cnx.cursor(buffered=True)
logger.info("✅ Курсор базы данных создан")

del_IssueID = "DELETE FROM u_IssueID_for_Watchers LIMIT 1"
cursor.execute(del_IssueID)
logger.info("✅ Выполнен запрос: DELETE FROM u_IssueID_for_Watchers")

query = "SELECT subject FROM u_subject"
cursor.execute(query)
result = cursor.fetchall()
logger.info("✅ Выполнен запрос: SELECT subject FROM u_subject, найдено записей: %d" % len(result))
for row in result:
    subject_email = str(row[0])
    logger.info("📋 Обрабатываем subject: %s" % subject_email)
    Double_rows() # Пометка заявок с одинаковой темой для Уфы (Заказчик Наталья Яковлева)
    # del_subject = "DELETE FROM u_subject";

# Отбивка на новую задачу в Редмайн
logger.info("🔄 Переходим к обработке новых задач...")
new_issues = "SELECT issueID, subject, description, status, created_on, easy_email_to, project_id, watcher  FROM u_new_issues"
cursor.execute(new_issues)
result = cursor.fetchall()
logger.info("📊 Найдено новых задач для обработки: %d" % len(result))

for row in result:
    issueID = str(row[0])
    subject_email = str(row[1])
    description = row[2]
    status = row[3]
    created_on = row[4]
    easy_email_to = row[5]
    project_id = row[6]
    watcher = row[7]

    logging.debug("Обрабатываем новую задачу %s для email: %s" % (issueID, easy_email_to))


    # Используем параметризованный запрос
    del_new_issues = "DELETE FROM u_new_issues WHERE IssueID = %s"
    if project_id in PROJECT_MOSCOW: # Входящие (Москва) или Входящие (Москва) Бизнес-анализ или Задачи по 1С
        # Проверяем домен почты (Костыль для Вильнюса, заказчик Санников Евгений)
        if DOMAIN_VILNIUS in easy_email_to:
            subject = "Новое обращение в IT Департамент TEZ TOUR (#" + issueID + ' ' + subject_email + ")"
            emailMessage = f.template_html_new_issue_vln(issueID, subject_email, description, status, created_on)
        else:
            if watcher == 1: # Если отбивка для наблюдателя
                subject = "Уведомление от IT Департамента TEZ TOUR (#" + issueID + ' ' + subject_email + ")"
                emailMessage = f.template_html_new_issue_msk_watcher(issueID, subject_email, description, status, created_on)
            else:
                subject = "Новое обращение в IT Департамент TEZ TOUR (#" + issueID + ' ' + subject_email + ")"
                emailMessage = f.template_html_new_issue_msk(issueID, subject_email, description, status, created_on)
                # emailMessage_new = f.template_html_new_issue_msk_new_template(issueID, subject_email, description, status, created_on)
        send_email("help@tez-tour.com", easy_email_to, emailMessage, subject)  # отправляем  почту
        # send_email("help@tez-tour.com", 'y.varslavan@tez-tour.com', emailMessage_new, subject, cursor)  # отправляем  почту с новым шаблоном

        cursor.execute(del_new_issues, (issueID,))
    if project_id == PROJECT_UKRAINE: # Входящие (Украина)
        if watcher == 1: # Если отбивка для наблюдателя
            subject = "Уведомление от ИТ отдела Тез Тур Украина (#" + issueID + ' ' + subject_email + ")"
            emailMessage = f.template_html_new_issue_ukr_watcher(issueID, subject_email, description, status, created_on)
        else:
            subject = "Новая заявка в ИТ отдел Тез Тур Украина (#" + issueID + ' ' + subject_email + ")"
            emailMessage = f.template_html_new_issue_ukr(issueID, subject_email, description, status, created_on)
        send_email("it@teztour.com.ua", easy_email_to, emailMessage, subject)  # отправляем  почту
        cursor.execute(del_new_issues, (issueID,))
    if project_id == PROJECT_SPAIN: # Входящие (Испания)
        subject = "Новое обращение в службу технической поддержки TEZ TOUR Spain (#" + issueID + ' ' + subject_email + ")"
        emailMessage = f.template_html_new_issue_spain(issueID, subject_email, description, status, created_on)
        send_email("help@tez-tour.es", easy_email_to, emailMessage, subject)  # отправляем  почту
        cursor.execute(del_new_issues, (issueID,))
    if project_id == PROJECT_CONTENT:  # Входящие (Контент)
        subject = "Новое обращение в Контент-Центр TEZ TOUR (#" + issueID + ' ' + subject_email + ")"
        emailMessage = f.template_html_new_issue_content(issueID, subject_email, description, status, created_on)
        send_email("content@tez-tour.com", easy_email_to, emailMessage, subject)  # отправляем  почту
        cursor.execute(del_new_issues, (issueID,))
    if project_id == PROJECT_EGYPT:  # Incoming (Egypt)
        subject = "A New Case in Technical support TEZ TOUR Egypt(Development Department) (#" + issueID + ")"
        status = "New"
        emailMessage = f.template_html_new_issue_egypt(issueID, subject_email, description, status, created_on)
        send_email("help.eg@tez-tour.com", easy_email_to, emailMessage, subject)  # отправляем  почту
        cursor.execute(del_new_issues, (issueID,))
    # if project_id == 203:  # Входящие (Контент Минск)
    #     subject = "Новое обращение в Контент-Центр TEZ TOUR Минск (#" + issueID + ")"
    #     emailMessage = f.template_html_new_issue_content_Minsk(issueID, subject_email, description, status, created_on)
    #     send_email("content@minsk.tez-tour.com", easy_email_to, emailMessage, subject)  # отправляем  почту
    #     cursor.execute(del_new_issues)


    # if project_id == 154:  # Входящие для Уфы (проекты Расчет заявок, Ценовые предложения, Агентства Уфы)
    #    Double_rows() # Пометка заявок с одинаковой темой для Уфы (Заказчик Наталья Яковлева)
    #     subject = "Новое обращение" #TEZ TOUR Уфа
    #     emailMessage = f.template_html_new_issue_Ufa(issueID, subject_email, description, status, created_on)
    #     send_email("ufa@ufa.tez-tour.com", easy_email_to, emailMessage, subject)  # отправляем  почту
    #     cursor.execute(del_new_issues)

del_new_issues = "DELETE FROM u_new_issues WHERE project_id NOT IN(1,109,129,132,134,139,140,153,154,155)"
cursor.execute(del_new_issues)
logger.info("✅ Выполнен запрос: DELETE FROM u_new_issues WHERE project_id NOT IN(...)")

# Изменение статуса
logger.info("🔄 Переходим к обработке изменений статуса...")
sel_issues = "SELECT IssueID, email,Subj,Body,OldStatus,NewStatus,DateCreated,OldSubj,UserRedmine,Author,Assigned,Priority,mailbox_username,projectID FROM u_update_status"
cursor.execute(sel_issues)
result = cursor.fetchall()
logger.info("📊 Найдено записей для обработки изменений статуса: %d" % len(result))

for row in result:
    issueID = str(row[0])
    email = str(row[1])
    subj = row[2]
    body = row[3]
    oldStatus = row[4]
    newStatus = row[5]
    dateCreated = str(row[6])
    title = str(row[7])
    userRedmine = row[8]
    author = str(row[9])
    assigned = str(row[10])
    priority = str(row[11])
    mailbox_username = str(row[12])
    projectID = row[13]
    status = newStatus

    logging.info("Обрабатываем изменение статуса для задачи %s, email: %s, userRedmine: %d" % (issueID, email, userRedmine))

    # Проверяем, следует ли отправлять email
    if not should_send_email(email):
        logging.info("Пропускаем отправку уведомления об изменении статуса на %s - адрес исключен" % email)
        # Удаляем запись из базы, даже если не отправляем email
        del_issues = "DELETE FROM u_update_status WHERE IssueID = %s"
        cursor.execute(del_issues, (issueID,))
        continue

    logging.debug("Обрабатываем задачу IssueID: %s, email: %s, newStatus: %s, userRedmine: %d" % (issueID, email, newStatus, userRedmine))

    add_notes = Show_notes(issueID)  # добавление примечания исполнителя к тексту задачи
    add_notes = add_notes if add_notes is not None else ""  # Если None, заменяем на пустую строку
    logging.debug("Примечания для задачи: %s" % add_notes)

    # Блок 1: Redmine-пользователь, статус "Закрыта"
    if userRedmine == 1 and newStatus == STATUS_CLOSED:
        if projectID in PROJECT_UFA:
            logging.info("Используем шаблон template_html_Assigned_Ufa для проекта %d" % projectID)
            emailMessage = f.template_html_Assigned_Ufa(issueID, body, 'Статус', oldStatus, newStatus, dateCreated, title, author, status, priority, assigned, add_notes) + f.html_footer()
        else:
            if email and DOMAIN_VILNIUS in email:
                logging.info("Используем шаблон template_html_Assigned_vln для email: %s" % email)
                emailMessage = f.template_html_Assigned_vln(issueID, body, 'Статус', oldStatus, newStatus, dateCreated, title, author, status, priority, assigned, add_notes)
            else:
                logging.info("Используем шаблон template_html_Assigned для email: %s" % email)
                emailMessage = f.template_html_Assigned(issueID, body, 'Статус', oldStatus, newStatus, dateCreated, title, author, status, priority, assigned, add_notes) + f.html_contact() # + f.html_footer()


    # Блок 2: Redmine-пользователь, статус не "Закрыта"
    elif userRedmine == 1 and newStatus != 'Закрыта':
        if email and "@teztour.lt" in email:
            logging.info("Используем шаблон template_html_Assigned_vln для email: %s" % email)
            emailMessage = f.template_html_Assigned_vln(issueID, body, 'Статус', oldStatus, newStatus, dateCreated, title, author, status, priority, assigned, add_notes)
        else:
            logging.info("Используем шаблон template_html_Assigned для email: %s" % email)
            emailMessage = f.template_html_Assigned(issueID, body, 'Статус', oldStatus, newStatus, dateCreated, title, author, status, priority, assigned, add_notes) # + f.html_footer()

    # Блок 3: Не Redmine-пользователь, статус "Закрыта"
    elif userRedmine == 0 and newStatus == STATUS_CLOSED:
        if projectID in PROJECT_UFA:
            logging.info("Используем шаблон template_html_Ufa для проекта %d" % projectID)
            emailMessage = f.template_html_Ufa(issueID, body, 'Статус', oldStatus, newStatus, dateCreated, author, status, priority, assigned) + f.html_footer()
        else:
            if email and DOMAIN_VILNIUS in email:
                logging.info("Используем шаблон template_html_Assigned_vln для email: %s" % email)
                emailMessage = f.template_html_Assigned_vln(issueID, body, 'Статус', oldStatus, newStatus, dateCreated, author, status, priority, assigned, add_notes)
            else:
                logging.info("Используем шаблон template_html для email: %s" % email)
                emailMessage = f.template_html(issueID, body, 'Статус', oldStatus, newStatus, dateCreated, author, status, priority, assigned) + f.html_contact() # + f.html_footer()

    # Блок 4: Не Redmine-пользователь, статус не "Закрыта"
    elif userRedmine == 0 and newStatus != 'Закрыта':
        if email and "@teztour.lt" in email:
            logging.info("Используем шаблон template_html_Assigned_vln для email: %s" % email)
            emailMessage = f.template_html_Assigned_vln(issueID, body, 'Статус', oldStatus, newStatus, dateCreated, author, status, priority, assigned, add_notes)
        else:
            logging.info("Используем шаблон template_html для email: %s" % email)
            emailMessage = f.template_html(issueID, body, 'Статус', oldStatus, newStatus, dateCreated, author, status, priority, assigned) # + f.html_footer()


    # emailMessage_new = f.template_html_new(issueID, body, 'Статус', oldStatus, newStatus, dateCreated, author, status, priority, assigned)

    del_issues = "DELETE FROM u_update_status WHERE IssueID = %s"
    try:
        logging.info("Отправляем email на %s с темой: %s" % (email, subj))
        send_email(mailbox_username, email, emailMessage, subj)

        # send_email(mailbox_username, 'y.varslavan@tez-tour.com', emailMessage_new, subj, cursor)

        logging.info("Email успешно отправлен на %s" % email)
    except Exception as e:
        EmailNote = "Сбой отправки email на адрес %s: %s" % (email, str(e))
        logging.error(EmailNote)
    finally:
        cursor.execute(del_issues, (issueID,))
        logging.info("Запись с IssueID %s удалена из u_update_status" % issueID)

del_issues = "DELETE FROM u_update_status WHERE NewStatus = %s"
cursor.execute(del_issues, (STATUS_COMPLETED,))
logger.info("✅ Удалены записи со статусом 'Выполнена'")

# Изменение приоритета
logger.info("🔄 Переходим к обработке изменений приоритета...")
sel_issuesPriority = "SELECT IssueID,email,Subj,Body,DateCreated,OldSubj,OldPriority,NewPriority,OldSubj,UserRedmine,NewStatus,Author,Assigned,mailbox_username FROM u_update_priority"  # выбираем заявки у которых поменялся приоритет
cursor.execute(sel_issuesPriority)
result = cursor.fetchall()
logger.info("📊 Найдено записей для обработки изменений приоритета: %d" % len(result))
for row in result:
    issueID = str(row[0])
    email = str(row[1])
    subj = str(row[2]) # Новая тема письма
    body = str(row[3])
    dateCreated=str(row[4])
    oldSubj=str(row[5])
    oldPriority=str(row[6])
    newPriority=str(row[7])
    title = str(row[8]) #OldSubj Изначальная тема письма
    userRedmine = row[9]  # Признак что юзер Редмайновский
    status = str(row[10])
    author = str(row[11])
    assigned = str(row[12])
    mailbox_username = str(row[13])
    priority = newPriority

    # Проверяем, следует ли отправлять email
    if not should_send_email(email):
        logging.info("Пропускаем отправку уведомления об изменении приоритета на %s - адрес исключен" % email)
        # Удаляем запись из базы, даже если не отправляем email
        del_issues_Priority = "DELETE FROM u_update_priority WHERE IssueID = %s"
        cursor.execute(del_issues_Priority, (issueID,))
        continue

    if userRedmine == 1:
        add_notes = ''
        emailMessage = f.template_html_Assigned(issueID, body, 'Пrioритет', oldPriority, newPriority, dateCreated, title, author, status, priority, assigned, add_notes) # + f.html_footer()
    else:
        emailMessage = f.template_html(issueID,body,'Приоритет',oldPriority,newPriority,dateCreated, author, status, priority, assigned) # + f.html_footer()

    del_issues_Priority = "DELETE FROM u_update_priority WHERE IssueID = %s"
    try:
        send_email(mailbox_username, email, emailMessage, subj) # отправляем почту
    except Exception as e:
        EmailNote = "Сбой отправки email на адрес %s: %s" % (email, str(e))
        logging.error(EmailNote)
    finally:
        cursor.execute(del_issues_Priority, (issueID,))

# Изменение Даты выполнения
logger.info("🔄 Переходим к обработке изменений даты выполнения...")
sel_issuesDue_Date = "SELECT IssueID, email,Subj,Body,OldDueDate,NewDueDate,DateCreated,OldSubj,UserRedmine,Author,Assigned,NewStatus,Priority,mailbox_username FROM u_update_due_date"  # выбираем заявки у которых поменялся приоритет
cursor.execute(sel_issuesDue_Date)
result = cursor.fetchall()
logger.info("📊 Найдено записей для обработки изменений даты выполнения: %d" % len(result))
for row in result:
    issueID = str(row[0])
    email = str(row[1])
    subj = str(row[2]) # Новая тема письма
    body = str(row[3])
    oldDueDate = str(row[4])
    newDueDate = str(row[5])
    dateCreated = str(row[6])
    title = str(row[7])# OldSubj Изначальная тема письма
    userRedmine = row[8]  # Признак что юзер Редмайновский
    author = str(row[9])
    assigned = str(row[10])
    status = str(row[11])
    priority = str(row[12])
    mailbox_username = str(row[13])

    # Проверяем, следует ли отправлять email
    if not should_send_email(email):
        logging.info("Пропускаем отправку уведомления об изменении даты выполнения на %s - адрес исключен" % email)
        # Удаляем запись из базы, даже если не отправляем email
        del_issues_Due_Date = "DELETE FROM u_update_due_date WHERE IssueID = %s"
        cursor.execute(del_issues_Due_Date, (issueID,))
        continue

    if len(oldDueDate) <= 0: oldDueDate='""'
    if oldDueDate <= '2016-01-01': oldDueDate='None'
    if userRedmine == 1:
        add_notes = ''
        emailMessage = f.template_html_Assigned(issueID, body, 'Дата выполнения', oldDueDate, newDueDate, dateCreated, title, author, status, priority, assigned, add_notes)  # + f.html_footer()
    else:
        emailMessage = f.template_html(issueID,body,'Дата выполнения',oldDueDate,newDueDate,dateCreated, author, status, priority, assigned) + f.html_footer()

    del_issues_Due_Date = "DELETE FROM u_update_due_date WHERE IssueID = %s"
    try:
        send_email(mailbox_username, email, emailMessage, subj) # отправляем почту
    except Exception as e:
        EmailNote = "Сбой отправки email на адрес %s: %s" % (email, str(e))
        logging.error(EmailNote)
    finally:
        cursor.execute(del_issues_Due_Date, (issueID,))

# Изменение Исполнителя задачи
logger.info("🔄 Переходим к обработке изменений исполнителя...")
sel_issues_Assigned = "SELECT IssueID, email,Subj,Body, IFNULL (OldAssigned,'None') AS OldAssigned,NewAssigned,DateCreated,OldSubj,Author,Status,Priority,mailbox_username FROM u_update_assigned"  # выбираем заявки у которых поменялся испонитель
cursor.execute(sel_issues_Assigned)
result = cursor.fetchall()
logger.info("📊 Найдено записей для обработки изменений исполнителя: %d" % len(result))
for row in result:
    issueID = str(row[0])
    email = str(row[1])
    # email =  "y.varslavan@tez-tour.com"
    subj = str(row[2]) # Новая тема письма
    body = str(row[3])
    oldAssigned = str(row[4])
    newAssigned = str(row[5])
    dateCreated = str(row[6])
    title = str(row[7])# OldSubj Изначальная тема письма
    author = str(row[8])
    status = str(row[9])
    priority = str(row[10])
    mailbox_username = str(row[11])
    if len(oldAssigned) <= 0: oldAssigned='""'
    add_notes = ''

    # Проверяем, следует ли отправлять email
    if not should_send_email(email):
        logging.info("Пропускаем отправку уведомления об изменении исполнителя на %s - адрес исключен" % email)
        # Удаляем запись из базы, даже если не отправляем email
        del_issues_Assigned = "DELETE FROM u_update_assigned WHERE IssueID = %s"
        cursor.execute(del_issues_Assigned, (issueID,))
        continue

    # Проверяем домен почты (Костыль для Вильнюса, заказчик Санников Евгений)
    if DOMAIN_VILNIUS in email:
        emailMessage = f.template_html_Assigned_vln(issueID, body, 'Исполнитель', oldAssigned, newAssigned, dateCreated, title, author, status, priority, newAssigned, add_notes)
    else:
        emailMessage = f.template_html_Assigned(issueID,body,'Исполнитель',oldAssigned,newAssigned,dateCreated,title, author, status, priority, newAssigned, add_notes)  # + f.html_footer()
        # Генерируем новый шаблон для тестирования (только для обычных доменов)
        # emailMessageNew = f.template_html_Assigned_new(issueID, body, 'Исполнитель', oldAssigned, newAssigned, dateCreated, title, author, status, priority, newAssigned, add_notes)

    del_issues_Assigned = "DELETE FROM u_update_assigned WHERE IssueID = %s"

    try:
        # Отправляем обычное письмо получателю
        send_email(mailbox_username, email, emailMessage, subj)

        # Отправляем новый шаблон на тестовый адрес только для обычных доменов
        #if "@teztour.lt" not in email:
        #   test_subject = "[ТЕСТ НОВОГО ШАБЛОНА] {}".format(subj)
        #   send_email(mailbox_username, "y.varslavan@tez-tour.com", emailMessageNew, test_subject)

    except Exception as e:
        EmailNote = "Сбой отправки email на адрес %s: %s" % (email, str(e))
        logging.error(EmailNote)
    finally:
        cursor.execute(del_issues_Assigned, (issueID,))

# добавление примечания задачи (only users Anonymous)
logger.info("🔄 Переходим к обработке добавления примечаний...")
sel_issues_Notes = "SELECT issue_id, user_email, notes, date_created, project_id, mailbox_username, subject  FROM u_Add_Notes Where project_id NOT IN (198)"
cursor.execute(sel_issues_Notes)
result = cursor.fetchall()
logger.info("📊 Найдено записей для обработки добавления примечаний: %d" % len(result))

for row in result:
    issueID = str(row[0])
    email = str(row[1])
    #email =  "y.varslavan@tez-tour.com"
    notes = str(row[2])
    dateCreated = str(row[3])
    project_id= row[4]
    mailbox_username = str(row[5])
    subject =  str(row[6])
    subj = 'В задачу #' + issueID + ' добавлен комментарий ' + '(' + subject + ')'

    # Проверяем, следует ли отправлять email
    if not should_send_email(email):
        logging.info("Пропускаем отправку уведомления о добавлении примечания на %s - адрес исключен" % email)
        # Удаляем запись из базы, даже если не отправляем email
        del_AddNotes = "DELETE FROM u_Add_Notes WHERE issue_id = %s"
        cursor.execute(del_AddNotes, (issueID,))
        continue

    if project_id in PROJECT_UFA:  # Входящие для Уфы (проекты Расчет заявок, Ценовые предложения)
        emailMessage = f.template_html_AddNotes_Ufa (issueID, notes) + f.html_footer()
    else:
        emailMessage = f.template_html_AddNotes (issueID, notes) # + f.html_footer()
    del_AddNotes = "DELETE FROM u_Add_Notes WHERE issue_id = %s"
    try:
        send_email(mailbox_username, email, emailMessage, subj) # отправляем  почту
    except Exception as e:
        EmailNote = "Сбой отправки email на адрес %s: %s" % (email, str(e))
        logging.error(EmailNote)
    finally:
        cursor.execute(del_AddNotes, (issueID,))
logger.info("🔄 Завершаем работу с базой данных...")
try:
    cnx.commit()
    logger.info("✅ Изменения в базе данных сохранены")
    cursor.close()
    cnx.close()
    logger.info("✅ Соединение с базой данных закрыто")
except Exception as e:
    logger.warning("⚠️ Ошибка при закрытии соединения: %s" % str(e))
finally:
    logger.info("=" * 60)
    logger.info("✅ NOTIFIC.PY ЗАВЕРШЕН УСПЕШНО")
    logger.info("⏰ Время завершения: %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    logger.info("=" * 60)
    sys.exit(0)
