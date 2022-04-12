# problem 1
string1 = input("please enter a string")
string_len = len(string1)
middle_char = (string_len // 2)
print(middle_char)
new_string = ""
new_string = string1[middle_char -1] + string1[middle_char] + string1[middle_char+1]
print(new_string)

#problem 2
s1 = "ABCDEFG"
s2 = "HIJKLMN"
s1_legnth = len(s1)
s2_legnth = len(s2)
s1_middle = (s1_legnth // 2)
s2_middle = (s2_legnth // 2)
first_middle_last = s1[0:1]+ s1[s1_legnth // 2] + s1[5:6] 
first_middle_last2 = s2[0:1]+ s2[s2_legnth // 2] + s2[5:6] 
print(first_middle_last)
print(first_middle_last2)

#problem 3
s1 = "ABCDEFG"
s2 = "HIJKLMN"
s3 = s1[0]+s2[-1]+s2[1]+s2[-2]+s1[1:]+s2[2:-2]
print(s3)

#problem 4
s1 = input("Please type a word:")
s2 = s1[::-1].upper()
print(s2)

#problem 5
s1 = "ABCDEFG"
s2 = s1[0:-2]+s1[-1]
print(s2)