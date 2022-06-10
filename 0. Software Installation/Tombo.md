# Installation


### 1. Creat anaconda environment
```
conda create -n tombo_env python=3.7
```
### 2. Set up channels
 (https://bioconda.github.io/user/install.html#install-conda)
```
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
```
### 3. Install Tombo
```
conda install -c bioconda ont-tombo
```
### 4. Install ont_fast5_api
Install ont_fast5_api (https://pypi.org/project/ont-fast5-api/) for multi_to_single_fast5
```
pip install ont-fast5-api
```
### 5. Update NumPy  
In Tombo, the version of NumPy must be lower 1.20，otherwise it will have ValueError: cannot convert float NaN to integer.(https://github.com/nanoporetech/tombo/issues/319)
```
conda install numpy=1.19.5
```

# Demo

Dataset: ` diaphragm_small.fast5 `

```
multi_to_single_fast5 --input_path multi_fast5/diaphragm_small.fast5  --save_path single_fast5_DNA --recursive -t 20
tombo resquiggle single_fast5_cDNA Mus_musculus.GRCm38.cdna.all.fa --overwrite --processes 10 --num-most-common-errors 0 --signal-matching-score 0
tombo plot genome_locations --fast5-basedirs single_fast5_cDNA/0 --genome-locations ENSMUST00000061618.8:3172
```

