# Nanopore Data Process
This blog introduces the Nanopore data processing including reading data from fast5, fastq or fasta files, the process of Guppy, Tombo, Nanopolish and so on.


## 1. Software Installation



## 2. Nanopolish eventalign

```
nanopolish eventalign \
    --reads reads.fasta \
    --bam reads-ref.sorted.bam \
    --signal-index \
    --genome ref.fa \
    --summary summary.txt \
    --scale-events > eventalign.txt
```
## 3. seqkit（根据起始位置从基因组中提取序列）

```
conda install -c bioconda seqkit
seqkit subseq --bed gencode_lncrna.bed -o test.fa GRCh38.primary_assembly.genome.fa
```

.bed file contains three columns (using \t to split):
```
chrom chrom_start_pos chrom_end_pos 
```
因为没有指定正负链，所以这个命令总是提取的是在正链上的基因。如果在负链上，还需要反转互补。

还需要注意.bed文件和输出test.fa（起始位置需要加1）的不同：
```
 .bed            10	114432066	114432466
 .fa            >10_114432067-114432466:. 
```
Referrence:  https://www.jianshu.com/p/11b8804e570d
