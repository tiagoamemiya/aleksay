#!/usr/bin/python
# encoding: utf-8

import random
import sys

from os import path

header_line = "|||||||||||||| ALEKSAY ||||||||||||||"
lformat = f'^{len(header_line)+1}'

with open(path.join(path.dirname(__file__), 'messages.txt')) as f:
    quotes = f.readlines()

quotes = list([x.strip() for x in quotes if x])

def alek():
    baloon = "___________  __________"
    baloon_footer = "\/"

    result = ""
    result += f'{quote():{lformat}}\n'
    result += f'{baloon:{lformat}}\n'
    result += f'{baloon_footer:{lformat}}\n'
    result += """
       |\\\\\\\\\\\\\\  !
       ||      )
       || ~~  ~~
       (5  - |-|
       ||    J |
       ||  /\\\\\\\\      ||
       |||||||||      ||
       |__  |         | ]]]
   __ /__/\/_\__      | / )
  /             \\     /  /\n
"""
    result += header_line

    return result

def quote():
    q = sys.argv[1:]
    if len(q) > 0:
        return ' '.join(q)

    return random_quote()

def random_quote():
    return random.choice(quotes)

# main
def main():
    print("")
    print(alek())
    print("")

# main
if __name__ == "__main__":
    main()
