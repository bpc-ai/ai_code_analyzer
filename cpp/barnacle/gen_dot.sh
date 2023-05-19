#!/bin/bash

# find *.h *.cpp -exec cpp-merge --include ./ --source ./ {} \; >> combined.cpp

export PATH=$PATH:~/Documents/work/SonarQube/llvm-project/build/bin/
clang++ --analyze -Xclang -analyzer-checker=debug.ViewCFG combined.cpp 2>&1 | tee output.txt

file='output.txt'
echo $png
i=1  
while read line; do
	dotfile=$(echo $line| cut -d"'" -f 2)
	png="combined.$i.png"
	echo "$png"
	cp $dotfile .
	localdotfile=$(echo $dotfile| cut -d"/" -f 3)
	echo "$localdotfile"
	dot -Tpng $localdotfile -o $png
	i=$((i+1))  
done < $file

