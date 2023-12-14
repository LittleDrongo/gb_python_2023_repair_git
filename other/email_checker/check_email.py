import imaplib
import email
from email.header import decode_header
import re

def get_unread_emails(email_address, folder='INBOX', imap_server='imap.mail.ru', imap_port=993, imap_password='None'):
    # Подключение к серверу IMAP
    mail = imaplib.IMAP4_SSL(imap_server, imap_port)
    mail.login(email_address, imap_password)

    # Выбор папки
    mail.select(folder)

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
        
        # Используем регулярное выражение для поиска email-адреса
        match = re.search(r'<([^>]+)>', from_full)
        from_email = None

        if match:
            from_email = match.group(1)
        else:
            from_email = None

        # Добавление информации о письме в список
        unread_emails.append({
            'Subject': subject,
            'From': from_full,
            'Name': from_name,
            'Email' : from_email
        })

    # Закрытие соединения
    mail.close()
    mail.logout()
    return unread_emails

# Пример использования:
email_address = 'python_pars@mail.ru'
imap_password = 'tLSHqB1uBe2F3u5Q5xGc'
unread_emails = get_unread_emails(email_address, imap_password=imap_password)

# Вывод списка непрочитанных писем
for email_info in unread_emails:
    print(f"Входящее: {email_info['Name']} <{email_info['Email']}> | {email_info['Subject']}")