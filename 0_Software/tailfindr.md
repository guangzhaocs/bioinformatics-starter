
```
cd /scratch/work/chengg1/tailfindr
module load miniconda
conda create -n tailfindr python=3.8 r-base=4.3
source activate tailfindr
```

```
pip install pyvbz-1.0.1-cp38-cp38-linux_x86_64.whl
conda install h5py
conda install -c r r-devtools 
```

```
R
devtools::install_url('https://cran.r-project.org/src/contrib/Archive/rbokeh/rbokeh_0.5.1.tar.gz', type = "source", dependencies = TRUE)
devtools::install_github("adnaniazi/tailfindr")
```
