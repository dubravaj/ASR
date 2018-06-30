#!/usr/bin/env bash

name=$1
count=$2
fasta_file=$name'_'$count'.txt'
out_file=$name'_lempelziv'

calc_lempelziv.py --fasta $fasta_file -o $out_file