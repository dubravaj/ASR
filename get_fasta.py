#!/usr/bin/python3.6


import urllib.request
import os
import sys

def get_fasta(pdb_id, chain):
    """"get FASTA file for selected chain"""
    fasta_file = pdb_id + ".fasta"
    if(os.path.exists(fasta_file) and os.path.getsize(fasta_file) > 0):
        return
    with open(fasta_file,"w") as fasta_output:
        url = "https://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=fastachain&compression=NO&structureId=%s&chainId=%s"%(pdb_id, chain)
        try:
            handle = urllib.request.urlopen(url)
        except urllib.error.URLError as e:
            print(e.reason)

        fasta_output.write(handle.read().decode('utf-8'))
    fasta_output.close()

pdb_id = sys.argv[1]
chain = sys.argv[2]
get_fasta(pdb_id, chain)