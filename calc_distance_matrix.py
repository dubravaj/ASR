#!/usr/bin/python

import sys
from alfpy.utils import seqrecords
from alfpy.utils import distmatrix
from alfpy.utils.data import subsmat
from alfpy import bbc
from alfpy import ncd
from alfpy import wmetric
from alfpy import word_pattern
from alfpy.utils.data import seqcontent
from alfpy import word_vector
from alfpy import lempelziv
from alfpy import word_d2

infile = ""
outfile = ""
method = ""

if len(sys.argv) > 4:
    sys.stderr.write("Too many arguments\n")
    exit(1)
else:
    method = sys.argv[1]
    infile = sys.argv[2]
    outfile = sys.argv[3]

input_file = open(infile, 'r')
seq_records = seqrecords.read_fasta(input_file)
input_file.close()

#choose one method to compute distance matrix
if method == "bbc":
    alphabet = seqcontent.get_alphabet('protein')
    vector = bbc.create_vectors(seq_records, 10, alphabet)
    dist = bbc.Distance(vector)
    matrix = distmatrix.create(seq_records.id_list, dist)
    matrix.display()

elif method == "ncd":
    dist = ncd.Distance(seq_records)
    matrix = distmatrix.create(seq_records.id_list,dist)
    matrix.display()

elif method == "wmetric":
    matrix = subsmat.get('blosum62')
    dist = wmetric.Distance(seq_records, matrix)
    matrix = distmatrix.create(seq_records.id_list, dist)
    matrix.display()

elif method == "d2":
    patterns = []
    for i in range(1, 5 + 1):
        p = word_pattern.create(seq_records.seq_list, i)
        patterns.append(p)

    counts = []
    for p in patterns:
        c = word_vector.Counts(seq_records.length_list, p)
        counts.append(c)

    countsweight = []
    weights = seqcontent.get_weights('protein')
    weightmodel = word_vector.WeightModel(weights)
    for p in patterns:
        c = word_vector.CountsWeight(seq_records, p, weightmodel)
        countsweight.append(c)
    dist = word_d2.Distance(countsweight)
    matrix = distmatrix.create(seq_records.id_list, dist)
    matrix.display()

elif method == "lempelziv":
    distance = lempelziv.Distance(seq_records)
    l = ['d', 'd_star', 'd1', 'd1_star', 'd1_star2']
    for el in l:
        distance.set_disttype(el)
        matrix = distmatrix.create(seq_records.id_list, distance)
        matrix.display()

