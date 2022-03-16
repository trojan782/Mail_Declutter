import email
import imaplib
import getpass
from itertools import count


# Your Email should be the username e.g johndoe@gmail.com
username = 'kajaobinna@gmail.com'

password = getpass.getpass("Enter your password: ")

mail = imaplib.IMAP4_SSL('imap.gmail.com')

print("Logging you in...")
try:
    mail.login(username, password)
except Exception as e:
    print(e)
    
print("Login Successful")
print("Declutering Staring...")
mail.select('INBOX')

# To delete all mails from a particular sender input the desired Email below
results, messages = mail.search(None, '(FROM "alert@indeed.com")')

messages = messages[0].split()

count = 0
for msg in messages:
    result, message = mail.store(msg, '+X-GM-LABELS', '\\Trash')
    count += 1
    print("Deleting... {}").format(msg)
print("Operation Completed!")
print('{} mails deleted!').format(count)
mail.close()
mail.logout()

