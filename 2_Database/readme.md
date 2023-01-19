

# Download Data
```
nohup /scratch/work/chengg1/sraToolkit/sratoolkit.3.0.0-centos_linux64/bin/prefetch-orig.3.0.0 -O sra $(<SRR_Acc_List.txt) &
```

# Unzip
```
for i in `cat SRR_Acc_List.txt`; do /scratch/work/chengg1/sraToolkit/sratoolkit.3.0.0-centos_linux64/bin/fastq-dump-orig.3.0.0 --split-files --gzip --outdir ${i}/ ${i}/${i}.sra && rm ${i}/${i}.sra; done


cd sra
for i in `ls`; do /scratch/work/chengg1/sraToolkit/sratoolkit.3.0.0-centos_linux64/bin/fastq-dump-orig.3.0.0 --split-files --gzip --outdir ${i}/ ${i}/${i}.sra && rm ${i}/${i}.sra; done
```
