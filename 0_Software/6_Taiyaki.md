# Taiyaki


```
# creat conda env
conda create -n taiyaki_env python=3.7
source activate taiyaki_env

# Download and unpack training data (approx. 10GB)
wget  https://s3-eu-west-1.amazonaws.com/ont-research/taiyaki_walkthrough.tar.gz
tar zxvf taiyaki_walkthrough.tar.gz
cd taiyaki_walkthrough

# Obtain and install Taiyaki
git clone https://github.com/nanoporetech/taiyaki
cd taiyaki
pip install -r requirements.txt
python setup.py install
python setup.py develop
source venv/bin/activate
cd ..


python taiyaki/misc/upgrade_model.py pretrained/r941_dna_minion.checkpoint
 
```

## Usage

```
cd /scratch/cs/nanopore/chengg1/base_calling/dataset/taiyaki_walkthrough
cd taiyaki && source venv/bin/activate && cd ..
sbatch map.sh
```
