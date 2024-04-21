import imaplib as im
import email
import os 
<<<<<<< HEAD
import pandas as pd
=======
import csv
>>>>>>> master
from dotenv import load_dotenv

load_dotenv()

<<<<<<< HEAD
def read_email_list_to_monitor(email_csv):
    email=pd.read_csv(email_csv)
    email_list=email.Email.tolist()
    return email_list

def retrieve_emails(emails):
=======

def read_email_list_to_monitor(email_csv):
    with open(email_csv, "r") as email:
        email_list=[]
        reader=csv.reader(email)
        for row in reader:
            email_list.append(row)
    return email_list

def retrieve_emails(email_list):
>>>>>>> master
    try:
        mail = im.IMAP4_SSL('imap.gmail.com')
        mail.login(os.getenv('EMAIL_SECONDARY'), os.getenv('PASSWORD_SECONDARY'))
        
        mail.select('inbox')
        
<<<<<<< HEAD
        for email_address in emails:
            try:
                print(f"Searching for emails from: {email_address}")
                result, data = mail.search(None, "FROM", email_address)
                if result == "OK":
                    for num in data[0].split():
                        print(f"Fetching email with UID: {num}")
                        result, email_data = mail.fetch(num, '(RFC822)')
                        raw_msg = email_data[0][1]
                        msg = email.message_from_bytes(raw_msg)
                        sender = msg["From"]
                        if sender == email_address:
                            print(f"Found email from: {email_address}")
                            email_contents = []  # List to store the content of each email
                            if msg.is_multipart():
                                for msg_part in msg.walk():
                                    content_type = msg_part.get_content_type()
                                    if content_type == "text/plain" or content_type== "text/html":
                                        email_contents.append(msg_part.get_payload(decode=True).decode("utf-8"))
                            print("Email content:")
                            for content in email_contents:
                                print(content)
                            print()
                        else:
                            print(f"Failed to fetch email with UID: {num}")
                            
            except Exception as e:
                print(f"Error occurred while processing email from {email_address}: {e}")
                continue                                            
=======
        for mails in email_list:
            print(mails)
            result,data= mail.search(None,"FROM",mails)
            if result=="OK":
                for num in data[0].split():
                    result, email_data= mail.fetch(num,'(RFC822)')
                    
                    raw_email=email_data[0][1] 
                    msg = email.message_from_bytes(raw_email)  
                    sender=msg["From"]
                    if sender==mails:                    
                        if msg.is_multipart:
                            for msg_part in msg.walk():
                                content_type=msg_part.get_content_type()
                                if content_type=="text/plain" or content_type=="text/html":
                                    body+=msg_part.get_payload(decode=True).decode("utf-8")
                                    print(body)
                                else:
                                    body=msg_part.get_payload(decode=True).decode()
                                    print(body)
>>>>>>> master
                     
    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the connection
        mail.close()
<<<<<<< HEAD
        mail.logout()
=======
        mail.logout()
>>>>>>> master
