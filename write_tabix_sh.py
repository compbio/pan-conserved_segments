#!/usr/bin/env python

import os

# bed_input = 'IGFN1_exon.bed'  # input file name
bed_input = input("enter name of your input: ")  # input file name
#search_winow = 2000
search_winow = int(input("enter search window size (recommended: 2000): "))
tabix_file_loc = input("enter the directory where tabix files are: ")
#tabix_file_loc = '../../pst_matrix/pst_pos_hprc_by_chr/'

file_name = bed_input.split(".")[0]
fout = open(file_name + "_bedtools_" + str(search_winow) + ".sh", "w")

out_dir = "search_" + str(search_winow)
os.mkdir(out_dir)

with open(bed_input) as f:
    for lines in f:
        line = lines.rstrip().split("\t")
        # In input bed file, line[5] = gene name while line[9] = exon number
        target = line[5] + "-" + line[9]
        start_pos = int(line[1])
        start_search = line[0] + ":" + \
            str(start_pos - search_winow) + "-" + str(start_pos)
        end_pos = int(line[2])
        end_search = line[0] + ":" + \
            str(end_pos) + "-" + str(end_pos + search_winow)

        fout.write("tabix " + tabix_file_loc + line[0] + ".pst.hprc.bed.gz " +
                   start_search + " >./" + out_dir + "/" + target + ".start.bed" + "\n")
        fout.write("tabix " + tabix_file_loc + line[0] + ".pst.hprc.bed.gz " +
                   end_search + " >./" + out_dir + "/" + target + ".end.bed" + "\n")

fout.close()
