from read_email import *
from auth_data import *
from send_email import *
from exctractor import *

# Вывод списка непрочитанных писем
def get_list_to_search():
    unread_emails = get_unread_emails(imap_params)
    for email_info in unread_emails:
        print(f"Входящее: {email_info['Name']} <{email_info['Email']}> | {email_info['Subject']}")
        print(f"{email_info['Body']}")
        print("—"*100)
        email_body_strs = email_info['Body']
        file_list = email_body_strs.split()        

        subj = email_info['Subject']

        if subj == auth_subj:

            files_pathes = search_zips(default_start_directory, file_list, default_output_directory)
            files_to_attach = []        
            for i in files_pathes:
                for j in i:
                    files_to_attach.append(j)
            send_to = email_info['Email']
            send_email(send_to, email_body_strs, (f'Результат поиска файлов {subj} {send_to}'), files_to_attach)