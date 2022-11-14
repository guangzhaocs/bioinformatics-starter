
## Install

### CPU Version
```
https://mirror.oxfordnanoportal.com/software/analysis/ont-guppy-cpu-5.0.11-win64.msi
```

```
wget https://mirror.oxfordnanoportal.com/software/analysis/ont-guppy-cpu_6.0.1_linux64.tar.gz
tar -zvxf ont-guppy-cpu_6.0.1_linux64.tar.gz
cd ont-guppy-cpu
bin/guppy_basecaller --version
# or
/scratch/work/chengg1/ont-guppy-cpu/bin/guppy_basecaller --version
```
Guppy Basecalling Software, (C) Oxford Nanopore Technologies, Limited. Version 6.0.1+652ffd1


### GPU Version
```
wget https://mirror.oxfordnanoportal.com/software/analysis/ont-guppy_6.0.1_linux64.tar.gz
tar -zvxf ont-guppy_6.0.1_linux64.tar.gz

module load gcc
module load cuda
cd ont-guppy-cpu
bin/guppy_basecaller --version
```
Guppy Basecalling Software, (C) Oxford Nanopore Technologies, Limited. Version 6.0.1+652ffd1

## Usage


### Demo 1: Taiyaki Walk-through

```
cd /scratch/cs/nanopore/chengg1/base_calling/dataset/taiyaki_walkthrough
```

```
/scratch/work/chengg1/ont-guppy-cpu/bin/guppy_basecaller -i reads -s basecalls -c /scratch/work/chengg1/ont-guppy-cpu/data/dna_r9.4.1_450bps_hac.cfg
```

```
/scratch/work/chengg1/ont-guppy/bin/guppy_basecaller -i reads -s cudabasecalls -c /scratch/work/chengg1/ont-guppy/data/dna_r9.4.1_450bps_hac.cfg --device cuda:0
```

![image](https://user-images.githubusercontent.com/85612159/201744916-692fe68f-e150-4253-ad5d-5b9a34352ac5.png)


