state_dict = {}
state_input = True
while state_input:
    state_names = input("Please enter a state or press 'q' to quit: ")
    if state_names.lower() == "q":
        state_input = False
    else:
        state_facts = []
        input_facts = True
        while input_facts:
            fact = input("Please enter a fact: ")
            if fact.lower() == "q":
                input_facts = False
            else:
                state_facts.append(fact)
            state_dict[state_names] = state_facts

for keys, values in state_dict.items():
    print(f"some facts about {keys} are {values}")


