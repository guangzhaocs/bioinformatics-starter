## Download data

```
/scratch/work/chengg1/sraToolkit/sratoolkit.3.0.0-centos_linux64/bin/prefetch-orig.3.0.0 -O output_dir --option-file SRR_Acc_List.txt
```


## unzip
```
for i in `ls output_dir`; do /scratch/work/chengg1/sraToolkit/sratoolkit.3.0.0-centos_linux64/bin/fastq-dump-orig.3.0.0 --split-files --gzip --outdir ${i}/ ${i}/${i}.sra && rm ${i}/${i}.sra; done
```
