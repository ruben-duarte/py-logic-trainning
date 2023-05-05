
"""
Ex:

arg!
ARG!

gReaT!
GrEAt!

"""

def switch_case(str):
    for letter in str:
        if letter.isupper():
            letter = letter.lower()
            print(letter, end='')
        else:
            letter = letter.upper()
            print(letter, end='')


def switch_case2(str):
    new_str= ''
    for letter in str:
        if letter.isupper():
            new_str+= letter.lower()
        else:
            new_str+= letter.upper()
    print(new_str)


switch_case('gReaT!!')
switch_case2('gReaT!!')