
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
module load gcc
module load cuda
/scratch/work/chengg1/ont-guppy/bin/guppy_basecaller -i reads -s basecalls -c /scratch/work/chengg1/ont-guppy/data/dna_r9.4.1_450bps_hac.cfg --device cuda:0
```

![image](https://user-images.githubusercontent.com/85612159/201746065-bb75e32b-cebb-47cc-a423-26fd8fbb96ca.png)

```
--fast5_out                           Choice of whether to do fast5 output.
-r [ --recursive ]                    Search for input files recursively.
--disable_pings                       Disable the transmission of telemetry pings.

```

## Config
```
guppy_basecaller --print_workflows
```

| flowcell     | kit            | barcoding     | config_name           |   model version        |
|  :---:       |     :---:      |    :---:      |  :---:                |    :---:               |
|FLO-FLG001    | SQK-RNA001     |               | rna_r9.4.1_70bps_hac  |         2020-09-07_rna_r9.4.1_minion_256_8f8fc47b  |
|FLO-FLG001    | SQK-RNA002     |               |rna_r9.4.1_70bps_hac   |        2020-09-07_rna_r9.4.1_minion_256_8f8fc47b   |
|FLO-MIN106    | SQK-RNA001     |               |rna_r9.4.1_70bps_hac   |        2020-09-07_rna_r9.4.1_minion_256_8f8fc47b   |
|FLO-MIN106    | SQK-RNA002     |               |rna_r9.4.1_70bps_hac   |        2020-09-07_rna_r9.4.1_minion_256_8f8fc47b   |
|FLO-MINSP6    | SQK-RNA001     |               |rna_r9.4.1_70bps_hac   |        2020-09-07_rna_r9.4.1_minion_256_8f8fc47b   |
|FLO-MINSP6    | SQK-RNA002     |               |rna_r9.4.1_70bps_hac   |        2020-09-07_rna_r9.4.1_minion_256_8f8fc47b   |
|FLO-MIN107    | SQK-RNA001     |               |rna_r9.4.1_70bps_hac   |        2020-09-07_rna_r9.4.1_minion_256_8f8fc47b   |
|FLO-MIN107    | SQK-RNA002     |               |rna_r9.4.1_70bps_hac   |        2020-09-07_rna_r9.4.1_minion_256_8f8fc47b   |


##  Reference
1. https://timkahlke.github.io/LongRead_tutorials/BS_G.html
2. https://denbi-nanopore-training-course.readthedocs.io/en/latest/basecalling/basecalling_1.html



