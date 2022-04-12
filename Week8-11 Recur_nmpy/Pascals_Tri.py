
def triangle(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        tri = [[1]]
        for x in range(n - 1):
            temp = [0] + tri[-1] + [0]
            row = []
            for y in range(len(tri[-1]) + 1):
                row.append(temp[y] + temp[y + 1])
            tri.append(row) 
        return max(tri) #you can remove the 'max' to see the whole triangle

usr_input = input("Please enter a positive integer: ")
if usr_input.isdigit() == True:
    print(triangle(int(usr_input)))
elif usr_input == "q":
    print("you have exited the program.")
else:
    print("you have entered a negative or non-integer value. Enter positive integers only.")

