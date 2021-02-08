#Question 2:
#Find number of small and capital letters in a string and replace all capital letters by same small letter and all #small letters by same capital letters


def capital_small(word):
    new_word = []
    for char in word:
        if char == " ":
            new_word.append(char)
        if char == char.upper():
            new_word.append(char.lower())
        else:
            new_word.append(char.upper())
    return "".join(new_word)

print(capital_small("EduCatiON"))
