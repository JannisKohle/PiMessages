import os
import sys

args = sys.argv[1:]

usage = "Type 'pimessages help' for usage"

if args[0] == "signup":
    args = args[1:]

    if len(args) == 0:  # no more args
        username = input("Username: ")
        password = input("Password: ")

    elif len(args) == 2:
        if args[0] in ["-un", "--username"]:
            username = args[1]
            password = input("Password: ")

        elif args[0] in ["-pw", "--password"]:
            password = args[1]
            username = input("Username: ")

        else:
            print(usage)

    elif len(args) == 4:
        if args[0] in ["-un", "--username"]:
            if args[2] in ["-pw", "--password"]:
                username = args[1]
                password = args[3]

            else:
                print(usage)

        elif args[0] in ["-pw", "--password"]:
            if args[2] in ["-un", "--username"]:
                username = args[3]
                password = args[1]

            else:
                print(usage)
        else:
            print(usage)
    else:
        print(usage)

elif args[0] == "login":
    args = args[1:]

    if len(args) == 0:  # no more args
        username = input("Username: ")
        password = input("Password: ")

    elif len(args) == 2:
        if args[0] in ["-un", "--username"]:
            username = args[1]
            password = input("Password: ")

        elif args[0] in ["-pw", "--password"]:
            password = args[1]
            username = input("Username: ")

        else:
            print(usage)

    elif len(args) == 4:
        if args[0] in ["-un", "--username"]:
            if args[2] in ["-pw", "--password"]:
                username = args[1]
                password = args[3]

            else:
                print(usage)

        elif args[0] in ["-pw", "--password"]:
            if args[2] in ["-un", "--username"]:
                username = args[3]
                password = args[1]

            else:
                print(usage)
        else:
            print(usage)
    else:
        print(usage)

elif args[0] == "send":
    args = args[1:]

    if len(args) == 1:
        message = input("Message: ")

    elif len(args) == 3:
        if args[1] == "-m" or args[1] == "--message":
            pass
        else:
            print(usage)
    else:
        print(usage)

elif args[0] == "chat":
    pass
elif args[0] == "ignore":
    pass
elif args[0] == "unignore":
    pass
elif args[0] == "inbox":
    pass
elif args[0] == "account-info":
    pass
elif args[0] == "pw" or args[0] == "password":
    pass
elif args[0] == "help" or args[0] == "info":
    pass
