

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
Examples in KO-rep1.extract.bed12 (line 21-30):
```
1       186963  188245  3e590b49-2735-46ad-bf9c-e2ab39c9c8c1    34      -       186963  188245  255,0,0 3       324,198,116     0,416,1166
1       186968  188577  4ab27082-5ff4-406d-93dd-75e1f47f59a9    6       -       186968  188577  255,0,0 5       319,202,136,137,139     0,407,786,1161,1470
1       186968  195917  dbc150c4-4e46-4b7e-acbd-341312d26d12    47      -       186968  195917  255,0,0 7       319,198,136,137,146,102,655     0,411,786,1161,1470,1822,8294
1       186974  195419  5135f71c-246c-49fa-a277-6843b8cb65a9    45      -       186974  195419  255,0,0 5       313,198,137,146,157     0,405,1155,1464,8288
1       294876  296718  ed24c30c-40d4-4060-acb8-c1533faceee9    12      -       294876  296718  255,0,0 1       1842    0
1       629649  629977  7dde27aa-6110-4f80-98b6-44a880cebe88    11      +       629649  629977  255,0,0 1       328     0
1       629649  630001  5d0efd71-5d81-44bf-b65d-3dd3172a0870    9       +       629649  630001  255,0,0 1       352     0
1       629651  689958  a0990902-ef61-42d8-9405-5c8c7103b543    40      +       629651  689958  255,0,0 3       321,101,17      0,774,60290
1       629652  630206  050ef887-e254-479d-bae4-d66c5fe945ee    11      +       629652  630206  255,0,0 1       554     0
1       629652  630476  43e706ae-c766-4a55-a32f-55dfba282570    7       +       629652  630476  255,0,0 1       824     0
```
