import json

filename = "name.json"

with open(filename, "r") as showname:
	content = json.load(showname)

print(content)

