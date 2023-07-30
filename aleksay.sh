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
     ||  /\\\\\\\\     ||
     |||||||||     ||
     |__  |        | ]]]
 __ /__/\/_\__     | / )
/             \\    /  /
"
}

if [[ ! -z "$1" ]]
	then
	message=$1
elif [ -f 'messages.txt' ]
	then
	IFS=$'\n' default_messages=($(cat messages.txt))
	unset IFS
	total_items=${#default_messages[@]}
	let total_items-=1
	index=$( shuf -i 0-$(eval echo $total_items) -n 1 )
	message=${default_messages[index]}
else
	message='...'
fi


show_ballon "$message"
show_alek