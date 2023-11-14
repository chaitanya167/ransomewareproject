import smtplib
from email.mime.text import MIMEText

# Define email parameters
sender_email = 'chaitanyar1692@gmail.com'  # Use a spoofed sender address
recipient_email = 'chaitanyar169@gmail.com'  # Target recipient
subject = 'Congratulations You Won Lottery in Walmart!'
body = 'WALMART LUCKY WINNER \nCONGRATULATIONS!! \nYour Email was selected in WALMART Lucky Draw and won the Iphohe and AppleWatch. Kindly click on the link \nhttps://tinyurl.com/lotteery for claims.\nYours Sincerely \nMr. James Hodges Head Of Operations'

# Create the email message
message = MIMEText(body)
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = subject

# Send the email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login('chaitanyar1692@gmail.com', 'elgd wgkh qotd ncjp')
    server.sendmail(sender_email, recipient_email, message.as_string())
