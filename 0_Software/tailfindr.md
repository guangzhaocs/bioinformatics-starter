
```
cd /scratch/work/chengg1/tailfindr_install
module load miniconda
module load gcc/9.3.0
conda create -n tailfindr python=3.8 r-base=4.3
source activate tailfindr
```

```
pip install pyvbz-1.0.1-cp38-cp38-linux_x86_64.whl
conda install h5py
conda install -c bioconda r-tailfindr
```

```
library(tailfindr)
df <- find_tails(fast5_dir = 'fast5',
                 save_dir = 'tailfindr',
                 basecall_group = 'NanapolishEvent',
                 csv_filename = 'rna_tails.csv',
                 num_cores = 2)
```

```
df <- find_tails(fast5_dir = system.file('extdata', 'rna', package = 'tailfindr'),
                 save_dir = 'tailfindr',
                 csv_filename = 'rna_tails.csv',
                 num_cores = 2)
```
