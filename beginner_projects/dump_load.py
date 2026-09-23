import json

name = input("Enter your name: ")

filename = "name.json"

with open(filename, "w") as nameobject:
	json.dump(name, nameobject)

