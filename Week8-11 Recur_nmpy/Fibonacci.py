def fiboSeq(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        x = fiboSeq(n-1) + fiboSeq(n-2)
        return x


num = int(input("please enter a positive integer: "))
for x in range(num):
    print(fiboSeq(x))