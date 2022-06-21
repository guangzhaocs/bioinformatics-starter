# metaPlotR

```
perl /scratch/work/chengg1/metaPlotR/make_annot_bed.pl --genomeDir hg38_chroms --genePred hg38_gencode_v38.genePred> hg38_annot.bed
sort -k1,1 -k2,2n hg38_annot.bed > hg38_annot.sorted.bed
perl /scratch/work/chengg1/metaPlotR/size_of_cds_utrs.pl --annot hg38_annot.sorted.bed > region_sizes.txt
```
