import json
SystemInformation = {"OS": "NetSim", "Version": 13, "Owner": "Boson"}
with open('SystemInformation.json', 'w') as JsonFile:
     json.dump(SystemInformation, JsonFile)