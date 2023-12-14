import imaplib
import email
from email.header import decode_header
import quopri

def decode_subject(encoded_subject):
    """Decode email subject."""
    headers = decode_header(encoded_subject)
    return " ".join([text if isinstance(text, str) else text.decode(encoding or 'utf-8', errors='ignore') for text, encoding in headers])

def decode_sender(sender):
    """Decode email sender."""
    try:
        decoded_sender, encoding = decode_header(sender)[0]
        if isinstance(decoded_sender, bytes):
            return decoded_sender.decode(encoding or 'utf-8', errors='ignore')
        elif isinstance(decoded_sender, str):
            return decoded_sender
    except Exception as e:
        print(f"Error decoding sender: {e}")
        return sender

def decode_body(body, content_type):
    """Decode email body."""
    if content_type == "text/plain":
        return body.decode('utf-8')
    elif content_type == "text/html":
        try:
            import html2text
            return html2text.html2text(body.decode('utf-8'))
        except ImportError:
            print("To decode HTML, install 'html2text' module: pip install html2text")
            return body.decode('utf-8')
    else:
        # Handle other content types as needed
        return body.decode('utf-8')

def fetch_email_content(email_id, mail):
    """Fetch and print email content."""
    result, data = mail.fetch(email_id, '(RFC822)')
    if result == 'OK':
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)
        subject = decode_subject(msg["Subject"])
        sender = decode_sender(msg.get("From"))
        print(f"Subject: {subject}")
        print(f"From: {sender}")
        print("Body:")
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain" or content_type == "text/html":
                    print(decode_body(part.get_payload(decode=True), content_type))
        else:
            content_type = msg.get_content_type()
            print(decode_body(msg.get_payload(decode=True), content_type))
        print("=" * 30)

def check_emails():
    EMAIL = 'python_pars@mail.ru'
    PASSWORD = '86mvydGEVbRCQAJNsunv'
    IMAP_SERVER = 'imap.mail.ru'
    
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)
    
    mail.select("inbox")
    
    result, data = mail.search(None, "ALL")
    if result == 'OK':
        email_ids = data[0].split()
        for email_id in email_ids:
            fetch_email_content(email_id, mail)
    
    mail.close()
    mail.logout()

# if __name__ == "__main__":
check_emails()