f = open("dataStorage.py", "w")
f.write("email = \"" + input("bestbuy email: ") + "\"\npassword = '" + input("bestbuy password: ") + "'\ndiscordId = " + input("discord id: (go into settings->advanced->enable developer mode, then right click your name anywhere you've sent a message and copy id):"))
##cookies = input("cookies: ")
##toSave = []
##while len(cookies) > 0:
##    try:
##        toSave.append({"name":cookies[:cookies.index("=")], "value": cookies[cookies.index("=") + 1: cookies.index(";")]})
##        cookies = cookies[cookies.index(";") + 2:]
##    except:
##        toSave.append({"name":cookies[:cookies.index("=")], "value": cookies[cookies.index("=") + 1:]})
##        break       
##print(toSave)
##f.write("\ncookies= " + str(toSave))
f.close()
print("setup complete. run \"run.cmd\" to start the program")
