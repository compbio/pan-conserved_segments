#!/usr/bin/env python

import glob
from collections import defaultdict

output_file = input("enter output file name: ")
search_window = int(input("enter size of search window: "))
fout = open(output_file, "w")
#fout = open("IGFN1_exon_interval-len-diff.txt", "w")

assm_list = ['chr', 'start', 'end', 'HG002.maternal', 'HG002.paternal', 'HG00438.maternal', 'HG00438.paternal', 'HG005.maternal', 'HG005.paternal', 'HG00621.maternal', 'HG00621.paternal', 'HG00673.maternal', 'HG00673.paternal', 'HG00733.maternal', 'HG00733.paternal', 'HG00735.maternal', 'HG00735.paternal', 'HG00741.maternal', 'HG00741.paternal', 'HG01071.maternal', 'HG01071.paternal', 'HG01106.maternal', 'HG01106.paternal', 'HG01109.maternal', 'HG01109.paternal', 'HG01123.maternal', 'HG01123.paternal', 'HG01175.maternal', 'HG01175.paternal', 'HG01243.maternal', 'HG01243.paternal', 'HG01258.maternal', 'HG01258.paternal', 'HG01358.maternal', 'HG01358.paternal', 'HG01361.maternal', 'HG01361.paternal', 'HG01891.maternal', 'HG01891.paternal', 'HG01928.maternal', 'HG01928.paternal', 'HG01952.maternal', 'HG01952.paternal', 'HG01978.maternal', 'HG01978.paternal', 'HG02055.maternal', 'HG02055.paternal', 'HG02080.maternal', 'HG02080.paternal',
             'HG02109.maternal', 'HG02109.paternal', 'HG02145.maternal', 'HG02145.paternal', 'HG02148.maternal', 'HG02148.paternal', 'HG02257.maternal', 'HG02257.paternal', 'HG02486.maternal', 'HG02486.paternal', 'HG02559.maternal', 'HG02559.paternal', 'HG02572.maternal', 'HG02572.paternal', 'HG02622.maternal', 'HG02622.paternal', 'HG02630.maternal', 'HG02630.paternal', 'HG02717.maternal', 'HG02717.paternal', 'HG02723.maternal', 'HG02723.paternal', 'HG02818.maternal', 'HG02818.paternal', 'HG02886.maternal', 'HG02886.paternal', 'HG03098.maternal', 'HG03098.paternal', 'HG03453.maternal', 'HG03453.paternal', 'HG03486.maternal', 'HG03486.paternal', 'HG03492.maternal', 'HG03492.paternal', 'HG03516.maternal', 'HG03516.paternal', 'HG03540.maternal', 'HG03540.paternal', 'HG03579.maternal', 'HG03579.paternal', 'NA18906.maternal', 'NA18906.paternal', 'NA19240.maternal', 'NA19240.paternal', 'NA20129.maternal', 'NA20129.paternal', 'NA21309.maternal', 'NA21309.paternal']

fout.write('ROI' + "\t" + 'grch38_dist')
for i in range(3, 97):
    fout.write("\t" + assm_list[i])
fout.write("\n")

output_dir = 'search_' + str(search_window)
files = glob.glob(output_dir + "/*.start.bed")
grch38_start = 0
grch38_end = 0
hprc_start = {}
hprc_end = {}

for file in sorted(files):
    target = file.split("/")[-1].split(".start")[0]
    with open(file) as f:
        for lines in f:
            pass
        last_line = lines.rstrip().split("\t")  # last line has PST closes to the start
        grch38_start = int(last_line[1])
        for i in range(3, 97):
            hprc_start[assm_list[i]] = int(
                last_line[i].split(":")[1].split("-")[0])

    with open(output_dir + "/" + target + ".end.bed") as f:
        # first line has PST closes to the end
        first_line = f.readline().rstrip().split("\t")
        grch38_end = int(first_line[1])
        for i in range(3, 97):
            hprc_end[assm_list[i]] = int(
                first_line[i].split(":")[1].split("-")[0])

    grch38_dist = grch38_end - grch38_start
    fout.write(target + "\t" + str(grch38_dist))
    for assm, pos in sorted(hprc_start.items()):
        start_pos = pos
        end_pos = hprc_end[assm]
        hprc_dist = abs(end_pos - start_pos)
        interval_len_diff = hprc_dist - grch38_dist
        fout.write("\t" + str(interval_len_diff))
    fout.write("\n")
fout.close()
