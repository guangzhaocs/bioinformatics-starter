### 00download
|- KO
|   - SRR_Acc_List.txt
|   - SRR1
|   - ...
|- WT
|   - SRR_Acc_List.txt
|   - SRR1
|   - ...
### 01cellranger
|- KO
|   - SRR_Acc_List.txt
|   - SRR1
|   - ...
|- WT
|   - SRR_Acc_List.txt
|   - SRR1
|   - ...


## Download SRR_Acc_List.txt

```
add blank line in the txt file
```



## Download data

```
/scratch/work/chengg1/sraToolkit/sratoolkit.3.0.0-centos_linux64/bin/prefetch-orig.3.0.0 -O output_dir --option-file SRR_Acc_List.txt
```


## unzip
```
for i in `ls output_dir`; do /scratch/work/chengg1/sraToolkit/sratoolkit.3.0.0-centos_linux64/bin/fastq-dump-orig.3.0.0 --split-files --gzip --outdir ${i}/ ${i}/${i}.sra && rm ${i}/${i}.sra; done
```

## rename
```
cat SRR_Acc_List.txt| while read i ;do (mv ${i}/${i}_1*.gz ${i}/${i}_S1_L001_I1_001.fastq.gz;mv ${i}/${i}_2*.gz ${i}/${i}_S1_L001_R1_001.fastq.gz;mv ${i}/${i}_3*.gz ${i}/${i}_S1_L001_R2_001.fastq.gz);done
```

## copy to cellranger floder
```
for i in `cat 00download/Ctrl/SRR_Acc_List.txt`; do cp 00download/Ctrl/${i}/* 01cellranger/Ctrl/fq/ ; done
```

## delate I1
```
ls|grep "I1"| xargs -P 1 -I {} rm {}
```

## sed 
```
for i in `ls|cut -d "_" -f 1 |uniq` ; do gunzip ${i}_S1_L001_R1_001.fastq.gz && sed -i s/$i/Ctrl/ ${i}_S1_L001_R1_001.fastq && gzip ${i}_S1_L001_R1_001.fastq; done
for i in `ls|cut -d "_" -f 1 |uniq` ; do gunzip ${i}_S1_L001_R2_001.fastq.gz && sed -i s/$i/Ctrl/ ${i}_S1_L001_R2_001.fastq && gzip ${i}_S1_L001_R2_001.fastq; done
```
