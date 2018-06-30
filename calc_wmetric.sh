#!/usr/bin/env bash


name=$1
count=$2
fasta_file=$name'_'$count'.txt'
out_file=$name'_ncd'


calc_ncd.py --fasta $fasta_file -o $out_file