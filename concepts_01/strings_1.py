"""
Write a function that takes a string as input and returns the count of vowels (a, e, i, o, u) present in the string.
"""

def vowels_count(string):
    """
    Receives string: str
    returns count of vowels
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    total = 0   
    str = string.replace(' ', '')
    for vowel in vowels: 
        total += str.count(vowel)
    return total

sentence = "Hello, how are you?"
print(vowels_count(sentence))


def count_vowels(string):
    vowels = 'aeiou'
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count