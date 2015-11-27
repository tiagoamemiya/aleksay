#!/usr/bin/python
# encoding: utf-8

import  random, sys

header_line="|||||||||||||| ALEKSAY ||||||||||||||"
quotes=open("messages.txt").read().split("\n")
quotes=filter(bool, quotes)

# Alek
def alek():
    ballon="___________  __________"
    ballon_footer="\/"
    ballon='{s:{c}^{n}}'.format(s=ballon,n=len(header_line),c=' ')
    print(ballon)
    ballon_footer='{s:{c}^{n}}'.format(s=ballon_footer,n=len(header_line),c=' ')
    print(ballon_footer)
    print ("""
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

# frase por parâmetro
def quote():
    q=sys.argv[1:]
    if len(q) > 0:
        print(" ".join(q).center( len(header_line) , " " ))
    else:
        print_random_quote()

# frase randomica
def print_random_quote():
    quote=random.choice(quotes)
    quote='{s:{c}^{n}}'.format(s=quote,n=len(header_line),c=' ')
    print(quote)

# main
def main():
    print("")
    quote()
    alek()
    print(header_line)
    print("")

# main
if __name__ == "__main__":
    main()
