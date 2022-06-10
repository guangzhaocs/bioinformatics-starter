# Installation

### 1.Creat anaconda environment
`conda create -n tombo_env python=3.7`

### 2.Set up channels
 (https://bioconda.github.io/user/install.html#install-conda)
 
`conda config --add channels defaults`

`conda config --add channels bioconda`

`conda config --add channels conda-forge`

### 3.Install Tombo
`conda install -c bioconda ont-tombo`

### 4. Install ont_fast5_api
Install ont_fast5_api (https://pypi.org/project/ont-fast5-api/) for multi_to_single_fast5
`pip install ont-fast5-api`

### 5.Update NumPy  
In Tombo, the version of NumPy must be lower 1.20，otherwise it will have ValueError: cannot convert float NaN to integer.[https://github.com/nanoporetech/tombo/issues/319]
`conda install numpy=1.19.5`
