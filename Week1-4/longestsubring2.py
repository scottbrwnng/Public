string = input("please enter a string:")
out_chars = {}
start = 0
maxlen = 0
n = len(string)

for i in range(n):
    if out_chars[i] in out_chars:
        out_chars[i] = i
    else: 
        start = max(start, out_chars[string[i]] + 1)
    out_chars[string[i]] = i
    maxlen = max(maxlen, start - i + 1)

print(out_chars)

