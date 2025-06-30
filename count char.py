def char_count(inputstr):
    char_freq={}
    for char in inputstr:
        char_freq[char]=char_freq.get(char,0)+1
    return char_freq
str="python_is_easy"
result=char_count(str)
print("Result is: ",result)
