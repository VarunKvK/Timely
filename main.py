from email_filtering import filtering_mails
def main():
    email="./emails/email_monitoring copy.csv"
    email_list=filtering_mails.read_email_list_to_monitor(email)
    filtering_mails.retrieve_emails(email_list)
    
if __name__ == "__main__":
    main()