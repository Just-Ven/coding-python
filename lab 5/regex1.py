# Exercise 1
import re

def match_string(text):
    pattern = r'ab*'
    if re.search(pattern, text):
        return True
    return False

# Test
test_strings = ["a", "ab", "abb", "abbb", "ac", "b", "bb"]
for test_string in test_strings:
    if match_string(test_string):
        print('pattern matches')
    else:
        print('pattern does not match')
