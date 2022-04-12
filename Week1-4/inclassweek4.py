##part 1
need_input = True
while need_input:
    string_n = input("please ender an odd integer or press 'q' to quit: ")
    if string_n.lower() == "q":
        need_input = False
        quit_process = True
        print("you have quit")
    else:
        if string_n.isnumeric():
            n = int(string_n)
            if n % 2 != 0:
                need_input = False
                quit_process = True
                print("Thank you for entering an odd intereger")
            else:
                need_input = True
                quit_process = False
                print("please enter an odd number: ")
        else:
            need_input = True
            quit_process = False
            print("please enter a numerical value: ")




