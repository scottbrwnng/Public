
update = open('/Users/Scott/Downloads/updated_accounts_rec.txt', "w")   
filename = '/Users/Scott/Downloads/accounts_rec.txt'
with open(filename, "r") as file_object:
    lines = file_object.readlines()

for x in lines:
    data = x.strip().split()
    if data[0] == '300':
        data[1] = 'William'
    elif data[0] == '400':
        data[2] = float(data[2]) + 200.00
    new_str = str(data)
    print(new_str)
    update.write(new_str + "\n")
update.close()

