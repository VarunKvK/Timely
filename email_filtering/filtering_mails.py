import imaplib as im
import email
import os 
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def read_email_list_to_monitor(email_csv):
    email=pd.read_csv(email_csv)
    email_list=email.Email.tolist()
    return email_list

def retrieve_emails(emails):
    try:
        mail=im.IMAP4_SSL('imap.gmail.com')
        mail.login(os.getenv('EMAIL_SECONDARY'),os.getenv('PASSWORD_SECONDARY'))
        
        mail.select('inbox')
        # print(emails)
        for mails in emails:
            try:
                print(mails)
                result,data=mail.search(None,"FROM",mails)
                if result=="OK":
                    print(result,data)
                    for num in data[0].split():
                        result, email_data= mail.fetch(num,'(RFC822')
                        raw_msg=email_data[0][1]
                        msg=email.message_from_bytes(raw_msg)
                        sender=msg["From"]
                        print(sender)
            except Exception as e:
                print(f"The particular {mails} doesn't exists so skipping it and continue .....")
                continue                                            
                     
    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the connection
        mail.close()
        mail.logout()
    