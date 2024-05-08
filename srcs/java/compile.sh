#!/bin/bash

if [ "$1" == "-c" ] || [ -z "$1" ]; then
	echo "Compiling project..."
	javac -d "bin/" src/*.java || exit
fi

if [ "$1" == "-r" ] || [ -z "$1" ]; then
	echo "Running project..."
	java -cp "bin/" Translator
fi
