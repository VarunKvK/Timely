import os
import pandas as pd

def read_template(filename):
    with open(filename,'r') as file:
        return file.read()

def get_username(username):
    email_list=pd.read_csv(username)
    email_list["Username"]=email_list["Email"].apply(lambda email: extract_username(email))
    username_list=email_list.Username.to_list()
    return username_list

def extract_username(email):
    parts=email.split("@")
    if len(parts)==2:
        username=parts[0]
        username = ''.join(char for char in username if not char.isdigit())
        return username
    return None

def personalize_email(template,username):
    for user in username:
        personalize_email_template=template.replace("[Client's Name]",user.capitalize())
        sender_personalise_email=personalize_email_template.replace("[Your Name]",os.getenv("SENDER"))
    return sender_personalise_email