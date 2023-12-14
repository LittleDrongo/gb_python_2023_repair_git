from read_email import *
from auth_data import *

email_address = imap_params['email_address']
imap_password = imap_params['imap_password']

unread_emails = get_unread_emails(email_address, imap_password=imap_password)

# Вывод списка непрочитанных писем

for email_info in unread_emails:
    print(f"Входящее: {email_info['Name']} <{email_info['Email']}> | {email_info['Subject']}")
    print(f"{email_info['Body']}")
    print("—"*100)
    email_body_strs = email_info['Body']
    file_list = email_body_strs.split()
    
    for file in file_list:
        print(file)
