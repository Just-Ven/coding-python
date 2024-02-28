import re

def find_sequence(s):
    pattern = r'[A-Z]+[a-z]'
    sequences = re.findall(pattern, s)
    return sequences if sequences else []

tests = [
    "AbcDefGhi", "abcDef", "DefGhi", "HelloWorldPythonIsCool", "helloWorld", "WorldPython", "PythonIs", "IsCool",
    "NoSequencesHere", "", "Multiple   WordsHere"
        ]

for test in tests:
    if find_sequence(test):
        print('Sequence found')
    else:
        print('Sequence not found')