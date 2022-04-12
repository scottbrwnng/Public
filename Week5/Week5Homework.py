
newdict = {}
flag = True
while flag:
    state = input("Please enter a state or press 'q' to exit: ")
    if state == "q":
        flag = False
        print("you have quit")
        break
    elif state in newdict:
        newfact = input(f"please enter another fact about {state}: ")
        fact += "\n" + newfact
        newdict[state] = fact
    else:
        newdict[state] = []
        fact = input(f"Please enter a fact about {state}, or press 'q' to quit: ")
    if fact == "q":
        flag = False
        print("you have quit")
        break
    else:
        newdict[state] = fact
        for state, fact in newdict.items():
            print(f"Some facts about {state} are:\n{fact}")

            

    
    




     