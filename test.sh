#!/bin/bash

arr=(
	'asss bxx c' 
	'd eddd f'
	)
#arr[0]=(1 2)
#arr[1]=(3 4)
for a in ${arr[@]};
do

	var=($a)
	echo $var
#	for v in ${var[@]};
#	do
#		echo $v
#	done

done

