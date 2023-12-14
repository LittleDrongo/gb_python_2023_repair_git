import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def perform_calculation(argument):
    # Ваш код для выполнения расчетов
    result = ("А вот и аргумент" + " " + argument)
    return result

def send_email(to_address, subject, body, attachment_path=None):
    # Ваши настройки для отправки электронного письма
    smtp_server = 'smtp.mail.ru'
    smtp_port = 587
    smtp_username = 'python_pars'
    smtp_password = 'tLSHqB1uBe2F3u5Q5xGc'
    from_address = 'python_pars@mail.ru'

    # Создание объекта MIMEMultipart
    message = MIMEMultipart()
    message['From'] = from_address
    message['To'] = to_address
    message['Subject'] = subject

    # Добавление текста в тело письма
    message.attach(MIMEText(body, 'plain'))

    # Добавление вложения, если указан путь к файлу
    if attachment_path:
        attachment = open(attachment_path, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % attachment_path)
        message.attach(part)

    # Создание объекта SMTP и отправка письма
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_address, to_address, message.as_string())

def process_email(email_content):
    # Извлекаем аргумент из содержимого электронного письма
    argument = email_content

    # Выполняем расчеты
    result = perform_calculation(argument)

    # Отправляем результат обратно с вложением (замените на путь к вашему файлу)
    attachment_path = '/eml_test.csv'
    sender_email = 'fomin.alexey@outlook.com'  # Замените на адрес отправителя
    send_email(sender_email, 'Calculation Result', f'The result is: {result}', attachment_path)

# Пример использования:
# if __name__ == "__main__":
    # Замените на свои настройки и адрес электронной почты
email_content = input("Введите аргумент: ")
process_email(email_content)
