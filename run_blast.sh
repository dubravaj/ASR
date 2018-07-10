#!/usr/bin/env bash

pdb_id=$1

./blastp -query $pdb_id'.fasta' -db nr -outfmt 5 -out $pdb_id'.xml' -max_target_seqs 250 -remote