import numpy as np

def array(n):
    # Creates a nxn arr with a value of zero
    arr = np.zeros((n, n))
    x = n//2
    y = n//2
    dir = 'r'
    # Initates the middle position to 1
    arr[x,y] = 1
    #Establishes base case
    while 0 in arr:
        # I used a brute force approach after a failed attempt to make a function which called itself and repositioned x and y 
        if dir == 'r':
            y += 1
            arr[x,y] = arr[x,y-1] + 1
            if arr[x+1,y] == 0:
                dir = 'd'
            else:
                dir = 'l'
        if dir == 'd':
            x += 1
            arr[x,y] = arr[x-1,y] + 1
            if arr[x,y-1] == 0:
                dir = 'l'
            else:
                dir = 'd'
        if dir == 'l':
            y -= 1
            arr[x,y] = arr[x,y+1] + 1
            if arr[x,y-1] == 0:
                y -= 1
                arr[x,y] = arr[x,y+1] + 1
                dir = 'u'
        if dir == 'u':
            x -= 1
            arr[x,y] = arr[x+1,y] + 1
            if arr[x-1,y] == 0:
                x -= 1
                arr[x,y] = arr[x+1,y] + 1
                dir = 'r'
        return arr
        
user_input = input("Please enter a odd-numbered integer: ")
if user_input.isnumeric() == False:
    print("Please use intergers only")
elif int(user_input) % 2 == 0:
    print("You have entered an even-numbered integer. Please enter odd-numbered integers only.")
else:
    print(array(int(user_input)))



