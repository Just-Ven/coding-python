import re

def snake_to_camel(snake_case_str):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), snake_case_str)

snake_case_input = input("Enter a string in snake_case: ")
camel_case_output = snake_to_camel(snake_case_input)
print(camel_case_output)


