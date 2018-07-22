#!/usr/bin/python2.7
import sys
from phylo_tree import PhyloTreeDistanceMatrix

newick_file = sys.argv[1]

pt = PhyloTreeDistanceMatrix(newick_file)
#pt.create_distance_matrix_file()

matrix_name = 'phylo_matrix_blasted_uniprot.txt'

with open(matrix_name, 'r') as matrix_handle:
    pt.load_distance_matrix(matrix_handle)
    pt.delete_clusters()

