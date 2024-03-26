import pandas as pd
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
from email_keywords.keyword_list import follow_up_words,email_client_words,thank_you_email_words


load_dotenv()

def read_email_list_to_monitor(email_csv):
    email_csv=pd.read_csv(email_csv)
    email_list=email_csv.Email.tolist()
    return email_list

def validate_email_file(email_folder,email_type):
    try:
        if email_type in follow_up_words:
            folder="FollowUp"
        elif email_type in email_client_words:
            folder="FreshEmail"
        elif email_type in thank_you_email_words:
            folder="ThanksMail"
        
        email_file=input("Enter the filename of the email: ").capitalize()
        if not email_file.endswith(".txt"):
            email_file+= ".txt"
            file_destination=f"{folder}/{email_folder}/{email_file}"
        email=os.path.join(os.getenv("DIRECTORY"),file_destination)
        return email
    except Exception as e:
        print("An error occurred:", e)


def parse_email_file(email_file):
    try:
        with open(email_file, "r") as file:
            email=file.read()
            subject, _, message=email.partition("\n\n")
    except Exception as e:
        print("An error occurred:", e)
    return subject, message
 


def select_email_template(subject,message,email_type,followup,new_email,thank_email):
    try:
        if email_type.lower() in [follow.lower() for follow in followup]:
            sub=subject
            body=message
            print("Email follow up is on the go")
        elif email_type.lower() in [mails.lower() for mails in new_email]:
            sub=subject
            body=message
            print("Email up is on the go")
        elif email_type.lower() in [thanks.lower() for thanks in thank_email]:
            sub=subject
            body=message
            print("Email thanks up is on the go")
    except Exception as e:
        print("An error occurred:", e)
    
    return sub,body


def send_email_to_list(email_list,sub,body):
    try:
        for mail in email_list:
            msg=MIMEMultipart()
            msg['From']=os.getenv("EMAIL_SECONDARY")
    except Exception as e:
        print("An error occurred:", e)