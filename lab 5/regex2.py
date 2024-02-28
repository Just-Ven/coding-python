# Exercise 2
import re

def pattern_match(string):
    pattern = r'abbb*' # or we can be rewrite like r'ab{2,3}'
    if re.search(pattern, string):
        return True
    return False


test_strings = ["abb", "abbb", "abbbb", "aabbb", "ab", "abbcc", "ac", "bb", "b"]

for test_string in test_strings:
    if pattern_match(test_string):
        print('pattern match')
    else:
        print('pattern does not much')
