import os

db_user = os.getlogin()
db_password = os.environ.get('DB_PASS')

print(db_user)
print(db_password)
print("This is new line")
print("Test done")