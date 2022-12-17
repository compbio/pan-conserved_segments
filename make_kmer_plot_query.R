#!/usr/bin/env Rscript

# ***********************************************
# Title       : kmerSV plot
# Description : Visualize the structural variants of interest
# Author      : Created by Stephanie Greer and modified by HoJoon Lee  - https://github.com/compbio/pan-conserved_segments
# Date        : August 25, 2022
# ***********************************************

args = commandArgs(trailingOnly=TRUE)

library(ggplot2)
library(gridExtra)
library(stringr)
library(data.table)

file<-args[1]
file

coords = str_split(file, "\\.")[[1]][2]
coords

outfile<-gsub(pattern = "\\.txt$", "\\.png", file)
outfile

df<-fread(file, header=T, data.table=F)
head(df)

# reverse order so "+" appears before "-" in legend
levels(df$strand)
df$strand_test <- factor(df$strand_test, levels = c("+", "-"))
hprc_contig<-df$query_chr[1]
hprc_contig

chr <- df$ref_chr[1]
chr

A = ggplot() + 
  geom_point(data=df, aes(x=query_pos, y=ref_pos, colour=strand_test), size=1, alpha=0.5, shape=15) +
  xlab(paste("HPRC coordinate (",hprc_contig,")", sep="")) +
  ylab(paste("GRCh38 coordinate (",chr,")", sep="")) +
  theme_bw() +
  theme(panel.border = element_blank(), 
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(), 
        axis.line = element_line(colour = "black"),
        axis.ticks.length=unit(-0.15, "cm"),
        axis.text.x = element_text(margin=unit(c(0.3,0.5,0.5,0.5), "cm")), 
        axis.text.y = element_text(margin=unit(c(0.5,0.25,0.5,0.5), "cm")),
        axis.title=element_text(size=12),
        axis.title.y = element_text(margin = margin(t = 0, r = -10, b = 0, l = 0)),
        axis.title.x = element_text(margin = margin(t = -10, r = 0, b = 0, l = 0)),
        #text=element_text(family="Arial"),
        #legend.position = c(0.2, 0.9),
        legend.direction = "vertical",
        legend.title = element_blank(),
        legend.background = element_rect(linetype = 1, size = 0.3, colour = 1),
        legend.spacing.y = unit(0., 'cm'),
        #legend.text = element_text(size=14, family="Arial", margin = margin(r = 1, b=1, unit = "pt")),
        legend.key.size = unit(0.5, 'lines'),
        legend.position = "none") +
  guides(colour = guide_legend(override.aes = list(alpha = 1, size=3))) +
  scale_color_manual(values=c("#56B4E9", "#E69F00"), labels=c("+ strand match","\U2012 strand match")) #+
  #ylim(41523352,41650000)

ggsave(outfile,height=4,width=5, plot=A)
