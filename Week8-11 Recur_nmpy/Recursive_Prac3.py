def smallest_int(x):
    for i in x:
        if len(x) == 0:
            return(None)
        elif len(x) == 1:
            return x[0]
        else:
            y = x.pop()
            z = smallest_int(x)
            if y <= z:
                return y
            else:
                return z
x = [5,4,3,2]
print(smallest_int(x))

