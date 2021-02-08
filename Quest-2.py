#Question 2:
#Find number of small and capital letters in a string and replace all capital letters by same small letter and all 
#small letters by same capital letters


def capital_small(word):
    new_word = []
    cap = 0
    small = 0
    for char in word:
        if char == " ":
            new_word.append(char)
        if char == char.upper():
            cap += 1
            new_word.append(char.lower())
        else:
            small += 1
            new_word.append(char.upper())
    return cap,small,"".join(new_word)

cap,small,output = capital_small("EduCatiON")

print(f"Number of capital letters are {cap}")
print(f"Number of small letters are {small}")
print(f"Output is {output}")
