def validate(email):
    if "@" in email and "." in email:
        username, domain = email.split("@")
        if username and domain:
            try:
                z, y = domain.split(".")
                if z and y:
                    return True
            except ValueError:
                print("too many values to unpack")
                exit()
    else:
        return False
