string1 = input("please enter a string:")
n = int(input("please enter number of substrings as an integer: "))
sub_length = len(string1)//n

new_array=[]
count_sub = 1
start=0
while count_sub < n:
    stop = start + sub_length
    new_array.append(string1[start:stop])
    start = stop
    count_sub += 1
if count_sub == n:
    new_array.append(string1[start:])
print(new_array)
for substring in new_array:
    duplicates = []
    for letter in substring:
        if letter not in duplicates:
            duplicates.append(letter)
    print(''.join(duplicates))