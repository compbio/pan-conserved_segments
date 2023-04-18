#!/usr/bin/env python

import os

bed_input = 'IGFN1_exon.bed'    ## input file name
search_winow = 100               ## 
tabix_file_loc = '../../pst_matrix/pst_pos_hprc_by_chr/'

file_name = bed_input.split(".")[0]
fout = open(file_name + "_bedtools.sh","w")
os.mkdir("search_" + search_winow)

with open(bed_input) as f:
  for lines in f:
    line = lines.rstrip().split("\t")
    target = line[5] + "-" + line[9]      ### In input bed file, line[5] = gene name while line[9] = exon number
    start_pos = int(line[1])
    start_search = line[0] + ":" + str(start_pos - search_winow) + "-" + str(start_pos)
    end_pos = int(line[2])
    end_search = line[0] + ":" + str(end_pos) + "-" + str(end_pos + search_winow)

    fout.write("tabix " + tabix_file_loc + line[0] + ".pst.hprc.bed.gz " + start_search + " >./intersect_bed/" + target + ".start.bed" + "\n")
    fout.write("tabix " + tabix_file_loc + line[0] + ".pst.hprc.bed.gz " + end_search + " >./intersect_bed/" + target + ".end.bed" + "\n")

fout.close()
