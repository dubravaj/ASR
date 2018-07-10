#!/usr/bin/python3.6

import sys

from Bio.PDB import *
from Bio.Blast import NCBIXML

# parse XML file from BLASTP output and create file with sequences
def parse_XML(pdb_id):
    """parse XML output from BLASTP and create sequence file"""
    i = 0
    try:
        output = open(pdb_id + ".txt", "w")
        xml_file = open(pdb_id + ".xml", "r")
    except IOError as e:
        #print(e.reason)
        sys.exit(1)
    blast = NCBIXML.parse(xml_file)
    names = []
    protein = ''
    # extract sequences from records in PDB
    for record in blast:
        for align in record.alignments:
            for hsp in align.hsps:
                i += 1
                protein = '>' + align.hit_id + align.hit_def  # protein name
                if (protein in names):
                    break  # name already added
                else:
                    names.append(protein)  # add name
                    output.write('>' + align.hit_id + align.hit_def + '\n')
                output.write(hsp.sbjct + '\n')  # find out
    xml_file.close()
    output.close()


name = sys.argv[1]
parse_XML(name)