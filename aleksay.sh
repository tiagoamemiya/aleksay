#!/bin/bash

function show_ballon(){
	message=$1
	ballon_size=${#message}
	let ballon_size+=4

	ballon_top=$( printf '#%.0s' $(eval "echo {1.."$(($ballon_size))"}") )
	ballon_bottom=$( printf '#%.0s' $(eval "echo {1.."$(($ballon_size))"}") )
	ballon_margin=$( printf ' %.0s' {1..17} )

	echo "$ballon_margin$ballon_top"
	echo "$ballon_margin# $message #"
	echo "$ballon_margin$ballon_bottom"
}

function show_alek(){
echo "     |\\\\\\\\\\\\\\\\ !
     ||      )
     || ~~  ~~
     (5  - |-|
     ||    J |
     ||  /\\\\       ||
     |||||||||     ||
     |__  |        | ]]]
 __ /__/\/_\__     | / )
/             \\    /  /
"
}

default_messages=(
	"Então mano..."
	"Deixa eu terminar!"
	"WOOOOSAH"
	"Porra Ciro!"
	"Falei!"
	"Posso usar seu terminal?"
)

total_items=${#default_messages[@]}
let total_items-=1
index=$( shuf -i 0-$(eval echo $total_items) -n 1 )

[[ ! -z "$1" ]] && message=$1 || message=${default_messages[index]}

show_ballon "$message"
show_alek