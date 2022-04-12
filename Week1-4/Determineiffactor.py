
def append_list():
    in_list = print("Please enter a set of comma seperated integers then hit enter: ")
    in_list.split(", ")
    user_list = []
    for x in in_list:
        user_list.append(x)
    print(user_list)
    return user_list




def find_factor(user_list):
    input_length = int(len(user_list))
    check_list = []
    return_factors = []
    return_number = []
    check_pos = 0
    input_pos = 0
    cont = True
    remainder = 0
    check_list = user_list
    while cont:
        factor_check = user_list[input_pos] % check_list[check_pos]
        if factor_check == 0 and input_pos != check_pos:
            return_factors.append(user_list[input_pos])
            return_number.append(check_list[check_pos])
            if input_pos < input_length:
                input_pos += 1
            else:
                check_pos += 1
                input_pos = 0
        else:
            if input_pos < input_length:
                input_pos += 1
            else:
                check_pos += 1
                input_pos = 0
        if check_pos > 4:
            cont = False
    return return_factors, return_number
      

                
append_list()

