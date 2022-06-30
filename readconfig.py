### Read config file

import json

# read filter
myjsonfile = open('config.json', 'r')
jsondata = myjsonfile.read()
# print(jsondata)

# Parse
obj = json.loads(jsondata)

drvr = (str(obj['driver']))
srvr = (str(obj['server']))
db = (str(obj['database']))
user = (str(obj['username']))
pw = (str(obj['password']))

print(drvr)
print(srvr)
print(db)
print(user)
print(pw)
