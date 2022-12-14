# pan-conserved_segment tag (PST)

We developed a very efficient k-mer indexing strategy that allows to examine the properties of k-mers (i.e. uniquness) across the genome quickly.
We identified a notable type of 31-mers, pan-conserved 31-mers, after indexing 94 haploid high-quality haploid assemblies from  47 individuals with diverse backgrounds by Human Pangenome Reference Consortium (HPRC, https://humanpangenome.org/).
Pan-conserved 31-mers are unique in each assembly and present in all assemblies. Most (98.7%) of pan-conserved 31-mers are consecutive in positions based on GRCh38 and these consecutive overlapping 31-mers define longer segments of sequence that were present across all haploid assemblies – we refer to these extended sequences as pan-conserved segment tags (PSTs)
![image](https://user-images.githubusercontent.com/1683615/204896720-821558ef-0a61-4709-9be1-aded071eecac.png)

All pan-conserved 31-mers can be downloaded in bed format from https://dna-discovery.stanford.edu/publicmaterial/datasets/pangenome

Pan-conserved tag segments provided an informative set of universally conserved sequences.  Examining the intervals between pairs of these segments identified highly conserved segments of the genome versus ones that have structurally related polymorphisms. 
![image](https://user-images.githubusercontent.com/1683615/204897781-07b2f8a4-c299-4951-bbcb-d77aae614bd2.png)

# k-mer SV plots
We identified 60,763 polymorphic invervals and use the constituent 31-mers of SVs to visualize the structure of different classes of SVs including insertions, deletions, duplications, inversion and more complex rearrangements. This process involved using a simple dot matrix plot with the two axis representing the GRCh38 and the specific haploid assembly. We plotted the position of the 31-mers that spanned the divergent interval.

Move to the "test" directory and run the following command:
for file in *merged.txt; do ../make_kmer_plot_query.R $file; done

There are total of 6 input files for 6 different types of SVs (Figure 4 in our preprint: https://www.biorxiv.org/content/10.1101/2022.10.06.511239v2)

![image](https://user-images.githubusercontent.com/1683615/208243200-5f493287-e7ac-4376-b518-5eda620db112.png)
