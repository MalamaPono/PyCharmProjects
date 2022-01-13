# ord(character) returns the ascii value of a character

def getvalue(letter_to_shift_by):
    letter_to_shift_by = letter_to_shift_by.lower()
    value = ord(letter_to_shift_by) - 96
    return value

def shift_by_word(letter,word,index):
    if 65 <= ord(letter) <= 90:
        lowercase = False
    else:
        lowercase = True

    letter_to_shift_by = word[index]
    value = getvalue(letter_to_shift_by)
    new_letter = ''
    if (ord(character) + value > 90) and (lowercase == False):
        new_letter = chr(ord(character) + value - 90 + 64)
    elif (ord(character) + value > 122) and (lowercase == True):
        new_letter = chr(ord(character) + value - 122 + 96)
    else:
        new_letter = chr(ord(character) + value)

    return new_letter

phrase = input('Enter a phrase: ')
word = input('Enter a word to shift by: ')

index = 0
final_string = ''
for character in phrase:
    if index == len(word):
        index = 0
    if (65 <= ord(character) <= 90) or (97 <= ord(character) <= 122):
        new_letter = shift_by_word(character,word,index)
        index += 1
        final_string += new_letter
    else:
        final_string += character

print(final_string)