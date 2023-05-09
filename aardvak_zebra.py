
"""
make a function that given a sring  returns "aardvark" if the string starts with a.  Otherwise returns 'zebra'
"""

def aardvark(string):
    if string.startswith('a'):
        print ('aardvark')

    else:
        print('zebra')


def aardvark2(string):
    if string[0] == 'a':
        print ('aardvark')

    else:
        print('zebra')


string1= 'amancer'
string2 = 'hola'

aardvark(string1)
aardvark2(string1)
aardvark(string2)
aardvark2(string2)