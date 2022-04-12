list1 = ["M", "na", "i", "Mi"]
list2 = ["y", "me", "s", "ke"]
out_string = ""
for x in list1:
    in_index = list1.index(x)
    out_string = out_string + x + list2[in_index] + " "
print(out_string)
