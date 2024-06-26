## single_to_multi_fast5
```
single_to_multi_fast5 --input_path single_fast5/ --save_path multi_fast5/ --filename_base $1 --batch_size 4000 --recursive; 
```

## multi_to_single_fast5
```
for i in `ls multi_fast5`;
do 
      multi_to_single_fast5 --input_path multi_fast5/${i}  --save_path single_fast5/ --recursive -t 20
done;
```

## pod5 to multi fast5
```
pod5 convert to_fast5 example.pod5 --output multi_fast5/
```

## multi fast5 to pod5
```
pod5 convert fast5 multi_fast5/*.fast5 --output multi_pod5/ --one-to-one multi_fast5/
```

## cram to multi fast5
```
ont2cram reverse_converter -i example.cram -o multi_fast5/
```

## Reference

- [ont_fast5_api](https://github.com/nanoporetech/ont_fast5_api)
- [pod5-file-format](https://pod5-file-format.readthedocs.io/en/0.1.21/docs/tools.html)
- [ont2cram](https://github.com/EGA-archive/ont2cram)
