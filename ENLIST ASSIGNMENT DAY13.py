#Write a Python program to check that a string contains only a certain set of characters

import re
def allowed_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(allowed_char("ABCabcf124fsa50"))
print(allowed_char("*&%@#!}{"))

print("\n*****************************************\n")


# Write a Python program that matches a word containing 'ab'.

def match(text):
        patterns = '\w*ab.\w*'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return'Match not found!'


print(match("Deira"))
print(match("Abraham Lincoln"))
print(match('abe'))
print("\n*****************************************\n")

# Write a Python program to check for a number at the end of a word/sentence

def num_end(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False

print(num_end('abcdef634556'))
print(num_end('abc'))
print("\n*****************************************\n")

# Write a Python program to match a string that contains only uppercase letters

def match1(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return 'Match not Found!'

print(match1("Pack my box with twelve dozen liquor jugs."))
print(match1('Stoicism_chapter_1'))
print("\n*****************************************\n")