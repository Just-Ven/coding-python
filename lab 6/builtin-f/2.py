def calc(s):
    count_l = 0
    count_u = 0
    for letter in s:
        if letter.islower():
            count_l += 1
        elif letter.isupper():
            count_u += 1
    print(count_l, count_u)

calc('PyThOn')
