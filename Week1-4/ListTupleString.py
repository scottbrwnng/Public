in_number = input('Please enter a number: ')
output_string = ""
in_tuple = ()
in_list = []
for x in range(int(in_number)):
    in_list.append(x)
    output_string += str(x) + " "
print(output_string)

for x in output_string.split(" "):
    in_tuple += tuple(x)
print(in_tuple)
running_total = 0
for x in in_tuple:
    running_total += int(x) ** 3 
    print(running_total)
print(f'= {running_total}')
