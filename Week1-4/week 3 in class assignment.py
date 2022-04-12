low_score_rank = 2
input_list = [("Mike", 60), ("Joe", 75), ("Sue", 85), ("Anne", 80), ("George", 75)]
score_list = []
for x in input_list:
    score_list.append(x[1])
score_list.sort()
score = score_list[low_score_rank-1]
print("The second lowest score is:", score)
# sorts list and prints second lowest score
for x in input_list: 
    if x[1]== score:
        print(x[0], "has a score of", score)
# prints second lowest score and everyone who has it

###### part 2 ######

num_items = input("Please enter a number: ")
output_string = ""
in_tuple = tuple()
int_list = []
for x in range(int(num_items)):
    int_list.append(x)
    output_string += str(x) + " "
output_string_rev = output_string.sort(reverse=True)
print(output_string)