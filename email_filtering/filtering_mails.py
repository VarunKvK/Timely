import imaplib as im
import email
import os 
import csv
from dotenv import load_dotenv

load_dotenv()

email_list = []
def read_email_list_to_monitor(email_csv):
    with open(email_csv, "r") as email:
        reader=csv.reader(email)
        for row in reader:
            email_list.append(row)
    return(email_list)

def retrieve_emails():
    try:
        mail=im.IMAP4_SSL('imap.gmail.com')
        mail.login(os.getenv('EMAIL_SECONDARY'),os.getenv('PASSWORD_SECONDARY'))
        
        mail.select('inbox')
        
        for mails in email_list:
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
                     
    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the connection
        mail.close()
        mail.logout()