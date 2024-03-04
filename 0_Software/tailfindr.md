
```
cd /scratch/work/chengg1/tailfindr
module load miniconda
conda create -n tailfindr python=3.8 r-base=4.3
```



```
pip install pyvbz-1.0.1-cp38-cp38-linux_x86_64.whl
```

```
module load r
conda install -c r r-devtools 
install.packages("devtools", lib="/scratch/work/chengg1/tailfindr")
```
