

## Step 1: minimap2

```
minimap2 -ax splice -uf --MD --sam-hit-only --secondary=no  -t 20 Homo_sapiens.GRCh38.dna.primary_assembly.fa origin_download_fastq/HEK293T-WT-rep1.fastq.gz |  samtools sort -@ 20 | samtools view -b > origin_download_bam/HEK293T-WT-rep1.bam
```
