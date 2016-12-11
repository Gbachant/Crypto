def get_initials():
    """Given a person's name, return the person's initials (uppercase) """
    fullname = input("What is your full name?")
    initials = ""
    split_name = fullname.split()
    for i in split_name:
        initials += i[0].upper()
    print(initials)
    return initials
