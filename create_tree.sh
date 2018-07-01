#!/usr/bin/env bash

if [ "$1" != "" ]; then
    inputfile=$1
elif [ "$1" == "-h" ]; then
    echo "Create phylogenetic tree using Neighbor Joining"
    echo "Usage:"
    echo "./create_tree filename"
    echo "filename file with distance matrix"
    exit
fi



cp $inputfile infile
echo "Y" | ./neighbor
cp outtree $inputfile'_tree'
cp outfile $inputfile'_output'
rm outtree
rm outfile
rm infile

