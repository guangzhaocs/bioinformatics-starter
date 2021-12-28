# -*- coding: utf-8 -*-
# @Time    : 2021/12/28 15:34
# @Author  : Guangzhao Cheng
# @FileName: combine_eventalign.py
import os
import numpy as np
from tqdm import tqdm
import argparse


def combine_eventalign(eventalign_file_name, combined_file_name=None, shift=2):
    """
    Combine the same kmers in eventalign file and write to a new file.

    Original file name:  eventalign.txt
    Combined file name:  eventalign_combine.txt

    Example:
    Original file:
    ================================================================================================================
    contig	position	reference_kmer	read_index	strand	event_index	event_level_mean ...	start_idx	end_idx
    ----------------------------------------------------------------------------------------------------------------
    gi|545778205|gb|U00096.3|:c514859-514401	3	ATGGAG	0	t	16538	98.58	...	81407	81411
    gi|545778205|gb|U00096.3|:c514859-514401	3	ATGGAG	0	t	16537	97.60	...	81403	81407
    gi|545778205|gb|U00096.3|:c514859-514401	3	ATGGAG	0	t	16536	104.00	...	81398	81403
    gi|545778205|gb|U00096.3|:c514859-514401	3	ATGGAG	0	t	16535	89.95	...	81392	81398
    ================================================================================================================

    After combining:
    =======================================================================================
    contig	read_index	position	trans_position	kmer	mean	start_idx	end_idx
    ---------------------------------------------------------------------------------------
    gi|545778205|gb|U00096.3|:c514859-514401	0	3	5	ATGGAG	97.53	81392	81411
    =======================================================================================

    trans_position = position + shift(default: 2)
    You can ignore the trans_position if you do not need it.
    """

    # creat the new file. If it exits, delete it !!!
    if not combined_file_name:
        combined_file_name = eventalign_file_name[:-4] + '_combine.txt'
    if os.path.exists(combined_file_name):
        os.remove(combined_file_name)
    print('* Remove the old eventalign_combine_file!')

    # read the header and the firt line of the original file.
    f = open(eventalign_file_name, "r")
    header = f.readline().strip().replace('\n', '').replace('\r', '').split('\t')
    column_num = len(header)
    assert header == ['contig', 'position', 'reference_kmer', 'read_index', 'strand', 'event_index', 'event_level_mean',
                      'event_stdv', 'event_length', 'model_kmer', 'model_mean', 'model_stdv', 'standardized_level',
                      'start_idx', 'end_idx']

    first_line = f.readline().strip().replace('\n', '').replace('\r', '').split('\t')
    assert len(first_line) == column_num
    print('* Creat the new eventalign_combine_file!')

    # parameters for current file
    curent_contig = first_line[0]
    curent_read_index = first_line[3]
    curent_kmer = first_line[2]
    curent_position_id = int(first_line[1])
    curent_position_start_idx = int(first_line[-2])
    curent_position_end_idx = int(first_line[-1])
    curent_kmer_list = [float(first_line[6])]
    f.close()

    print('* Start to processing ... ')
    num_lines = sum(1 for _ in open(eventalign_file_name, 'r'))
    with open(combined_file_name, 'a+') as writer_f:
        new_header = 'contig' + '\t' + 'read_index' + '\t' + 'position' + '\t' + 'trans_position' + '\t' + \
                     'kmer' + '\t' + 'mean' + '\t' + 'start_idx' + '\t' + 'end_idx' + '\t'
        writer_f.write(new_header + '\n')
        with open(eventalign_file_name, 'r') as f:
            for i, line in enumerate(tqdm(f, total=num_lines)):
                if i > 1:
                    line = line.strip().replace('\n', '').replace('\r', '').split('\t')

                    # hold current position
                    if curent_kmer == line[2] and curent_position_id == int(line[1]):

                        assert curent_contig == line[0]
                        assert curent_read_index == line[3]

                        # Firstly, make sure the direction
                        if curent_position_start_idx > int(line[-2]):
                            curent_position_start_idx = int(line[-2])
                        else:
                            curent_position_end_idx = int(line[-1])

                        # Secondly, update some parameters
                        curent_kmer_list.append(float(line[6]))

                    # a new position, wirte down the current kmer to the new file
                    else:
                        assert curent_position_end_idx >= curent_position_start_idx
                        mean = np.mean(np.array(curent_kmer_list))
                        mean = np.around(mean, decimals=2)
                        combined_kmer = curent_contig + '\t' + curent_read_index + '\t' + str(curent_position_id) \
                                        + '\t' + str(curent_position_id + shift) + '\t' + curent_kmer + '\t' + str(mean) \
                                        + '\t' + str(curent_position_start_idx) + '\t' + str(curent_position_end_idx) + '\t'
                        writer_f.write(combined_kmer + '\n')

                        # start to process a new position, update all parameters
                        curent_contig = line[0]
                        curent_read_index = line[3]
                        curent_kmer = line[2]
                        curent_position_id = int(line[1])
                        curent_position_start_idx = int(line[-2])
                        curent_position_end_idx = int(line[-1])
                        curent_kmer_list = [float(line[6])]

                    # the last line
                    if i == num_lines - 1:
                        assert curent_position_end_idx >= curent_position_start_idx
                        mean = np.mean(np.array(curent_kmer_list))
                        mean = np.around(mean, decimals=2)
                        combined_kmer = curent_contig + '\t' + curent_read_index + '\t' + str(curent_position_id) \
                                        + '\t' + str(curent_position_id + shift) + '\t' + curent_kmer + '\t' + str(mean) \
                                        + '\t' + str(curent_position_start_idx) + '\t' + str(
                            curent_position_end_idx) + '\t'
                        writer_f.write(combined_kmer + '\n')

                # if i == 10: break


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Combine the same kmers in eventalign file and write to a new file.')
    parser.add_argument('--eventalign-file-name', type=str, default='eventalign.txt')
    parser.add_argument('--combined-file-name', type=str, default=None)
    parser.add_argument('--shift', type=int, default=2)
    args = parser.parse_args()

    # root_dir = 'D://Nanopore_Data//Nanopolish_demo//ecoli_2kb_region//'
    # eventalign_file_name = root_dir + 'reads-ref.eventalign.txt'
    # args.eventalign_file_name = eventalign_file_name
    combine_eventalign(args.eventalign_file_name, args.combined_file_name, args.shift)
    print('* Already combined the eventalign file!')