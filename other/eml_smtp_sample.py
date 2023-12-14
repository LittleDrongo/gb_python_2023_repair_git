import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def perform_calculation(argument):
    # Ваш код для выполнения расчетов
    result = ("А вот и аргумент" + " " + argument)
    return result

def send_email(to_address, subject, body):
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

    # Отправляем результат обратно
    sender_email = 'fomin.alexey@outlook.com'  # Замените на адрес отправителя
    send_email(sender_email, 'Calculation Result', f'The result is: {result}')

# Пример использования:
# if __name__ == "__main__":
    # Замените на свои настройки и адрес электронной почты
email_content = input("Введите аргумент: ")
process_email(email_content)