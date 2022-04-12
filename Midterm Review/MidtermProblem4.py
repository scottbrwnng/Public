alnum_list = []
singleton_list = []
cont = True
while cont:
    str1 = input("Please enter an alphanumberic value or press 'q': ")
    if str1.isalnum() == False:
        print("you have entered a non- alphanumeric character")   
    elif str1 == "q" or str1 == "Q":
        cont = False
    else:
        alnum_list.append(str1)

for x in alnum_list:
    if x not in singleton_list:
        singleton_list.append(x)
    else:
        singleton_list.remove(x)
print(singleton_list)






