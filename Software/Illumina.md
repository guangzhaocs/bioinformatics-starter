## Illumina

10x Genomics的文库结构，根据碱基长度，就不难推测它们分别是R1（26bp：cell barcode和UMI序列）、R2（98bp：插入片段）和I1（8bp：index序列）.


## Download Dataset

### Install aspera(ascp)

Step 1:
```
conda install -y -c hcc aspera-cli
conda install -y -c bioconda sra-tools
```

Step 2:
```
ascp -h
```

Step 3:
```
which ascp
```
/scratch/work/chengg1/myconda/conda_envs/nanopolish_env/bin/ascp

Step 4:
```
ls /scratch/work/chengg1/myconda/conda_envs/nanopolish_env/etc/asperaweb_id_dsa.openssh
```
/scratch/work/chengg1/myconda/conda_envs/nanopolish_env/etc/asperaweb_id_dsa.openssh


## Reference

- Aspera下载安装使用[https://www.jianshu.com/p/fed19a8821eb]
- 使用ebi数据库直接下载fastq测序数据的改进脚本[https://mp.weixin.qq.com/s?__biz=MzAxMDkxODM1Ng==&mid=2247492889&idx=2&sn=bc2ef17a3b96a257fb692f73338c6b0f&scene=21#wechat_redirect]
