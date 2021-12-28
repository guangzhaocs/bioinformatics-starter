# Nanopore Data Process
This blog introduces the Nanopore data processing including reading data from fast5, fastq or fasta files, the process of Guppy, Tombo, Nanopolish and so on.



```
nanopolish eventalign \
    --reads reads.fasta \
    --bam reads-ref.sorted.bam \
    --signal-index \
    --genome ref.fa \
    --summary summary.txt \
    --scale-events > eventalign.txt
```
