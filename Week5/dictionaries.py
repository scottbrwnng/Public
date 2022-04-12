

# Unordered collection of keys, value pairs
# keys are IMMUTABLE, must be unique
# Values can be any data type
# use len() function to determine number of keys

#

# Define empty dict using:
# purse = dict()   or
# purse = {}

# Define new key value pairs:
# purse['money'] = 12
# purse['candy'] = 1
# purse['tissues'] = 50
# print(purse)
# result: {'money': 12, 'candy': 1, 'tissues': 50}

# Use the key to access the value
# x = purse[‘money’]   # x is now equal to 12
# Note:  You will receive a run-time key error if the key does not exist
# y = purse[‘car-keys’] # will create an error


# CHECK IF KEY EXISTS IN DICTIONARY
# Checking if a key exists in the dictionary: in (and not in)
# 
# if car_keys not in purse:
#   purse[car_keys] = 1
# else:
#   purse[car_keys] += 1
#
# can also check using get() command
# x = purse.get("aspirin") returns None if aspirin does not exist
# x = purse.get("")

# Can also check using the get() command
# x = purse.get(“aspirin”) # returns None if aspirin does not exist
# x = purse.get(“aspirin”, False) # returns False if aspirin does not exist

# Deleting a key-value pair
# del purse[‘aspirin’] 
# purse.pop(‘aspirin’)


# dictionaries are ITERABLE and can be sorted


counts = {'chuck': 42, 'fred': 1, 'jan': 100}
# using for loop:
# for item in counts:
#     print(item)

# # preferred: Specify KEYS, VALUES or ITEMS (or both)
# for key in counts.keys():
#     print(key,counts[key])
# for word_count in counts.values():
#     print(word_count)
# for name, word_count in counts.items():
#     print(name, word_count)

# # sorting – default is to sort the keys 
# for name in sorted(counts):
#     print(name)
# for count in sorted(counts.values()):
#     print(count)




# POP QUESTIONS:

# quiz_scores = {'Teri': 85, 'Matt': 72, 'Jan': 100, 'Michael': 65}
# # for key, item in sorted(quiz_scores.items()):
# #     print(key, item)
# #     print("-----")
# # WHAT DOES THIS PRODUCE?

# # WHAT IS THE CODE TO ADD SUSAN, WITH A SCORE OF 94 TO QUIZ-SCORES?
# quiz_scores['Susan'] = 94
# for key, item in sorted(quiz_scores.items()):
#     print(key, item)
#     print("-----")

# # Example: working with the quiz scores

# student_dict = dict()

# # initiate values
# student_dict["Mike"] = [44, 53, 42, 94]
# student_dict["Ahmed"] = [48, 72, 77, 43]
# student_dict["Marian"] = [85, 51, 72, 90]
# student_dict["Joseph"] = [98, 64, 62, 47]
# student_dict["John"] = [62, 73, 62, 51]
# student_dict["Maria"] = [80, 62, 62, 60]

# # calculate and print the avg by student; print the overall average at the end
# total_score = 0
# total_quizzes = 0

# for student, scores in student_dict.items():
#     total = sum(scores)
#     quiz_average = round(total/len(scores), 2)
#     print(f"The quiz average for {student} is {quiz_average}")
#     total_score += total
#     total_quizzes += len(scores)

# final_average = round((total_score/total_quizzes), 2)
# print(f"The class average is {final_average}")

# EXERCIESE 1: Print a count, by name of the students in a class
class_list = ["Mike", "Shannon", "Mike", "Michele", "Mike", "Ann", "Ann"]
newdict = {}
for i in range(class_list):
    newdict[i]=class_list[i]
print(newdict)
    






# input_text = "this is a sample text with several words"
# input_text += "this is more sample text with several words"
# input_text += "this is the final text with this exercise"
# list = input_text.split(" ")
# dict = dict()

# for i in list:
#     dict[i] = list.count(i)

# for word, count in sorted(dict.items(), key=lambda item:i, reverse=True):
#     print(count,word)

