# Script to Cut Datasets

> **NOTE**: This script is for non-commercial research or educational use only.

Use this script to cut ImageNet and Pascal VOC datasets.

## Usage 

Download the script cut_dataset.py.

### Cut ImageNet

In a python console, run the following command after specifying the parameters:

```
python C:/Users/Downloads/cut_dataset.py \
--source_archive_dir=C:\Users\Work\imagenet.zip \
--output_size=10 \
--output_archive_dir=C:\Users\Work\subsets \
--dataset_type=imagenet
```
This command runs the script with the following arguments:

Parameter  |  Explanation
--|--
`--source_archive_dir=C:\Users\Work\imagenet.zip`  |  Full path to a downloaded archive
`--output_size=10` |  Number of images to be left in a smaller dataset
`--output_archive_dir=C:\Users\Work\subsets` | Full directory to the smaller dataset, excluding the name
`--dataset_type=imagenet`| Type of the source dataset

### Cut Pascal VOC

In a python console, run the following command after specifying the parameters:

```py
python C:/Users/Downloads/cut_dataset.py \
--source_archive_dir=C:\Users\Work\voc.tar.gz \
--output_size=10 \
--output_archive_dir=C:\Users\Work\subsets \
--dataset_type=voc 
```

This command runs the script with the following arguments:

Parameter  |  Explanation
--|--
`--source_archive_dir=C:\Users\Work\voc.tar.gz`  |  Full path to a downloaded archive
`--output_size=10` |  Number of images to be left in a smaller dataset
`--output_archive_dir=C:\Users\Work\subsets` | Full directory to the smaller dataset, excluding the name
`--dataset_type=voc`| Type of the source dataset
