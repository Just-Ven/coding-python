import re

def replace(s):
    pattern = r'[ ,.]'
    replaced_s = re.sub(pattern, ':', s)
    return replaced_s

tests = [
    "This is a test string.", "This:is:a:test:string:",
    "Hello, world!", "Hello::world:",
    "One, two, three.", "One::two::three:",
    "",  # Пустая строка
    "NoReplacementNeeded", "NoReplacementNeeded",  # Строка без символов, требующих замены
    "Spaces   and   multiple, commas. And... dots", "Spaces:::and:::multiple:::commas:::And:::d:::ots"  # Множественные пробелы и знаки препинания
]

for test in tests:
    print(replace(test))