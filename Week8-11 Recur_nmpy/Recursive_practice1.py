def countdown(n):
    if n == 0:
        print("I love programming in python")
        return()
    else:
        print(n)
        countdown(n-1)
countdown(10)