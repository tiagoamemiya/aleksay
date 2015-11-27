#!/usr/bin/python
# encoding: utf-8

import  random, sys

header_line="|||||||||||||| ALEKSAY ||||||||||||||"
quotes=open("messages.txt").read().split("\n")

# Alek
def alek():
	ballon="___________  __________"
	ballon_footer="\/"
	print ballon.center( len(header_line) , " " )
	print ballon_footer.center( len(header_line) , " " )
	print """
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
	"""

# frase por parâmetro
def quote():
	q=sys.argv[1:]
	if len(q) > 0:
		print " ".join(q).center( len(header_line) , " " )
	else:
		print_random_quote()

# frase randomica
def print_random_quote():
	quote=random.choice(quotes)
	print quote.center( len(header_line) , " " )

# main
def main():
	print
	quote()
	alek()
	print header_line
	print

# main
if __name__ == "__main__":
    main()
