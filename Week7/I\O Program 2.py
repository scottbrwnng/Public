save = open('/Users/scott/Downloads/new_ozymandias.txt', "w")
with open('/Users/scott/Downloads/ozymandias.txt', "r") as file_obj:
    poem = file_obj.readlines()
new_poem = []
line_cnt = 0
word_cnt = 0 
letter_cnt = 0
for x in poem:
    temp = x.split()
    line_cnt += 1
    for i in temp:
        word_cnt += 1
        new_poem.append(i)
for x in new_poem:
    if len(x) == 5:
        letter_cnt += 1

a = str(f"The number of lines is: " +str(line_cnt) +"\n")
b = str(f"The number of words is: " +str(word_cnt) + "\n")
c = str(f"The number of 5 character words is: " +str(letter_cnt))



save.write(a + b + c)

