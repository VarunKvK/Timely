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

# def email_sent(email_csv,status):
#     try:
#         email=pd.read_csv(email_csv)
#         for mail,status in status:
#             email.loc[email.Email==mail,'STATUS=']=status
#         email.to_csv(email_csv,index=False)    
#     except Exception as e:
#         print("An error occurred:", e)



def prompt_number_of_mails():
    try:
        count=int(input("Enter the number of emails you want to send(Maximum is 100)? \n\n"))
        return count
    except Exception as e:
        print("An error occurred:", e)
        


def validate_email_file(email_folder,email_type):
    try:
        folder=""
        if email_type.lower() in [follow.lower() for follow in follow_up_words]:
            folder="FollowUp"
        elif email_type.lower() in [email.lower() for email in email_client_words]:
            folder="FreshEmail"
        elif email_type.lower() in [thank.lower() for thank in thank_you_email_words]:
            folder="ThanksMail"
        else:
            print("Invalid email type")
        
        email_file=input("Enter the filename of the email: \n\n").capitalize()
        if not email_file.endswith(".txt"):
            email_file+= ".txt"
            file_destination=f"{folder}/{email_folder}/{email_file}"
            # print(file_destination)
            print(folder)
            # print(os.getenv("DIRECTORY"))
        email=os.path.join(os.getenv("DIRECTORY"),file_destination)
        return email
    except Exception as e:
        print("An error occurred:", e)




def parse_email_file(email_file):
    print(email_file)
    with open(email_file, "r") as file:
        email=file.read()
        subject, _, message=email.partition("\n\n")
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
        subject=sub.split(": ",1)[1]
        status_list=[]
        for mail in email_list:
            try:
                msg=MIMEMultipart()
                msg['From']=os.getenv("EMAIL_SECONDARY")
                msg['To']=mail
                msg['Subject']=subject
                msg.attach(MIMEText(body, 'plain'))
            
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                    server.login(os.getenv("EMAIL_SECONDARY"),os.getenv("PASSWORD_SECONDARY"))
                    server.send_message(msg)
                # status_list.append((mail, "Sent"))
                print(f"Email sent to: {mail}")
            except Exception as e:
                # status_list.append((mail, "Failed"))
                print(f"Failed to send {mail}: {e}")
                continue
        return status_list
    except Exception as e:
        print("An error occurred:", e)