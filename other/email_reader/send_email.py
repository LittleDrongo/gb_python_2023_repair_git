import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from auth_data import *
import os

def send_email(to_address, body, subject, attachments, params=smtp_params):
    
    smtp_server = params['smtp_server']
    smtp_port = params['smtp_port']
    smtp_username = params['smtp_username']
    smtp_password = params['smtp_password']
    from_address = params['from_address']

    # Создание объекта MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Добавление текста сообщения
    msg.attach(MIMEText(body, 'plain'))

    # Добавление вложений
    for attachment in attachments:
        # Получение только названия файла без пути
        filename = os.path.basename(attachment)
        with open(attachment, 'rb') as file:
            part = MIMEApplication(file.read(), Name=filename)
            part['Content-Disposition'] = f'attachment; filename="{filename}"'
            msg.attach(part)

    # Установка соединения с SMTP-сервером и отправка письма
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_address, to_address, msg.as_string())

# Пример использования

"""

smtp_params = {'smtp_server': 'smtp.mail.ru',
              'smtp_port': 587,
              'smtp_username': 'python_pars',
              'smtp_password': 'tLSHqB1uBe2F3u5Q5xGc',
              'from_address' : 'python_pars@mail.ru'
              }

to_address = 'fomin.alexey@outlook.com'
body = 'Привет, это тестовое сообщение.'
subject = 'Тестовое письмо с вложениями'
attachments = ['eml_test.csv', 'eml_test copy.csv']

send_email(to_address, body, subject, attachments, smtp_params)


"""