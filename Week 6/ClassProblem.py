def get_input():
    no_string = True
    while no_string:
        return_string = input("Please enter a string to check if it is a valid email address ")
        no_string = False
    return return_string

def parse_input(input_string):
    valid_username = True
    valid_extension = True
    username = ""
    websitename  = ""
    extension = ""
    user_index = input_string.find('@')
    if user_index == -1:
        valid_username = False
    else:
        username = input_string[0:user_index]
        ext_index = input_string.find(".")
        if ext_index == -1:
            valid_extension = False
        else:
            websitename = input_string[user_index+1:ext_index]
            extension = input_string[ext_index + 1:]
    return valid_username, valid_extension, username, websitename, extension

def validate_user(username):
    valid_user =  True
    if len(username) == 0:
        valid_user = False
    else:
        for x in username:
            if not x.isalnum() and x != '_' and x != '-':
                valid_user = False
    return valid_user

def validate_website(websitename):
    valid_website = True
    if len(websitename) ==  0:
        valid_website = False
    else:
        for x in websitename:
            if not x.isalnum():
                valid_website = False
    return valid_website

def validate_ext(extname):
    valid_extension = True
    if len(extname) > 3 or len(extname) < 2:
        valid_extension =  False
    else:
        for x in extname:
            if not x.isalpha():
                valid_extension = False
    return valid_extension

input_string = get_input()
valid_name, valid_ext, name, website, ext = parse_input(input_string)
if not valid_name:
    print(f"Missing the @ - {input_string} is  not a valid email address")
elif not valid_ext:
    print(f"Missing a period -  {input_string} is not a valid email address")
else:
    valid_username = validate_user(name)
    if valid_username:
        valid_websitename = validate_website(website)
        if valid_websitename:
            valid_extension = validate_ext(ext)
            if valid_extension:
                print(f"{input_string} is a valid email address")
            else:
                print(f"{ext} is not a valid extension")
        else:
            print(f"{website} is not a valid web site name")
    else:
        print(f"{name} is not a valid username")
