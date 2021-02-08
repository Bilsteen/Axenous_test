#Question 1 :
#Find the characters which have occurred more than once in a string. 
#Replace the character by z which has occurred twice and by x which has occurred more than twice [Note :- Consider #the string as "BOOKKEEPER".]


def replace_char(word):
    new_word = ""
    word_list = list(word.lower())
    word_occurance = {}
    for char in word_list:
        if word_occurance.get(char) == None:
            word_occurance[char] = 1
        elif word_occurance.get(char) != None:
            word_occurance[char] += 1
    for char in word_list:
        if word_occurance.get(char) == 1:
            new_word += char
        elif word_occurance.get(char) == 2:
            new_word += "z"
        else:
            new_word += "x"
    return new_word

print(replace_char("BOOKKEEPER"))