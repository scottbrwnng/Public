# Write a Python program to create a list of numbers
# whose values are the squares of numbers 1 through 30.
# Print the first and last 5 members of the list.

total = []
for i in range(1,30):
    total.append(i ** 2)
print(total[:5])
print(total[-5:])