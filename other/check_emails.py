import imaplib
import email
from email.header import decode_header

# python_pars@mail.ru
# abrakadabra5221696
# 86mvydGEVbRCQAJNsunv

def decode_subject(encoded_subject):
    """Decode email subject."""
    headers = decode_header(encoded_subject)
    return " ".join([text if isinstance(text, str) else text.decode(encoding or 'utf-8', errors='ignore') for text, encoding in headers])

def fetch_email_content(email_id, mail):
    """Fetch and print email content."""
    result, data = mail.fetch(email_id, '(RFC822)')
    if result == 'OK':
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)
        subject = decode_subject(msg["Subject"])
        sender = msg.get("From")
        print(f"Subject: {subject}")
        print(f"From: {sender}")
        print("Body:")
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    print(part.get_payload(decode=True).decode('utf-8'))
        else:
            print(msg.get_payload(decode=True).decode('utf-8'))
        print("=" * 30)

def check_emails():
    # Параметры для подключения к почтовому ящику
    EMAIL = 'python_pars@mail.ru'
    # PASSWORD = 'abrakadabra5221696'
    PASSWORD = '86mvydGEVbRCQAJNsunv'
    IMAP_SERVER = 'imap.mail.ru'
    
    # Подключение к серверу по протоколу IMAP
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)
    
    # Выбор почтового ящика (inbox)
    mail.select("inbox")
    
    # Поиск всех писем в ящике
    result, data = mail.search(None, "ALL")
    if result == 'OK':
        email_ids = data[0].split()
        for email_id in email_ids:
            fetch_email_content(email_id, mail)
    
    # Закрытие соединения
    mail.close()
    mail.logout()

# if __name__ == "__main__":
check_emails()
