import os

# Password Keeper

admin_password = "zxc"

try:
    f = open("password.txt", "x")
except:
    pass

finish = False

def _help():
    print()
    print("Type \"help\" to show this message.")
    print("Type \"read\" to show every password kept by keypussy")
    print("Type \"reset\" to delete every password kept by keypussy")
    print("Type \"about\" for this project's lore. lol")
    print("Type \"quit\" or \"exit\" to exit this utility")
    print()
    print()

def _read():
    print()
    f = open("password.txt", "r")
    content_list = f.read().split()
    print(content_list)
    f.close()
    print()

def _process():
    f = open("password.txt", "a")
    email = str(input("What is your email/username: "))
    password = str(input("password to keep: "))
    f.write(email + " " + password + " ")
    f.close()
    print()

def _reset():
    f = open("password.txt", "w")
    f.close()

def _about():
    print()
    os.system('figlet keypussy')
    print()
    print("A password keeping utility made by an idiot like me as a hobby project.")
    print("The password is kept locally in host's machine.")
    print("I create this project to learn about writing files in using Python and os modules.")
    print()
    print()
    print("Made with love by Andrian Harry, Johnny Sins's best apprentice")
    print()
    print()

print("Hello Babi")
user_pass = str(input("Enter your passwordlah, sial!: "))

if user_pass == admin_password:
    while not finish:
        print("What do you want to do, my fellow cum dumpster?:   ")
        a = str(input(":"))
        if a == "read":
            _read()
        if a == "write":
            _process()
        if a == "quit" or a == "exit":
            finish = True
        if a == "reset":
            _reset()
        if a == "help":
            _help()
        if a == "about":
            _about()
else:
    print("Babi, kalau bukan boss jgn sibuklah cibai!")
    print("Blah kau! 🖕")

