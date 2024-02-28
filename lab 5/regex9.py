import re

def insert(camel_case_str):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', camel_case_str)

camel_case_input = input("input a string in camel case ")
spaced_output = insert(camel_case_input)
print(spaced_output)
