list = [{"name": "omar", "password": "123"}, {"name": "ali", "password": "444"}]


def Check(name):
    for i in list:
        if name == i["name"]:
            password = input("enter ur pass: ")
            if password == i["password"]:
                print("welcome !")
                break
        else:
            continue
    else:
        print("email or password not found")
        exit()
