# 65-90 capital
# 97-122 lowercase

# shift = int(input("Enter a shift: "))
# sentence = input('Enter a sentance: ')

# longer way
def shift1(offset,string):
    offset = offset % 26
    final = ""
    for character in string:
        if character.isalpha() == False:
            final += character
        else:
            ascii_value = ord(character)
            if ascii_value in range(65,90):
                if (ascii_value + offset) in range(65,91):
                    final += chr(ascii_value + offset)
                else:
                    ascii_value = ascii_value + offset - 26
                    final += chr(ascii_value)
            # this else block will run if ascii_value in range(97-122):
            else:
                if (ascii_value + offset) in range(97,123):
                    final += chr(ascii_value + offset)
                else:
                    ascii_value = ascii_value + offset - 26
                    final += chr(ascii_value)
    return final

# shorter formula way
def shift2(offset,string):
    final = ""
    offset = offset % 26

    for character in string:
        if character.isalpha() == False:
            final += character
        else:
            if character.isupper():
                ascii_value = (ord(character) - 65 + offset) % 26 + 65
                final += chr(ascii_value)
            else:
                ascii_value = (ord(character) - 97 + offset) % 26 + 97
                final += chr(ascii_value)

    return final

string = 'this is my name kocheta #@$$$'
offset = 67

print(shift1(offset,string))
print(shift2(offset,string))
