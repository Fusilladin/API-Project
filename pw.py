

import requets
import pyodbc
import pandas as pd
import json
import bcrypt
import os

### Reading the JSON config file
# read filter
myjsonfile = open('config.json', 'r')
jsondata = myjsonfile.read()
# /// print(jsondata) # test

### Parsing Config JSON file
obj = json.loads(jsondata)
# drvr = bytes((obj['driver']), "ascii")
drvr = (obj['driver'])
srvr = (obj['server'])
db = (obj['database'])
user = (obj['username'])
pw = (obj['password'])


### Connecting to DB
conn = pyodbc.connect("DRIVER=" + drvr
                      + ";SERVER=" + srvr
                      + ";DATABASE=" + db
                       + ";UID=" + user
                       + ";PWD=" + pw
)
# Querying the database
cursor = conn.cursor()
sql_query=pd.read_sql_query('SELECT * FROM [BOOKSTORE].[dbo].[BOOK]', conn)
sql_query.to_csv('all_data.csv', index=False)
print(sql_query)
