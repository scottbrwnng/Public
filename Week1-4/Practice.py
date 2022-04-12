need_input = True
while need_input:
    string_n = input("Please enter dimensions, or 'q' to quit: ")
    if string_n.lower() == "q":
        need_input = False
        quit_processing = True
    else:
        if string_n.isnumeric():
            need_input = False
            quit_processing = False
            n = int(string_n)
        else:
            need_input = True
            print("please try again")


