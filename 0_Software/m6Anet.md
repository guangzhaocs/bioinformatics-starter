

```
conda create -n m6anet_env python=3.7
pip install m6anet
```

```
m6anet dataprep --eventalign eventalign_demo.txt --out_dir m6anet_input --n_processes 4
```

```
m6anet inference --input_dir m6anet_input --out_dir m6anet_output  --n_processes 4 --num_iterations 1000
```
