# pan-conserved_segment tag (PST)
<img src="https://user-images.githubusercontent.com/1683615/204896720-821558ef-0a61-4709-9be1-aded071eecac.png" width="500" img align="right">
We developed a very efficient k-mer indexing strategy that allows to examine the properties of k-mers (i.e. uniquness) across the genome quickly.
We identified a notable type of 31-mers, pan-conserved 31-mers, after indexing 94 haploid high-quality haploid assemblies from  47 individuals with diverse backgrounds by Human Pangenome Reference Consortium (HPRC, https://humanpangenome.org/).
Pan-conserved 31-mers are unique in each assembly and present in all assemblies. Most (98.7%) of pan-conserved 31-mers are consecutive in positions based on GRCh38 and these consecutive overlapping 31-mers define longer segments of sequence that were present across all haploid assemblies – we refer to these extended sequences as pan-conserved segment tags (PSTs)
<br/>
<br/>
Pan-conserved tag segments provided an informative set of universally conserved sequences.  Examining the intervals between pairs of these segments identified highly conserved segments of the genome versus ones that have structurally related polymorphisms.
<p align="center">
<img src="https://user-images.githubusercontent.com/1683615/204897781-07b2f8a4-c299-4951-bbcb-d77aae614bd2.png" width="500">
</p>


All pan-conserved 31-mers can be downloaded in bed format, pan-conserved_seq.grch38.zip, from https://dna-discovery.stanford.edu/publicmaterial/datasets/pangenome
<br/>
<br/>
Here is the list of available files:
- polymorphic_intervals.50.grch38.bed: Each row represents an interval and 13 columns in this file (see the below image)
![image](https://user-images.githubusercontent.com/1683615/228391002-b8f1ae98-c425-43a5-a5f1-ebc39daf2e1b.png)
An interval (10052 bp) from 844891 to 854943 on chr1 on GRCh38 has the same lenght on 91 HPRC haploid assemblies. However, 3 of HPRC haploid assemblies have different interval lenghts; HG02080.paternal (345 bp shorter), HG02630.maternal (292 bp longer), HG03516.paternal (50 bp shoter) according to 12th and 13th column. 

- long_psts.2500.bed
  * long psts with size of >2,500 bp. 4th column shows the length of psts.
- the coordinates of PSTs across HPRC assemblies by chromosomes: chr*.pst.hprc.bed.gz (with tabix) under the directory of "pst_pos_hprc_by_chr"
  * Provide the coordinates of PSTs on GRCh38 and 94 HPRC assemblies
  * Use "tabix" to extract the PST within the genomic region of interest
   * For retrieving exon4 of TP53 (chr17:7,661,779-7,676,594), use the following command:
      ```
      tabix chr17.pst.hprc.bed.gz chr17:7,661,779-7,676,594
      ```
   | 1st col | chromosome on GRCh38 |
   | 2nd col | start pos on GRCh38 |
   | 3rd col | end pos on GRCh38 |
   | 4th col | position on HG002.maternal |
- Pan-conserved 31-mers and their GRCh38 coordinates:
  * pst-31mer.grch38.bed.gz
  * pst-31mer.grch38.bed.gz.tbi
- Pan-conserved sequences and their CHM13 coordinates: pan-conserved_seq.chm13.zip
- ll measured interval lengths between the selected pan-conserved sequences pairs: interval_length_matrix.zip

# Assessing the Presence of SVs on the _IGFN1_ Gene
Here we demonstrated how we can use PSTs to identify SVs in the gene of interes.
First, 

# k-mer SV plots
We identified 60,763 polymorphic invervals and use the constituent 31-mers of SVs to visualize the structure of different classes of SVs including insertions, deletions, duplications, inversion and more complex rearrangements. This process involved using a simple dot matrix plot with the two axis representing the GRCh38 and the specific haploid assembly. We plotted the position of the 31-mers that spanned the divergent interval.

Move to the "test" directory and run the following command:
for file in *merged.txt; do ../make_kmer_plot_query.R $file; done

There are total of 6 input files for 6 different types of SVs (Figure 4 in our preprint: https://www.biorxiv.org/content/10.1101/2022.10.06.511239v2)

<img src="https://user-images.githubusercontent.com/1683615/208243200-5f493287-e7ac-4376-b518-5eda620db112.png" width="750">
