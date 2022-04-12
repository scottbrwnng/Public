def gcd(n, k):
    if n == k:
        print("You have reached greatest common demonemator")
        return(n)
    elif n > k:
        print(n, k) #optional
        return gcd((n-k), k)
    else:
        print(n, k) #optional
        return gcd((k-n), n)

print(gcd(225, 85))
