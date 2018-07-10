#!/usr/bin/env bash

filename="$1"

while read -r line
do
    name=$line
    mkdir $name
    #./run_blast.sh $name
    for method in "bbc" "lempelziv" "ncd" "wmetric" "word" "cv" "d2" "ffp"; do
        ./calc_distance_matrix.sh $method $name 250
        cp $name'_250_'$method ./$name/$name'_250_'$method
        ./create_tree.sh $name'_250_'$method
        cp $name'_250_'$method'_output' ./$name/$name'_250_'$method'_output'
        cp $name'_250_'$method'_tree' ./$name/$name'_250_'$method'_tree'
        rm $name'_250_'$method
        rm $name'_250_'$method'_output'
        rm $name'_250_'$method'_tree'
    done


done < $filename
