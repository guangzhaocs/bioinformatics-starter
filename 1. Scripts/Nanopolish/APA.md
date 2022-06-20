

## Step 1: minimap2

```
minimap2 -ax splice -uf --MD --sam-hit-only --secondary=no -t 20 Homo_sapiens.GRCh38.dna.primary_assembly.fa origin_download_fastq/HEK293T-WT-rep1.fastq.gz | samtools sort -@ 20 | samtools view -b > origin_download_bam/HEK293T-WT-rep1.bam
```
## Step 2: filter
```
samtools view -h -q 5 -F 4 -F 256 -F 2048 -Sb origin_download_bam/HEK293T-Mettl3-KO-rep1.bam >  origin_download_filter_bam/HEK293T-Mettl3-KO-rep1.filter.bam
```
## Step 3: bamtobed
```
bedtools bamtobed -bed12 -split -i /scratch/cs/nanopore/nanopore_modification/xpore_dataset/origin_download_fastq_bam_filter/HEK293T-Mettl3-KO-rep1.bam > KO-rep1.extract.bed12
```

```
1       14396   18064   b0492d3c-fb21-4f50-80a9-3976d477e5b7    23      -       14396   18064   255,0,0 7       433,69,159,202,136,137,150      0,573,2210,2457,2836,3209,3518
1       14403   188585  7cadc59b-ec2f-42c4-a0e8-2b20c9a20266    30      -       14403   188585  255,0,0 8       426,69,153,159,202,136,137,147  0,171087,171913,172725,172972,173351,173726,174035
1       14403   20531   ca1c84a8-0f91-4ea8-ade6-ccbac8f857fe    10      -       14403   20531   255,0,0 10      426,69,152,159,202,137,147,102,54,1619     0,566,1392,2203,2450,3202,3511,3864,4097,4509
1       14403   24894   5bff7b07-ee3a-46dc-a4b3-a5730ef58cee    25      -       14403   24894   255,0,0 10      426,69,152,159,198,136,137,147,99,161      0,566,1392,2203,2454,2829,3202,3511,3864,10330
1       14403   187442  318206a0-c140-4101-8f3f-f5f4a4f15cfb    22      -       14403   187442  255,0,0 5       426,69,153,159,67       0,566,171913,172725,172972
1       14410   17963   7ee264e0-dbf2-46ca-a1f7-42fb6e33f132    6       -       14410   17963   255,0,0 8       419,69,152,159,198,136,137,49   0,559,1385,2196,2447,2822,3195,3504
1       16441   24894   a8dfb058-0783-4075-a9e4-60a76b39d892    8       -       16441   24894   255,0,0 7       324,198,136,137,147,112,157     0,416,791,1164,1473,1826,8296
1       16441   18370   ce561271-c509-4d68-86af-6cd9612b6fc6    8       -       16441   18370   255,0,0 6       324,198,136,137,147,103 0,416,791,1164,1473,1826
1       16442   24894   98098f28-7c3c-4f7b-a93c-80b463bd8458    8       -       16442   24894   255,0,0 6       323,198,137,147,99,157  0,415,1163,1472,1825,8295
1       16446   17697   4b7bfaec-ee7b-43dc-9cdf-723959754d12    7       -       16446   17697   255,0,0 4       319,198,136,92  0,411,786,1159
```
