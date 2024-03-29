from email_filtering import filtering_mails
from email_sender import send_emails,personalization
from email_keywords.keyword_list import follow_up_words,email_client_words,thank_you_email_words,send_keywords,filter_keywords
def main():
#CSV File
    csvfile="./emails/email_monitoring.csv"
    
    automate_task=input("What task do you want to automate?\n 1) Filter Emails through an csv file 2) Send emails to clients \n Output: \n\n")
    
    
    
    if automate_task.lower() in [filter.lower() for filter in filter_keywords]:
###################################### Filtering Emails ###########################################

#Optional to send a specific email adress
#sender_email=input("Enter the email address to monitor: ")
        
#Filter function ndergoing as some of the emails are not getting rendered
        emails=filtering_mails.read_email_list_to_monitor(email_csv=csvfile)
        filtering_mails.retrieve_emails(emails)
    
#################################################################################################
    
    
####################################### Sending Emails ##########################################

    elif automate_task.lower() in [send.lower() for send in send_keywords]:
        
#This lets you select specific type of email you wwant to send
        email_type=input("Enter the email-type you want to send: \n\n")
        email_file=input("Enter the email genre/folder-name you want to send from email-template: \n\n").capitalize()
        
#Validate the file the user typed in
        validated_file=send_emails.validate_email_file(email_file,email_type)
        
        
#Seperate the email with subject and body
        subject,message=send_emails.parse_email_file(validated_file)
        
        
#This is where the email template is selected from the keyword you entered
        sub,body=send_emails.select_email_template(subject=subject,message=message,email_type=email_type,followup=follow_up_words,new_email=email_client_words,thank_email=thank_you_email_words)
        
        
        personal_template=personalization.read_template(validated_file)
        
        email_reciever_csv=personalization.get_username(username=csvfile)
        
        personal_message=personalization.personalize_email(template=personal_template,username=email_reciever_csv)
        
        
        
#This sends the email list by reading it and then traversing into the next function
        email_send_list=send_emails.read_email_list_to_monitor(email_csv=csvfile)
        
        num_recipients=send_emails.prompt_number_of_mails()
        
        if num_recipients is None:
                return
        
        selected_number=email_send_list[:num_recipients]

#The function which sends the mail to the address

        status=send_emails.send_email_to_list(selected_number,sub,personal_message)

        # send_emails.email_sent(status=status,email_csv=csvfile)

#################################################################################################

if __name__ == "__main__":
    main()