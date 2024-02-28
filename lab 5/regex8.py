import re

def split(s):
    return re.findall(r'[A-Z][a-z]*', s)

user_input = input("input a string in c camel case: ")
words = split(user_input)
print(words) # or we can loop it
