def email_validaion(email):
    if '@' in email and '.' in email:
        username , domain = email.split('@')
        if username and domain :
            try:
                z,y = domain.split('.')
                if z and y:
                    return True
            except ValueError :
                print('too many values to unpack')
    else:
        return False

email = input("enter ur email: ")


for i in range(6):
        email = input("enter ur email: ")
        if email_validaion(email):
             break
        print("tr again ")
else:
        raise Exception("Try again later.")
