# Write and invoke a function which:
# receives as input two integers
# returns the sum, the difference, and the products of the two integers
# main program prints the outputs of the function


def new_fuct():
    x = int(input("Please enter an integer: "))
    y = int(input("Please enter another integer: "))
    sum = x + y
    product = x * y
    if x > y:
        difference = x - y
    else:
        difference = y - x
    return sum, product, difference
print(new_fuct())

