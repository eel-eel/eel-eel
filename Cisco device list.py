network_devices = ["Cisco Catalyst 9300", "Juniper Switch", "Extreme Networks swizzle", "Cisco Catalyst 2960x"]
newlist = []

for x in network_devices:
    if "Juni" in x:
        newlist.append(x)

print(newlist)