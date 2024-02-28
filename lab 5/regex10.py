import re

def camel_to_snake(s):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()

camel_case_input = input("input a string in camel case ")
snake_case_output = camel_to_snake(camel_case_input)
print(snake_case_output)
