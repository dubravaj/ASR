#!/usr/bin/env bash

if [ "$1" != "" ]; then
    method=$1
fi

name=$2
count=$3
fasta_file=$name'_'$count'.txt'
out_file=$name'_'$method

case "$method" in

bbc)
    calc_bbc.py --fasta $fasta_file -m protein > $out_file
    ;;

lempelziv)
    calc_lempelziv.py --fasta $fasta_file -o $out_file
    ;;

ncd)
    calc_ncd.py --fasta $fasta_file -o $out_file
    ;;

wmetric)
    calc_wmetric.py --fasta $fasta_file -o $out_file
    ;;

word)
    calc_word.py --fasta $fasta_file --word_size 10 -o $out_file
    ;;

cv)
    size=3
    calc_word_cv.py --fasta $fasta_file --word_size $size -o $out_file
    ;;

d2)
    calc_word_d2.py --fasta $fasta_file -o $out_file
    ;;

ffp)
    size=5
    calc_word_ffp.py --fasta $fasta_file -m protein --word_size $size -o $out_file
    ;;

rtd)
    size=10
    #mozno nastavit vzdialenost
    calc_word_rtd.py --fasta $fasta_file --word_size $size -o $out_file
    ;;

*)
    echo "Invalid option"
    exit
    ;;

esac
