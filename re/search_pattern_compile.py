#!/usr/bin/python

import re

def pattern_search():

    
    pattern = 'the'
    str_re = re.compile(pattern)

    file = open('files.txt', 'r') 
    matches = 0
    lines  = 0
    for line in file:
        match = str_re.search(line)
        if match:
            matches += 1
        lines += 1
    return (matches, lines)


if __name__ == '__main__':
    matches, lines = pattern_search()
    print('Lines::', lines)
    print('Matches::', matches)


