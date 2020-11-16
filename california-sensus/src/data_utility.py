""" 
Library containing useful auxiliary functions
Created by Y.Lin
"""

import os
import tarfile
import urllib
import numpy
import zlib

def get_data_from_url(src_url, dest_folder, dest_file_name):
    os.makedirs(dest_folder, exist_ok=True)
    dest = os.path.join(dest_folder, dest_file_name)
    urllib.request.urlretrieve(src_url, dest)

def extract_tarfile(tarfile_path, extracted_path):
    tar = tarfile.open(tarfile_path)
    tar.extractall(path=extracted_path)
    tar.close()

# implementation of single run split train test data
def split_train_test_single_run(data, ratio):
    # randomly permute a sequence of length 'data'
    random_unique_indices = numpy.random.permutation(len(data))
    split_size = int(len(data) * ratio)
    # all indices left of split size not inclusive
    train_indices = random_unique_indices[:split_size]
    # all indices after split size 
    test_indices = random_unique_indices[split_size:]
    # return left and right data of respective indices
    return data.iloc[train_indices], data.iloc[test_indices]

# implementation of multi-run split train test data that ensures test data is consistent across multiple
# run even as dataset 'updates', and no prev training data appear in test data
def split_train_test_multi_run(data, ratio, id_column):
    ids = data[id_column]
    # foreach id in the array, filter set of ids where the id converts to 64bit integer, masked to only 32 bit lsb, 
    test_set = ids.apply(lambda id: zlib.crc32(numpy.int64(id)) & 0xffffffff < ratio * 2 ** 32) 
    return data.loc[~test_set], data.loc[test_set]

def display_scores(scores):
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard deviation:", scores.std())