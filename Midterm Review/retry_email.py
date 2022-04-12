# username can only have letters, digits, dashes, and underscores. It must have a len of 1 or greater.
# webiste name can only have letters and digits. len >=1.
# extension can only contain letters
# maximum length of the extension is 3, minimum is 2.

def split_email(user_email):
    at_pos = user_email.find("@")
    period_pos = user_email.find(".")
    username = user_email[:at_pos]
    website = user_email[at_pos:period_pos]
    extension = user_email[period_pos:]
    return at_pos, period_pos, username, website, extension
def check_user(username):
    x = int(len(username))
    if username.isalnum() == False or x < 1:
        print("you have entered too short of a username")
    else:
        valid_user = True
        return valid_user

def check_website(website):
    valid_web = True
    x = int(len(website))
    while valid_web:
        if website.isalnum() == True and x >= 1:
            valid_web = True
        else: 
            valid_web = False
            print("you have entered an invalid character for the website")
    return valid_web



user_email = input("please enter a string for your email address: ")
at_pos, period_pos, username, website, extension = split_email(user_email)
check_user(username)
check_website(website)



