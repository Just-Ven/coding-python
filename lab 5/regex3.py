# Exercise 3
import re

def find_sequence(string):
    pattern = r'^[a-z]+_[a-z]+'
    sequences = re.search(pattern, string)
    return sequences if sequences else []


# Функция для тестирования
tests = [
    "abc_def_ghi", "abc_def", "def_ghi",
    "hello_world_python_is_cool", "hello_world", "world_python", "python_is", "is_cool",
    "No_sequences_here", ""
]
for test in tests:
    if find_sequence(test):
        print('Seqeunce found')
    else:
        print('Sequence not found')
