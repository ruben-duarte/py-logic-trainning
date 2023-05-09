"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""

def split_string_pair(string):
    length = len(string)
    pairs_letters = []
    k = 1
    if length % 2 != 0:
        new_length = length - 1
        final_pair = string[-1] + "_"
        for index in range(new_length//2):
            pairs_letters.append(string[2*index : k*2])
            k += 1
        pairs_letters.append(final_pair)
    else:
        for index in range(length//2):
            pairs_letters.append(string[2*index : k*2])
            k += 1
    print(pairs_letters)
 
        
split_string_pair('abcfe' )
split_string_pair('abcdef')


def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result

import re

def solution(s):
    return re.findall(".{2}", s + "_")


def solution(s):
    return [s[x:x+2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]

def solution(s):
    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]