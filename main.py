from email_filtering import filtering_mails
def main():
    csvfile="./emails/email_monitoring.csv"
    # sender_email=input("Enter the email address to monitor: ")
    emails=filtering_mails.read_email_list_to_monitor(email_csv=csvfile)
    filtering_mails.retrieve_emails(emails)
    
if __name__ == "__main__":
    main()