# Make a function lowercase that, given a string, returns the 
# string, except in all lowercase letters.

def lowercase(string):
    new_string = " " + string.lower() + " "
    frame = new_string.center(40,"+")
    print(frame)
    return new_string

string = "HOLA MUNDO"

lowercase(string)
