
# Installation

Attention: Do not use the Nanopolish Installation Tutorial and you must install samtools before nanopolish!
 
### 1. Creat anaconda environment

```
conda create -n nanopolish_env python=3.7
source activate nanopolish_env 
conda install -c bioconda samtools=1.9 --force-reinstall
samtools --version
conda install nanopolish
nanopolish --version
samtools --version
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
 
