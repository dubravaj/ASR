#!/usr/bin/env bash

if [ "$1" != "" ]; then
    method=$1
    if [ "$2" != "" ]; then
        filename=$2
        if [ "$3" != "" ]; then
            name=$3
        else
            echo "Need more arguments"
            exit
        fi
    else
        echo "Need more arguments"
        exit
    fi

elif [ "$1" == "-h" ]; then
    echo "Calculate distance matrix"
    echo "Usage:"
    echo "./calc_distance_matrix.sh method protein number_of_sequences"
    exit
fi


out_file=$name'_'$method

case "$method" in

bbc)
    calc_bbc.py --fasta $filename -m protein > $out_file
    ;;

lempelziv)
    calc_lempelziv.py --fasta $filename -o $out_file
    ;;

ncd)
    calc_ncd.py --fasta $filename -o $out_file
    ;;

wmetric)
    calc_wmetric.py --fasta $filename -o $out_file
    ;;

word)
    size=5
    calc_word.py --fasta $filename --word_size $size -o $out_file
    ;;

cv)
    size=5
    calc_word_cv.py --fasta $filename --word_size $size -o $out_file
    ;;

d2)
    calc_word_d2.py --fasta $filename -o $out_file
    ;;

ffp)
    size=5
    calc_word_ffp.py --fasta $filename -m protein --word_size $size -o $out_file
    ;;

rtd)
    size=5
    #mozno nastavit vzdialenost
    #nefunguje, vzdialenost nema implementovanu
    calc_word_rtd.py --fasta $filename --word_size $size -d angle_cos_diss -o $out_file
    ;;

*)
    echo "Invalid option"
    exit
    ;;

esac
