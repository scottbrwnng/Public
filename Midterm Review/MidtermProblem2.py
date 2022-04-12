

def find_runner_up(list_1 = None):
    if list_1 == None:
        return None
    new_list = []
    for x in list_1:
        if x not in new_list:
            new_list.append(x)
    new_list.sort(reverse=True)
    if len(new_list) >= 2:
        return new_list[1]
    else:
        return None    
        

list_1 = [1,1,1,1,1]
print(find_runner_up(list_1))
