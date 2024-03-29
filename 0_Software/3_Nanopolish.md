
# Installation (test 2024.03.18)

Attention: Do not use the Nanopolish Installation Tutorial and you must install samtools before nanopolish!
 
### 1. Creat anaconda environment

```
conda create -n nanopolish2_env python=3.7
source activate nanopolish2_env 
```

### 2. Install samtools
```
conda install -c bioconda samtools=1.9 --force-reinstall
samtools --version
# samtools 1.9
# Using htslib 1.9
# Copyright (C) 2018 Genome Research Ltd.
```

### 3. Install nanopolish
```
conda install nanopolish
nanopolish --version
# nanopolish version 0.13.2
# Written by Jared Simpson.
# 
# Copyright 2015-2017 Ontario Institute for Cancer Research

samtools --version
# samtools 1.9
# Using htslib 1.9
# Copyright (C) 2018 Genome Research Ltd.

```
 
 # Usage
 
 ### Index
 
 [Nanopolish Tutorial](https://nanopolish.readthedocs.io/en/latest/manual.html#index)
 
 ```
 nanopolish index --directory=fast5_dir basecalled.fastq
 ```

fast5_dir   
|---- 0   
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - xxx_01.fast5  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - xxx_02.fast5  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - ...   
|---- 1   
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - xxx_01.fast5  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - xxx_02.fast5  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - ...  
  
  
Maybe `fast5_dir` has many subfolders. It would be OK to use `--directory=fast5_dir` in the command. The output of the command is as follows. So it would be better to run the command under the `fastq` file folder.
 
 ```
 basecalled.fastq    
 basecalled.fastq.index
 basecalled.fastq.index.fai
 basecalled.fastq.index.gzi
 basecalled.fastq.index.readdb
 ```
 # Attention
 
 The `summary.txt` and `eventalign.txt` maybe have more than one mapping result for each read.
 
