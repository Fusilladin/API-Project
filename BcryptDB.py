### Hashing DB Credentials

import bcrypt

### transform into bytes type
drvr = "{SQL Server Native Client 11.0}"
srvr = "127.0.0.1"
db = "BOOKSTORE"
user = "Azure1"
pw = "Pass1"

# hash the credentials
hashed_drvr = bcrypt.hashpw(drvr, bcrypt.gensalt())
hashed_srvr = bcrypt.hashpw(srvr, bcrypt.gensalt())
hashed_db = bcrypt.hashpw(db, bcrypt.gensalt())
hashed_user = bcrypt.hashpw(user, bcrypt.gensalt())
hashed_pw = bcrypt.hashpw(pw, bcrypt.gensalt())

# print hashed credentials to test they're correct
print(hashed_drvr)
print(hashed_srvr)
print(hashed_db)
print(hashed_user)
print(hashed_pw)






#
