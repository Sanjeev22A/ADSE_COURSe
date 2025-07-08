#!/bin/bash

if [ -f "/tmp/tempfile.txt" ];
then 

file=$(cat "/tmp/tempfile.txt")

for line in $file
do
    echo -e "$line\n"
done

rm "/tmp/tempfile.txt"
else

echo "Enter the input first by running q2.sh file"
fi