import re

def find_sequence(s):
    pattern = r'a.b' # a.b$
    sequences = re.search(pattern, s)
    return sequences if sequences else []

strings = [
    "abc", "axb", "aaaab", "a$b", "a\nb",
    "abb", "a", "bcd", "ab",
    "asjkdabcaksjdk", "asdjfabcaksdfj", "adkfjabc",
    "aAbB", "aXb", "aaaabb", "a$bC", "a\nB",
    "aBB", "AB", "BCD", "AB"
]

for string in strings:
    if find_sequence(string):
        print('Sequence found')
    else:
        print('Sequence not found')