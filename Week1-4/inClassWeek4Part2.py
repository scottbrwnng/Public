need_input = True
while need_input:
    string_n = input("please ender an odd integer or press 'q' to quit: ")
    if string_n.lower() == "q":
        need_input = False
        quit_process = False
        print("you have quit")
        break
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
                print("please enter an odd integer")
        else:
            need_input = True
            quit_process = False
            print("please enter a numerical value: ")
    if quit_process:
        num_char = n *2 - 1
        mid_char = num_char // 2
        for i in range(n):
            out_string = ""
            for x in range(num_char):
                out_char = " "
                if i == n - 1:
                    out_char = "*"
                elif (x == mid_char - i) or (x == mid_char + i):
                    out_char = "*"
                out_string += out_char
            print(out_string)
    else:
        print("Thank you")

