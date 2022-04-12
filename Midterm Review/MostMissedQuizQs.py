from tkinter import Y



def outer():
    first_num = 1
    def inner():
        second_num = 2
        print("first num from outer", first_num)
        print("second num from inner", second_num)
    inner()
outer()