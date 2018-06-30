#!/usr/bin/env python

from alfpy.utils import seqrecords
from alfpy.utils import distmatrix
from alfpy import ncd



fh = open('1a2p_250.txt')
seq_records = seqrecords.read_fasta(fh)
fh.close()
print(seq_records)
print(seq_records.seq_list)

dist = ncd.Distance(seq_records)
matrix = distmatrix.create(seq_records.id_list,dist)
print(matrix.display())