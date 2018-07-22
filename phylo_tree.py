#!/usr/bin/python2.7

from __future__ import print_function
from ete3 import Tree
import pickle
from collections import OrderedDict


class PhyloTreeDistanceMatrix(object):

    _matrix_object_filename = 'phylo_matrix.txt'
    _tree_matrix_filename = 'tree_dist_matrix.txt'
    _matrix = {}
    _all_leaves = []

    def __init__(self, newick_file):
        self._t = Tree(newick_file)

    def create_distance_matrix_file(self, tree_matrix=_tree_matrix_filename, matrix_object=_matrix_object_filename):
        """create rooted phylogenetic tree and then use it to generate distance matrix file with distances between nodes"""
        R = self._t.get_midpoint_outgroup()
        self._t.set_outgroup(R)

        # need to use ordered dict to keep order of keys, no need in 3.6
        dist_matrix = OrderedDict()

        # get leaves from tree
        leaves = [node for node in self._t.get_leaves() if node.is_leaf()]

        # create distance matrix
        for leaf0 in leaves:
            dist_matrix[leaf0.name] = OrderedDict()
            for leaf1 in leaves:
                distance = self._t.get_distance(leaf0, leaf1)
                dist_matrix[leaf0.name][leaf1.name] = distance

        # save matrix as text file
        with open(tree_matrix, 'w') as f:
            l = ''
            for key in dist_matrix.keys():
                for key1 in dist_matrix[key].keys():
                    d = dist_matrix[key][key1]
                    l += (str(d) + ' ')
                line = str(key)+ ": " + l + '\n'
                f.write(line)
                l = ''
                line = ''
        f.close()

        # save matrix object
        with open(matrix_object, 'w') as phylo:
            pickle.dump(dist_matrix, phylo)
        phylo.close()

    def load_distance_matrix(self, matrix_file):
        """load matrix object from specific file"""
        matrix = pickle.load(matrix_file)
        self._matrix = matrix

    def get_matrix_item(self, rowname, colname):
        """return item from distance matrix specified by row and column"""
        return self._matrix[rowname][colname]

    def delete_nodes(self, default_seq_name="1A2P_defal", num_of_leaves=100, tree_file="new_tree.newick"):
        """delete leaves far from original sequence, after deleting the tree will contain num_of_nodes leaves """
        leaves_dict = {}
        self._all_leaves = [node for node in self._t.get_leaves() if node.is_leaf()]
        num_leaves = len(self._all_leaves)

        for item in self._all_leaves:
            leaves_dict[item.name] = self.get_matrix_item(default_seq_name, item.name)

        sorted_leaves_dict = sorted(leaves_dict.items(), key=lambda x: x[1], reverse=True)

        for item in sorted_leaves_dict:
            deleted_leaf = self._t.search_nodes(name=item[0])[0]
            if (num_leaves > num_of_leaves):
                deleted_leaf.delete()
                num_leaves -= 1

        self._t.write(format=1, outfile=tree_file)
        self.create_distance_matrix_file()

    def delete_clusters(self, strategy='mean', tree_file="new_tree.newick"):
        nodes = [node for node in self._t.get_leaves() if node.is_leaf()]
        sorted_nodes = {}
        if strategy == 'mean':
            mean = 0.0
            size = len(nodes)
            for node in nodes:
                mean += self.get_matrix_item("1A2P_defal", node.name)
            mean /= size
            print(mean)
            for item in nodes:
                sorted_nodes[item.name] = self.get_matrix_item('1A2P_defal', item.name)

            sorted_nodes = sorted(sorted_nodes.items(), key=lambda x: x[1], reverse=True)
            for item in sorted_nodes:
                if item[1] > mean:
                    deleted_leaf = self._t.search_nodes(name=item[0])[0]
                    deleted_leaf.delete()

            self._t.write(format=1, outfile=tree_file)