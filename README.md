# Script to Cut Datasets

> **NOTE**: This script is for non-commercial research or educational use only.

Use this script to cut ImageNet, Pascal VOC, and Common Objects in Context(COCO) datasets.

## Usage 

Download the script `cut_dataset.py`.

### Cut ImageNet or Pascal VOC

In a Python console, run the following command after specifying the parameters:

```
python C:/Users/Downloads/cut_dataset.py \
--source_archive_dir=<full_path_to_source_archive> \
--output_size=<number_of_images> \
--output_archive_dir=<path_to_output_archive> \
--dataset_type=imagenet
--first_image=<image_number>
```
This command runs the script with the following arguments:

Parameter  |  Explanation
--|--
`--source_archive_dir=<full_path_to_source_archive>`  |  Full path to the downloaded archive including the name
`--output_size=<number_of_images>` |  Number of images to be left in a smaller dataset
`--output_archive_dir=<path_to_output_archive>` | Full directory to the smaller dataset excluding the name
`--dataset_type=<dataset_type>`| Type of the source dataset (`imagenet` or `voc`)
`--first_image=<image_number>`| *Optional*. The number of the image to start cutting from. Specify if you want to split your dataset into train/val subsets. The default is 0.

### Cut COCO

In a Python console, run the following command after specifying the parameters:

```
python C:/Users/Downloads/cut_dataset.py \
--source_images_archive_dir=<full_path_to_source_images_archive> \
--source_annotations_archive_dir=<full_path_to_source_annotations_archive> \
--output_size=<number_of_images> \
--output_archive_dir=<path_to_output_archive> \
--dataset_type=coco
--first_image=<image_number>
```
This command runs the script with the following arguments:

Parameter  |  Explanation
--|--
`--source_images_archive_dir=<full_path_to_source_images_archive>` |  Full path to the downloaded archive with images, including the name
`--source_annotations_archive_dir=<full_path_to_source_annotations_archive>` |  Full path to the downloaded archive with annotations, including the name
`--output_size=<number_of_images>` |  Number of images to be left in a smaller dataset
`--output_archive_dir=<path_to_output_archive>` | Full directory to the smaller dataset excluding the name
`--dataset_type=<dataset_type>`| Type of the source dataset
`--first_image=<image_number>`| *Optional*. The number of the image to start cutting from. Specify if you want to split your dataset into train/val subsets. The default is 0.