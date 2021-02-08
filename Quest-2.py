#Question 2:
#Find number of small and capital letters in a string and replace all capital letters by same small letter and all #small letters by same capital letters


def capital_small(word):
    new_word = ""
#     word_list = list(word)
    for char in word:
        if char == " ":
            new_word += char
        if char == char.upper():
            new_word += char.lower()
        else:
            new_word += char.upper()
    return new_word

print(capital_small("EduCatiON"))