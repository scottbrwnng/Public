str1 = "This woman has to be gotten to the hospital. The hospital? What is it? It's a big building with patients but that is not important right now."
check_list = []
new_dict = {}
stripped_string = str1.replace(".", "")
stripped_string1 = stripped_string.replace("?", "")
split_string = stripped_string1.split(" ")
for x in split_string:
    check_list.append(x)
    if x in check_list:
        new_dict[x] = check_list.count(x)
print(new_dict)
        