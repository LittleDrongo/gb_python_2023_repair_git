import imaplib
import email
from email.header import decode_header
import re
from auth_data import *


def get_unread_emails(params):

    imap_server = params['imap_server']
    imap_password = params['imap_password']
    imap_port = params['imap_port']
    imap_folder = params['imap_folder']
    email_address = params['email_address']

    # Подключение к серверу IMAP
    mail = imaplib.IMAP4_SSL(imap_server, imap_port)
    mail.login(email_address, imap_password)

    # Выбор папки
    mail.select(imap_folder)

    # Поиск непрочитанных писем
    status, messages = mail.search(None, '(UNSEEN)')
    if status == 'OK':
        unread_message_nums = messages[0].split()
    else:
        print(f"Не удалось получить список непрочитанных писем. Статус: {status}")
        return []

    # Получение информации о каждом непрочитанном письме
    unread_emails = []
    for num in unread_message_nums:
        _, msg_data = mail.fetch(num, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])
        
        # Получение темы письма
        subject, encoding = decode_header(msg.get('Subject'))[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding or 'utf-8')

        # Получение отправителя
        from_name, from_encoding = decode_header(msg.get('From'))[0]
        if isinstance(from_name, bytes):
            from_name = from_name.decode(from_encoding or 'utf-8')

        from_full = msg.get('From')
        
        # Используем регулярное выражение для поиска email-адреса в переменной from_full
        match = re.search(r'<([^>]+)>', from_full)
        from_email = None

        if match:
            from_email = match.group(1)
        else:
            from_email = None

        # Декодирование тела письма
        body = None
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True).decode(part.get_content_charset() or 'utf-8', errors='replace')
                break

        # Добавление информации о письме в список
        unread_emails.append({
            'Subject': subject,
            'From': from_full,
            'Name': from_name,
            'Email' : from_email,
            'Body': body
        })

    # Закрытие соединения
    mail.close()
    mail.logout()
    return unread_emails

# Пример использования:

"""
unread_emails = get_unread_emails(imap_params)


# Вывод списка непрочитанных писем

for email_info in unread_emails:
    print(f"Входящее: {email_info['Name']} <{email_info['Email']}> | {email_info['Subject']}")
    print(f"{email_info['Body']}")
    print("—"*100)
    email_body_strs = email_info['Body']
    file_list = email_body_strs.split()
    
    for file in file_list:
        print(file)
"""