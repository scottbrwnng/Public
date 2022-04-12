

def longestSubstring(str): #sets function
    n = len(str) #length of the user input substring
    st_pt = 0 # starting point of 
    maxlength = 0 #maximum length of the output string
    st_ind = 0 # starting index of output string
    position = {} #stores output string
    position[str[0]] = 0 # sets position of output string starts at 0

    for i in range(1,n):
        if str[i] not in position:
            position[str[i]] = i #if current character is NOT currently in string, adds character to output string
        else: 
            if position[str[i]] >= st_pt: #if it is, than it moves the starting position over after the last occurance of the current character
                currentlength = i - st_pt #set the length of the working substring with the current character - the current starting point
                if maxlength < currentlength: #if the previously max lenth is less than the current length, 
                    maxlength = currentlength #than update the max length
                    st_ind = st_pt 
                st_pt = position[str[i]]+1 #moves the starting point of the next substring
            position[str[i]] = i #updates position of current character
    if maxlength < i - st_pt: #if current character - starting point is less than the length of longest substring,
        maxlength = i - st_pt #than reset max length
        st_ind = st_pt #set starting index of the longest substring at the starting point of the last current string
    return str[st_ind : st_ind + maxlength]


str = input("please enter a string: ") #driver code for longestString function
    
if len(longestSubstring(str)) > 3:
    print("the longest non-repeating substring is:", longestSubstring(str))
else:
    print("too small for printing")
            
