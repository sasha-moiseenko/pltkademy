#!/bin/bash

DIR="./random/*"
for i in {1..100}; do touch ./random/"random_text_$i.txt"; done
for file in $DIR; do
	echo $(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1) > $file
done

