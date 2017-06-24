# This Code for python beginner
# Dictionary Test Code

# This Object is Dictionary
# Dictionary is consist of KEY and VALUE
services = {'ftp':21,'ssh':22,'smtp':25,'http':80}

# Use Dictionary default methods
print services.keys()
print services.items()
print services.has_key('ftp') # Return Bool value
print "[+] Found vuln with FTP on port " + str(services['ftp'])
