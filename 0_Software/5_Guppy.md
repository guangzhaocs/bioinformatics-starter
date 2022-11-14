
## Install

CPU Version:
```
https://mirror.oxfordnanoportal.com/software/analysis/ont-guppy-cpu-5.0.11-win64.msi
```

```
wget https://mirror.oxfordnanoportal.com/software/analysis/ont-guppy-cpu_6.0.1_linux64.tar.gz
tar -zvxf ont-guppy-cpu_6.0.1_linux64.tar.gz
cd ont-guppy-cpu
bin/guppy_basecaller --version

/scratch/work/chengg1/ont-guppy-cpu/bin/guppy_basecaller --version
```
Guppy Basecalling Software, (C) Oxford Nanopore Technologies, Limited. Version 6.0.1+652ffd1


GPU Version:
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
cd taiyaki_walkthrough
```

```
/home/chengg1/Install/ont-guppy-cpu/bin/guppy_basecaller -i reads -s basecalls -c /home/chengg1/Install/ont-guppy-cpu/data/dna_r9.4.1_450bps_hac.cfg
```

