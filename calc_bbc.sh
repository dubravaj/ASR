#!/usr/bin/env bash

name=$1
count=$2
fasta_file=$name'_'$count'.txt'
out_file=$name'_bbc'

calc_bbc.py --fasta $fasta_file -m protein > $out_file