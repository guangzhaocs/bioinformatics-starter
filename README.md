# Quickstart: Travel to Bioinformatics

This blog introduces the Bioinformatics Software Installation, the srcipts of Bioinformatics processing, and so on.


## 1. Software Installation

nanopolish[0. Software Installation/Nanopolish.md]


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
seqkit subseq --bed test.bed -o test.fa GRCh38.primary_assembly.genome.fa
```

`test.bed` file contains three columns (using `\t` to split):
```
chrom chrom_start_pos chrom_end_pos 
```
`test.bed` example:
```
3	134561560	134561960
5	176380171	176380571
17	68420614	68421014
```
因为没有指定正负链，所以这个命令总是提取的是在正链上的基因。如果在负链上，还需要反转互补。

还需要注意test.bed文件和输出test.fa（起始位置需要加1）的不同：

`test.fa` example:
```
>3_134561561-134561960:. 
AAATAAAAATAAACACCAAAGAGTTACTGTCATCTGAAGTAGCAGCTCTTTAAAAACATG...
>5_176380172-176380571:. 
CAAAGAAGAGACAGAGAAGGAGCAATCCAGGTTCATGTGCTGCATGAGCCTTTCATTTGC...
>17_68420615-68421014:. 
TCCCTCCTCCACGCCGACCCGAGAGCAGCTGAGCTGCGCTGGCTCTGGGCAGGGAGTGTG...
```
Referrence:  https://www.jianshu.com/p/11b8804e570d
