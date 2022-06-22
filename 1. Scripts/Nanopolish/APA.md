


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
bedtools bamtobed -bed12 -split -i origin_download_fastq_bam_filter/HEK293T-Mettl3-KO-rep1.bam > origin_download_fastq_bam_filter_to_bed/KO-rep1.extract.bed12
```
bed12 format (https://bedtools.readthedocs.io/en/latest/content/general-usage.html): 
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| chrom | start | end | name | score | strand | thickStart | thickEnd | itemRGB | blockCount | blockSizes| blockStarts |


Examples in `KO-rep1.extract.bed12` (line 21-30):
```
1  186963  188245  3e590b49-2735-46ad-bf9c-e2ab39c9c8c1    34    -    186963  188245  255,0,0   3    324,198,116     0,416,1166
1  186968  188577  4ab27082-5ff4-406d-93dd-75e1f47f59a9    6     -    186968  188577  255,0,0   5    319,202,136,137,139     0,407,786,1161,1470
1  186968  195917  dbc150c4-4e46-4b7e-acbd-341312d26d12    47    -    186968  195917  255,0,0   7    319,198,136,137,146,102,655     0,411,786,1161,1470,1822,8294
1  186974  195419  5135f71c-246c-49fa-a277-6843b8cb65a9    45    -    186974  195419  255,0,0   5    313,198,137,146,157     0,405,1155,1464,8288
1  294876  296718  ed24c30c-40d4-4060-acb8-c1533faceee9    12    -    294876  296718  255,0,0   1    1842    0
1  629649  629977  7dde27aa-6110-4f80-98b6-44a880cebe88    11    +    629649  629977  255,0,0   1    328     0
1  629649  630001  5d0efd71-5d81-44bf-b65d-3dd3172a0870    9     +    629649  630001  255,0,0   1    352     0
1  629651  689958  a0990902-ef61-42d8-9405-5c8c7103b543    40    +    629651  689958  255,0,0   3    321,101,17      0,774,60290
1  629652  630206  050ef887-e254-479d-bae4-d66c5fe945ee    11    +    629652  630206  255,0,0   1    554     0
1  629652  630476  43e706ae-c766-4a55-a32f-55dfba282570    7     +    629652  630476  255,0,0   1    824     0
```

## Step 4: bedToGenePred
Convert the relative position to absolute position. 

`bedToGenePred` source code : https://github.com/ENCODE-DCC/kentUtils/blob/master/src/utils/bedToGenePred/bedToGenePred
```
cd ..
bedToGenePred origin_download_fastq_bam_filter_to_bed/KO-rep1.extract.bed12 KO-rep1.extract.bed12.pred
```
Examples in `KO-rep1.extract.bed12.pred` (line 21-30):
```
3e590b49-2735-46ad-bf9c-e2ab39c9c8c1    1    -    186963  188245  186963  188245    3       186963,187379,188129,   187287,187577,188245,
4ab27082-5ff4-406d-93dd-75e1f47f59a9    1    -    186968  188577  186968  188577    5       186968,187375,187754,188129,188438,     187287,187577,187890,188266,188577,
dbc150c4-4e46-4b7e-acbd-341312d26d12    1    -    186968  195917  186968  195917    7       186968,187379,187754,188129,188438,188790,195262, 187287,187577,187890,188266,188584,188892,195917,
5135f71c-246c-49fa-a277-6843b8cb65a9    1    -    186974  195419  186974  195419    5       186974,187379,188129,188438,195262,     187287,187577,188266,188584,195419,
ed24c30c-40d4-4060-acb8-c1533faceee9    1    -    294876  296718  294876  296718    1       294876,   296718,
7dde27aa-6110-4f80-98b6-44a880cebe88    1    +    629649  629977  629649  629977    1       629649,   629977,
5d0efd71-5d81-44bf-b65d-3dd3172a0870    1    +    629649  630001  629649  630001    1       629649,   630001,
a0990902-ef61-42d8-9405-5c8c7103b543    1    +    629651  689958  629651  689958    3       629651,630425,689941,   629972,630526,689958,
050ef887-e254-479d-bae4-d66c5fe945ee    1    +    629652  630206  629652  630206    1       629652,   630206,
43e706ae-c766-4a55-a32f-55dfba282570    1    +    629652  630476  629652  630476    1       629652,   630476,
```

## Step 5: genePredToGtf

### Step 5.1: genePredToGtf
 Convert genePred table or file to gtf.
```
genePredToGtf "file" KO-rep1.extract.bed12.pred KO-rep1.out.gtf
```

Examples in `KO-rep1.out.gtf`:
```
1       KO-rep1.extract.bed12.pred      transcript      186975  195419  .       -       .       gene_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; transcript_id "5135f71c-246c-49fa-a277-6843b8cb65a9";
1       KO-rep1.extract.bed12.pred      exon    186975  187287  .       -       .       gene_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; transcript_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; exon_number "1"; exon_id "5135f71c-246c-49fa-a277-6843b8cb65a9.1";
1       KO-rep1.extract.bed12.pred      CDS     186978  187287  .       -       1       gene_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; transcript_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; exon_number "1"; exon_id "5135f71c-246c-49fa-a277-6843b8cb65a9.1";
1       KO-rep1.extract.bed12.pred      exon    187380  187577  .       -       .       gene_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; transcript_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; exon_number "2"; exon_id "5135f71c-246c-49fa-a277-6843b8cb65a9.2";
1       KO-rep1.extract.bed12.pred      CDS     187380  187577  .       -       1       gene_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; transcript_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; exon_number "2"; exon_id "5135f71c-246c-49fa-a277-6843b8cb65a9.2";
1       KO-rep1.extract.bed12.pred      exon    188130  188266  .       -       .       gene_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; transcript_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; exon_number "3"; exon_id "5135f71c-246c-49fa-a277-6843b8cb65a9.3";
1       KO-rep1.extract.bed12.pred      CDS     188130  188266  .       -       0       gene_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; transcript_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; exon_number "3"; exon_id "5135f71c-246c-49fa-a277-6843b8cb65a9.3";
1       KO-rep1.extract.bed12.pred      exon    188439  188584  .       -       .       gene_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; transcript_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; exon_number "4"; exon_id "5135f71c-246c-49fa-a277-6843b8cb65a9.4";
1       KO-rep1.extract.bed12.pred      CDS     188439  188584  .       -       2       gene_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; transcript_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; exon_number "4"; exon_id "5135f71c-246c-49fa-a277-6843b8cb65a9.4";
1       KO-rep1.extract.bed12.pred      exon    195263  195419  .       -       .       gene_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; transcript_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; exon_number "5"; exon_id "5135f71c-246c-49fa-a277-6843b8cb65a9.5";
1       KO-rep1.extract.bed12.pred      CDS     195263  195419  .       -       0       gene_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; transcript_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; exon_number "5"; exon_id "5135f71c-246c-49fa-a277-6843b8cb65a9.5";
1       KO-rep1.extract.bed12.pred      start_codon     195417  195419  .       -       0       gene_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; transcript_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; exon_number "5"; exon_id "5135f71c-246c-49fa-a277-6843b8cb65a9.5";
1       KO-rep1.extract.bed12.pred      stop_codon      186975  186977  .       -       0       gene_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; transcript_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; exon_number "1"; exon_id "5135f71c-246c-49fa-a277-6843b8cb65a9.1";
1       KO-rep1.extract.bed12.pred      transcript      294877  296718  .       -       .       gene_id "ed24c30c-40d4-4060-acb8-c1533faceee9"; transcript_id "ed24c30c-40d4-4060-acb8-c1533faceee9";
1       KO-rep1.extract.bed12.pred      exon    294877  296718  .       -       .       gene_id "ed24c30c-40d4-4060-acb8-c1533faceee9"; transcript_id "ed24c30c-40d4-4060-acb8-c1533faceee9"; exon_number "1"; exon_id "ed24c30c-40d4-4060-acb8-c1533faceee9.1";
1       KO-rep1.extract.bed12.pred      CDS     294880  296718  .       -       0       gene_id "ed24c30c-40d4-4060-acb8-c1533faceee9"; transcript_id "ed24c30c-40d4-4060-acb8-c1533faceee9"; exon_number "1"; exon_id "ed24c30c-40d4-4060-acb8-c1533faceee9.1";
1       KO-rep1.extract.bed12.pred      start_codon     296716  296718  .       -       0       gene_id "ed24c30c-40d4-4060-acb8-c1533faceee9"; transcript_id "ed24c30c-40d4-4060-acb8-c1533faceee9"; exon_number "1"; exon_id "ed24c30c-40d4-4060-acb8-c1533faceee9.1";
1       KO-rep1.extract.bed12.pred      stop_codon      294877  294879  .       -       0       gene_id "ed24c30c-40d4-4060-acb8-c1533faceee9"; transcript_id "ed24c30c-40d4-4060-acb8-c1533faceee9"; exon_number "1"; exon_id "ed24c30c-40d4-4060-acb8-c1533faceee9.1";
1       KO-rep1.extract.bed12.pred      transcript      629650  629977  .       +       .       gene_id "7dde27aa-6110-4f80-98b6-44a880cebe88"; transcript_id "7dde27aa-6110-4f80-98b6-44a880cebe88";
1       KO-rep1.extract.bed12.pred      exon    629650  629977  .       +       .       gene_id "7dde27aa-6110-4f80-98b6-44a880cebe88"; transcript_id "7dde27aa-6110-4f80-98b6-44a880cebe88"; exon_number "1"; exon_id "7dde27aa-6110-4f80-98b6-44a880cebe88.1";
1       KO-rep1.extract.bed12.pred      CDS     629650  629977  .       +       0       gene_id "7dde27aa-6110-4f80-98b6-44a880cebe88"; transcript_id "7dde27aa-6110-4f80-98b6-44a880cebe88"; exon_number "1"; exon_id "7dde27aa-6110-4f80-98b6-44a880cebe88.1";
1       KO-rep1.extract.bed12.pred      start_codon     629650  629652  .       +       0       gene_id "7dde27aa-6110-4f80-98b6-44a880cebe88"; transcript_id "7dde27aa-6110-4f80-98b6-44a880cebe88"; exon_number "1"; exon_id "7dde27aa-6110-4f80-98b6-44a880cebe88.1";
```

### Step 5.2: filter gtf
```
cat KO-rep1.out.gtf|awk -F"\t" '{if($3=="transcript"){print $0}}' > KO-rep1.out2.gtf && rm KO-rep1.out.gtf
```
Examples in `KO-rep1.out2.gtf`:
```
1       KO-rep1.extract.bed12.pred      transcript      186964  188245  .       -       .       gene_id "3e590b49-2735-46ad-bf9c-e2ab39c9c8c1"; transcript_id "3e590b49-2735-46ad-bf9c-e2ab39c9c8c1";
1       KO-rep1.extract.bed12.pred      transcript      186969  188577  .       -       .       gene_id "4ab27082-5ff4-406d-93dd-75e1f47f59a9"; transcript_id "4ab27082-5ff4-406d-93dd-75e1f47f59a9";
1       KO-rep1.extract.bed12.pred      transcript      186969  195917  .       -       .       gene_id "dbc150c4-4e46-4b7e-acbd-341312d26d12"; transcript_id "dbc150c4-4e46-4b7e-acbd-341312d26d12";
1       KO-rep1.extract.bed12.pred      transcript      186975  195419  .       -       .       gene_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; transcript_id "5135f71c-246c-49fa-a277-6843b8cb65a9";
1       KO-rep1.extract.bed12.pred      transcript      294877  296718  .       -       .       gene_id "ed24c30c-40d4-4060-acb8-c1533faceee9"; transcript_id "ed24c30c-40d4-4060-acb8-c1533faceee9";
1       KO-rep1.extract.bed12.pred      transcript      629650  629977  .       +       .       gene_id "7dde27aa-6110-4f80-98b6-44a880cebe88"; transcript_id "7dde27aa-6110-4f80-98b6-44a880cebe88";
1       KO-rep1.extract.bed12.pred      transcript      629650  630001  .       +       .       gene_id "5d0efd71-5d81-44bf-b65d-3dd3172a0870"; transcript_id "5d0efd71-5d81-44bf-b65d-3dd3172a0870";
1       KO-rep1.extract.bed12.pred      transcript      629652  689958  .       +       .       gene_id "a0990902-ef61-42d8-9405-5c8c7103b543"; transcript_id "a0990902-ef61-42d8-9405-5c8c7103b543";
1       KO-rep1.extract.bed12.pred      transcript      629653  630206  .       +       .       gene_id "050ef887-e254-479d-bae4-d66c5fe945ee"; transcript_id "050ef887-e254-479d-bae4-d66c5fe945ee";
1       KO-rep1.extract.bed12.pred      transcript      629653  630476  .       +       .       gene_id "43e706ae-c766-4a55-a32f-55dfba282570"; transcript_id "43e706ae-c766-4a55-a32f-55dfba282570";
```

## Step 6: extract the last site
```
cat KO-rep1.out2.gtf| awk -F "[\t;]" '{if($7=="+"){print $1"\t"$5"\t"$9}else{print $1"\t"$4"\t"$9}}' |sed 's/gene_id//g' |sed 's/"//g' > KO-rep1_pAsite_gene.txt
```

Examples in `KO-rep1_pAsite_gene.txt`:
```
1       186964   3e590b49-2735-46ad-bf9c-e2ab39c9c8c1
1       186969   4ab27082-5ff4-406d-93dd-75e1f47f59a9
1       186969   dbc150c4-4e46-4b7e-acbd-341312d26d12
1       186975   5135f71c-246c-49fa-a277-6843b8cb65a9
1       294877   ed24c30c-40d4-4060-acb8-c1533faceee9
1       629977   7dde27aa-6110-4f80-98b6-44a880cebe88
1       630001   5d0efd71-5d81-44bf-b65d-3dd3172a0870
1       689958   a0990902-ef61-42d8-9405-5c8c7103b543
1       630206   050ef887-e254-479d-bae4-d66c5fe945ee
1       630476   43e706ae-c766-4a55-a32f-55dfba282570
```


## Step 7: change vcf name

```
bash path_to_script/change_vcf_name.sh a KO-rep1.out2.gtf KO-rep1.pA.gtf && rm KO-rep1.out2.gtf
```
Examples in `KO-rep1.pA.gtf`:
```
chr1    stdin   transcript      186964  188245  .       -       .       gene_id "3e590b49-2735-46ad-bf9c-e2ab39c9c8c1"; transcript_id "3e590b49-2735-46ad-bf9c-e2ab39c9c8c1";
chr1    stdin   transcript      186969  188577  .       -       .       gene_id "4ab27082-5ff4-406d-93dd-75e1f47f59a9"; transcript_id "4ab27082-5ff4-406d-93dd-75e1f47f59a9";
chr1    stdin   transcript      186969  195917  .       -       .       gene_id "dbc150c4-4e46-4b7e-acbd-341312d26d12"; transcript_id "dbc150c4-4e46-4b7e-acbd-341312d26d12";
chr1    stdin   transcript      186975  195419  .       -       .       gene_id "5135f71c-246c-49fa-a277-6843b8cb65a9"; transcript_id "5135f71c-246c-49fa-a277-6843b8cb65a9";
chr1    stdin   transcript      294877  296718  .       -       .       gene_id "ed24c30c-40d4-4060-acb8-c1533faceee9"; transcript_id "ed24c30c-40d4-4060-acb8-c1533faceee9";
chr1    stdin   transcript      629650  629977  .       +       .       gene_id "7dde27aa-6110-4f80-98b6-44a880cebe88"; transcript_id "7dde27aa-6110-4f80-98b6-44a880cebe88";
chr1    stdin   transcript      629650  630001  .       +       .       gene_id "5d0efd71-5d81-44bf-b65d-3dd3172a0870"; transcript_id "5d0efd71-5d81-44bf-b65d-3dd3172a0870";
chr1    stdin   transcript      629652  689958  .       +       .       gene_id "a0990902-ef61-42d8-9405-5c8c7103b543"; transcript_id "a0990902-ef61-42d8-9405-5c8c7103b543";
chr1    stdin   transcript      629653  630206  .       +       .       gene_id "050ef887-e254-479d-bae4-d66c5fe945ee"; transcript_id "050ef887-e254-479d-bae4-d66c5fe945ee";
chr1    stdin   transcript      629653  630476  .       +       .       gene_id "43e706ae-c766-4a55-a32f-55dfba282570"; transcript_id "43e706ae-c766-4a55-a32f-55dfba282570";

```
## Step 8: select 

```
cat KO-rep1.pA.gtf |awk -F "\t" '{if($7=="+"){print $1"\t"$5-1"\t"$5"\t"$2"\t"$3"\t"$7}else{print $1"\t"$4-1"\t"$4"\t"$2"\t"$3"\t"$7}}' > KO-rep1.pA.bed
```
Examples in `KO-rep1.pA.bed`:
```
chr1    186963  186964  stdin   transcript      -
chr1    186968  186969  stdin   transcript      -
chr1    186968  186969  stdin   transcript      -
chr1    186974  186975  stdin   transcript      -
chr1    294876  294877  stdin   transcript      -
chr1    629976  629977  stdin   transcript      +
chr1    630000  630001  stdin   transcript      +
chr1    689957  689958  stdin   transcript      +
chr1    630205  630206  stdin   transcript      +
chr1    630475  630476  stdin   transcript      +
```
## Step 9: sort
```
sort -k1,1 -k2,2n KO-rep1.pA.bed > KO-rep1.pA.sorted.bed
```
## Step 10: intersectBed
```
intersectBed -a pA.sorted.bed -b path_to_reference/metaplotR/hg38/hg38_annot.sorted.bed -sorted -wo -s > annot_pA.sorted.bed
```

Examples in `hg38_annot.sorted.bed`:
```
chr1    17368   17369   ENST00000619216.1|MIR6859-1|ncRNA|68    C       -
chr1    17369   17370   ENST00000619216.1|MIR6859-1|ncRNA|67    T       -
chr1    17370   17371   ENST00000619216.1|MIR6859-1|ncRNA|66    A       -
chr1    17371   17372   ENST00000619216.1|MIR6859-1|ncRNA|65    C       -
chr1    17372   17373   ENST00000619216.1|MIR6859-1|ncRNA|64    A       -
chr1    17373   17374   ENST00000619216.1|MIR6859-1|ncRNA|63    G       -
chr1    17374   17375   ENST00000619216.1|MIR6859-1|ncRNA|62    A       -
chr1    17375   17376   ENST00000619216.1|MIR6859-1|ncRNA|61    G       -
chr1    17376   17377   ENST00000619216.1|MIR6859-1|ncRNA|60    G       -
chr1    17377   17378   ENST00000619216.1|MIR6859-1|ncRNA|59    C       -
```

Exapmles in `pA.sorted.bed`:
```
chr1    14396   14397   stdin   transcript      -
chr1    14403   14404   stdin   transcript      -
chr1    14403   14404   stdin   transcript      -
chr1    14403   14404   stdin   transcript      -
chr1    14403   14404   stdin   transcript      -
chr1    14410   14411   stdin   transcript      -
chr1    16441   16442   stdin   transcript      -
chr1    16441   16442   stdin   transcript      -
chr1    16442   16443   stdin   transcript      -
chr1    16446   16447   stdin   transcript      -
```

Examples in `annot_pA.sorted.bed`:
```
chr1    810059  810060  stdin   transcript      +       chr1    810059  810060  ENST00000670700.1|LINC01409|ncRNA|1376  A       +       1
chr1    826205  826206  stdin   transcript      -       chr1    826205  826206  ENST00000473798.1|LINC00115|ncRNA|1317  T       -       1
chr1    841997  841998  stdin   transcript      +       chr1    841997  841998  ENST00000670780.1|LINC01128|ncRNA|1073  T       +       1
chr1    842000  842001  stdin   transcript      +       chr1    842000  842001  ENST00000670780.1|LINC01128|ncRNA|1076  A       +       1
chr1    842000  842001  stdin   transcript      +       chr1    842000  842001  ENST00000670780.1|LINC01128|ncRNA|1076  A       +       1
chr1    843590  843591  stdin   transcript      +       chr1    843590  843591  ENST00000670780.1|LINC01128|ncRNA|2666  A       +       1
chr1    844373  844374  stdin   transcript      +       chr1    844373  844374  ENST00000670780.1|LINC01128|ncRNA|3449  G       +       1
chr1    854084  854085  stdin   transcript      +       chr1    854084  854085  ENST00000445118.7|LINC01128|ncRNA|1255  C       +       1
chr1    854084  854085  stdin   transcript      +       chr1    854084  854085  ENST00000608189.5|LINC01128|ncRNA|1642  C       +       1
chr1    854084  854085  stdin   transcript      +       chr1    854084  854085  ENST00000609009.6|LINC01128|ncRNA|1632  C       +       1
```

## Step 11: rel_and_abs_dist_calc
```
perl path_to_metaPlotR/rel_and_abs_dist_calc.pl --bed annot_pA.sorted.bed --regions path_to_reference/metaplotR/hg38/region_sizes.txt > annot_pA.dist.measures.txt
```

## Step 12: delete
只保留3'UTR的pA位点,所以我们这里删掉pA位点的rel_location 0-2的位点。注意后续对应的位点也应该删除
```
cat annot_pA.dist.measures.txt|awk -F "\t" '{if($5 >= 2.0) print $0}' > annot_pA.dist.measures_only3utr.txt && rm annot_pA.dist.measures.txt
```

## Step 13: change vcf name
```
bash path_to_script/change_vcf_name.sh r annot_pA.dist.measures_only3utr.txt annot_pA.dist.measures_only3utr_nochr.txt 
```

