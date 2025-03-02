import os

email_user = os.environ.get('EMAIL_USER')
email_pass = os.environ.get('EMAIL_PASS')

print(email_user)
print(email_pass)

#db_password = os.environ.get('DB_PASS')