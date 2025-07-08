#!/bin/bash
echo "run using make question2"
echo "This supports only one read for every write and input must first be given in this file"
read -sp "Enter the input from the user for the first file : " userInp

echo ${userInp} > "/tmp/tempfile.txt"
