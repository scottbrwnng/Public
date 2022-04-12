from pickle import TRUE


list1 = [["Mike", 60], ["Joe", 75], ["Sue", 85], ["Anne", 80], ["George", 75]]
score_list = []
for x in list1:
    score_list.append(x[1])
print(score_list)

score_list.sort()
score = score_list[1]
print(score_list)
print(score)

for x in list1:
    if x[1] == score:
        print(f'{x[0]} has the second lowest score of {score}')
