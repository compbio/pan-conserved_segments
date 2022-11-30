# pan-conserved_segment tag (PST)

We developed a very efficient k-mer indexing strategy that allows to examine the properties of k-mers (i.e. uniquness) across the genome quickly.
We identified a notable type of 31-mers, pan-conserved 31-mers, after indexing 94 haploid high-quality haploid assemblies from  47 individuals with diverse backgrounds by Human Pangenome Reference Consortium (HPRC, https://humanpangenome.org/).
Pan-conserved 31-mers are unique in each assembly and present in all assemblies. Most (98.7%) of pan-conserved 31-mers are consecutive in positions based on GRCh38 and these consecutive overlapping 31-mers define longer segments of sequence that were present across all haploid assemblies – we refer to these extended sequences as pan-conserved segment tags (PSTs)
![image](https://user-images.githubusercontent.com/1683615/204896720-821558ef-0a61-4709-9be1-aded071eecac.png)

Pan-conserved tag segments provided an informative set of universally conserved sequences.  Examining the intervals between pairs of these segments identified highly conserved segments of the genome versus ones that have structurally related polymorphisms. 
