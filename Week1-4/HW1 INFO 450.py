verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
textlegnth = len(verse)
print("\nThe legnth of the verse is {}".format(textlegnth))
capital13 = verse[12].isupper()
print("\nIs the 13th letter of the verse a capital letter?: {}" .format(capital13))
andindex = verse.index("and")
print("\nThe position of the first \'and' in the verse is: {}" .format(andindex))
andrindex = verse.rindex("and")
print("\nThe position of the last \'and' in the verse is: {}" .format(andrindex))
print("\nThe text between the first and last occurrences of \'and' are:\n {}" .format(verse[andindex:andrindex]))
print("\nThe word \'you' occurs in the verse {} times." .format(verse.count("you")))
print("\nThe word \'mike' occurs in the verse {} times." .format(verse.count("mike"))) 


andcount = f"{verse.count('and')}"
betweenand = verse[verse.index('and'):verse.rindex('and')]
ifappears = verse[3:].lower().count('if')
print(f"""\nThe word 'and' occurs {andcount} times in the verse.
\nThe text between the first and last appearances of 'and' are:
\n{betweenand}
\n The number of times 'if' appears {ifappears} times in the verse.
""")
