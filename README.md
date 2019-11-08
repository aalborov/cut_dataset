# Script to Cut Datasets

> **NOTE**: This script is for non-commercial research or educational use only.

Use this script to cut ImageNet and Pascal VOC datasets.

## Usage 

Download the script cut_dataset.py.

In a python console, run the following command after specifying the parameters:

```
python C:/Users/Downloads/cut_dataset.py \
--source_archive_dir=<full_path_to_source_archive> \
--first_image=<image_number>
--output_size=<number_of_images> \
--output_archive_dir=<path_to_output_archive> \
--dataset_type=imagenet
```
This command runs the script with the following arguments:

Parameter  |  Explanation
--|--
`--source_archive_dir` |  Full path to a downloaded archive including the name
`--first_image` |  Number of the image to start from (you might want to have subsets of different images for testing and validation)
`--output_size` |  Number of images to be left in a smaller dataset
`--output_archive_dir` | Full directory to the smaller dataset excluding the name
`--dataset_type`| Type of the source dataset (`imagenet` or `voc`)
