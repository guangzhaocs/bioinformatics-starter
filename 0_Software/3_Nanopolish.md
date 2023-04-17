
# Installation

Attention: Do not use the Nanopolish Installation Tutorial and you must install samtools before nanopolish!
 
### 1. Creat anaconda environment

```
conda create -n nanopolish_env python=3.7
source activate nanopolish_env 
```

### 2. Install samtools
```
conda install -c bioconda samtools=1.9 --force-reinstall
samtools --version
```

### 3. Install nanopolish
```
conda install nanopolish
nanopolish --version
samtools --version
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
 
