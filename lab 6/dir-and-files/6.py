import string

def generate_files():
    for letter in string.ascii_uppercase:
        filename = f"{letter}.txt"
        f = open(filename, 'x')

generate_files()