#!/usr/bin/python2.7

from __future__ import print_function
from ete3 import Tree
import sys
import pickle

newick_file = sys.argv[1]
t = Tree(newick_file)
R = t.get_midpoint_outgroup()
t.set_outgroup(R)

leafs = list()
dist_matrix = {}

for node in t.get_leaves():
    if(node.is_leaf()):
        leafs.append(node)

dist_list = []

for leaf0 in leafs:
    dist_matrix[leaf0.name] = {}
    for leaf1 in leafs:
        distance = t.get_distance(leaf0,leaf1)
        dist_matrix[leaf0.name][leaf1.name] = distance

with open('tree_dist_matrix.txt','w') as f:
    l = ''
    for key in dist_matrix.keys():
        for key1 in dist_matrix[key].keys():
            d = dist_matrix[key][key1]
            l+= (str(d) + ' ')
        line = str(key)+ ": " + l + '\n'
        f.write(line)
        l = ''
        line = ''
f.close()

with open('phylo_matrix.txt','w') as phylo:
    pickle.dump(dist_matrix,phylo)

