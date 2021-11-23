import os
import glob

# set filepath to data
train_path = "./data/train/annotations/"
valid_path = "./data/valid/annotations/"
unnecessary_labels = ["aro.npy","lnd.npy","val.npy"]

# delete all unnecessary training labels
deleted_count = 0
for label in unnecessary_labels:
    for filename in glob.glob(train_path + "*" + label):
        os.remove(filename) 
        deleted_count += 1
        if deleted_count % 1000 == 0:
            print("%d unnecessary training label files deleted so far"%deleted_count)
print("%d unnecessary training label files deleted in total"%deleted_count)

# delete all unnecessary validation labels
deleted_count = 0
for label in unnecessary_labels:
    for filename in glob.glob(valid_path + "*" + label):
        os.remove(filename) 
        deleted_count += 1
        if deleted_count % 1000 == 0:
            print("%d unnecessary validation label files deleted so far"%deleted_count)
print("%d unnecessary validation label files deleted in total"%deleted_count)