## File Structure
00download  
|---- KO  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - SRR_Acc_List.txt  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - SRR000001  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - ...  
|---- WT  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - SRR_Acc_List.txt  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - SRR000021  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - ...

  

## Download SRR_Acc_List.txt

```
add blank line in the txt file
```


## Download data

```
cd 00download/KO
/scratch/work/chengg1/sraToolkit/sratoolkit.3.0.0-centos_linux64/bin/prefetch-orig.3.0.0 -O output_dir --option-file SRR_Acc_List.txt
```


## unzip
```
for i in `cat SRR_Acc_List.txt`; do /scratch/work/chengg1/sraToolkit/sratoolkit.3.0.0-centos_linux64/bin/fastq-dump-orig.3.0.0 --split-files --gzip --outdir ${i}/ ${i}/${i}.sra && rm ${i}/${i}.sra; done
```

## rename
```
for i in `cat SRR_Acc_List.txt`; do (mv ${i}/${i}_1*.gz ${i}/${i}_S1_L001_I1_001.fastq.gz;mv ${i}/${i}_2*.gz ${i}/${i}_S1_L001_R1_001.fastq.gz;mv ${i}/${i}_3*.gz ${i}/${i}_S1_L001_R2_001.fastq.gz);done
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

```
@WT_3.1 D00796:330:CCCJVANXX:1:1104:1055:2158 length=26
CCNTTTCCACCTGGTGTTAATCCGTC
+WT_3.1 D00796:330:CCCJVANXX:1:1104:1055:2158 length=26
CC#<=FEGGGGGGGEGGGGGGGGAFF
@WT_3.2 D00796:330:CCCJVANXX:1:1104:1453:2198 length=26
TAAGCGTAGAAGATTCGACCGCCCAC
+WT_3.2 D00796:330:CCCJVANXX:1:1104:1453:2198 length=26
CCCCCGGGGGGGGGGGGGGGGGDGGE
@WT_3.3 D00796:330:CCCJVANXX:1:1104:1746:2153 length=26
CTGATCCTCTGCCAGGATAAGCTTCG
```
