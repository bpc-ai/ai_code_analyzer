#!/bin/bash

export PATH=$PATH:~/Documents/work/SonarQube/llvm-project/build/bin/
clang++ --analyze -Xclang -analyzer-checker=debug.ViewCFG $1 2>&1 | tee output.txt

file='output.txt'
png="$(echo $1| cut -d"." -f 1).png"
echo $png
i=1  
while read line; do
	if [ $i = 1 ]; then
		dotfile=$(echo $line| cut -d"'" -f 2)
		echo "$dotfile"
		break
	fi
	i=$((i+1))  
done < $file

cp $dotfile .
dot -Tpng $dotfile -o $png

