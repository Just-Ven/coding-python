import re
# нужно найти паттерн нахождение прописной буквы за которой следует строчная буква
def find_sequence(s):
    pattern = r'[A-Z][a-z]+'
    sequences = re.search(pattern, s)
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