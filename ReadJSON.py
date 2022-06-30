import json

# read file

myjsonfile = open('employee.json', 'r')
jsondata = myjsonfile.read()
# print(jsondata)

# Parse
obj = json.loads(jsondata)

print(str(obj['firstName']))
# print(driver)
print(str(obj['lastName']))

list = obj['address']
print(list)
# print(list[0])
# print(list[1])
# print(len(list))

for i in range(len(list)):
    print("Address of", i, ("is........"))
    print("Street:", list[i].get("street"))
    print("City:", list[i].get("city"))
    print("State:", list[i].get("state"))











#
