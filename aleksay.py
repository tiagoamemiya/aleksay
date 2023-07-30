#!/usr/bin/python
# encoding: utf-8

import  random, sys

header_line = "|||||||||||||| ALEKSAY ||||||||||||||"
lformat = f'^{len(header_line)+1}'

with open('messages.txt') as f:
    quotes = f.readlines()

quotes = list([x.strip() for x in quotes if x])

def alek():
    baloon = "___________  __________"
    baloon_footer = "\/"

    print(f'{quote():{lformat}}')
    print(f'{baloon:{lformat}}')
    print(f'{baloon_footer:{lformat}}')
    print("""
       |\\\\\\\\\\\\\\  !
       ||      )
       || ~~  ~~
       (5  - |-|
       ||    J |
       ||  /\\\\\\\\      ||
       |||||||||      ||
       |__  |         | ]]]
   __ /__/\/_\__      | / )
  /             \\     /  /
    """)

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
    alek()
    print(header_line)
    print("")

# main
if __name__ == "__main__":
    main()
