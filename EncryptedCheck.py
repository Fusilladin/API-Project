### Checking bcrypted imported credentials

import json
import bcrypt

myjsonfile = open('config.json', 'r')
jsondata = myjsonfile.read()
# print(jsondata)

obj = json.loads(jsondata)
drvr = bytes((obj['driver']), "ascii")
# print(drvr)

hashed = bcrypt.hashpw(b"$2b$12$U5eRuGTQS2uCyQftc3vLnOPEDjsyZXqSz.UBV9ymtpQ/pVeHtEQ7m", bcrypt.gensalt())
pw = drvr
# print(hashed)

if bcrypt.checkpw(pw, hashed):
    print("It matches!")
else:
    print("Does not match!")















#
