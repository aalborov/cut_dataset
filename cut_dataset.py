import os
import argparse
import shutil
import tarfile
import sys

image_types = ('.jpg', '.jpeg', '.jpe', '.img', '.png', '.bmp')
def parser():
    parser = argparse.ArgumentParser(description=' ')
    parser.add_argument('--source_archive_dir',
                        type=str,
                        required=True,
                        help='Full path to the source archive')
    parser.add_argument('--output_size',
                        type=int,
                        required=True,
                        help='Number of images in the output dataset')
    parser.add_argument('--first_image',
                        type=int,
                        required=False,
                        default=0,
                        help='Number of the image to start from')
    parser.add_argument('--output_archive_dir',
                        type=str,
                        required=True,
                        help='Full path to the output archive (without the name of the archive)')
    parser.add_argument('--dataset_type',
                        type=str,
                        choices=['imagenet', 'pascal voc', 'voc'],
                        required=True,
                        help='Dataset format: ImageNet or Pascal VOC')
    return parser


def unarchive(source_archive_dir, output_folder_dir):
    shutil.unpack_archive(source_archive_dir, output_folder_dir)


def is_possible_to_cut(dataset_size, subset_size, first_image):
    return first_image < dataset_size - subset_size


def cut_imagenet(output_size, output_folder_dir, first_image):
    file_names = os.listdir(output_folder_dir)
    image_names = []

    text_files = []
    for file_name in file_names:
        if file_name.lower().endswith('.txt'):
            text_files.append(file_name)
            if len(text_files) > 1:
                sys.exit('Incorrect dataset format.')
            else:
                annotation_name = file_name
        elif file_name.lower().endswith(image_types):
            image_names.append(file_name)
    image_ext = os.path.splitext(image_names[0])[1]
    if not image_names:
        sys.exit('Incorrect dataset format.')

    if not is_possible_to_cut(len(image_names), output_size, first_image):
        sys.exit('Invalid --first-image value. The number of the starting image should be less than the difference '
                 'between the dataset size and the subset size.')

    annotation_path = os.path.join(output_folder_dir, annotation_name)
    with open(annotation_path, 'r') as annotation:
        annotation_text = annotation.readlines()

    new_annotation_text = annotation_text[first_image:output_size+first_image]

    with open(annotation_path, 'w') as new_annotation:
        for line in new_annotation_text:
            new_annotation.write(line)

    new_file_names = [annotation_name, ]

    for line in new_annotation_text:
        new_file_names.append('{}{}'.format(os.path.splitext(line.split()[0])[0], image_ext))

    files_to_archive = (new_file_names, '',)

    return files_to_archive


def cut_voc(output_size, output_folder_dir, first_image):
    voc_folder = os.listdir(output_folder_dir)[0]

    voc_year_folder_dir = os.path.join(output_folder_dir, voc_folder)
    voc_year_folder = os.listdir(voc_year_folder_dir)[0]

    voc_root_dir = os.path.join(voc_year_folder_dir, voc_year_folder)
    voc_content_root_folders = os.listdir(voc_root_dir)

    annotation_dir = os.path.join(voc_root_dir, 'Annotations')
    for element in voc_content_root_folders:
        path_to_element = os.path.join(voc_root_dir, element)
        if os.path.isdir(path_to_element) and 'Images' in element:
            images_dir = path_to_element

    images_files = os.listdir(images_dir)[first_image:first_image+output_size]

    if not is_possible_to_cut(len(images_files), output_size, first_image):
        sys.exit('Invalid --first-image value. The number of the starting image should be less than the difference'
                 'between the dataset and subset sizes.')

    main_dir = os.path.join(voc_root_dir, 'ImageSets', 'Main')

    if (not os.path.isdir(annotation_dir) or not os.path.isdir(main_dir)
            or not os.path.isdir(images_dir)):
        sys.exit('Incorrect dataset format.')

    names = []
    files_directories = []

    for images_file in images_files:
        img_name = os.path.splitext(images_file)[0]
        annotation = '{}.xml'.format(os.path.join(annotation_dir, img_name))
        if images_file.lower().endswith(image_types) and os.path.isfile(annotation):
            names.append(img_name)
            files_directories.append(os.path.join(images_dir, images_file))
        if len(names) == output_size:
            break
    if not names:
        sys.exit('Incorrect dataset format.')

    for name in names:
        files_directories.append('{}.xml'.format(os.path.join(annotation_dir, name)))

    possible_names = ('test.txt', 'trainval.txt', 'val.txt')
    main_txt_dir = None
    for name in possible_names:
        if os.path.isfile(os.path.join(main_dir, name)):
            main_txt_dir = os.path.join(main_dir, name)
            break
    if not os.path.isfile(main_txt_dir):
        sys.exit('Incorrect dataset format')

    with open(main_txt_dir, 'w') as main:
        main.write('\n'.join(names))

    files_directories.append(main_txt_dir)
    files_to_archive = (files_directories, 'VOCdevkit',)

    return files_to_archive


def archive(new_file_names, source_path, output_archive_name, output_folder_dir, rel_path_finder):
    with tarfile.open(os.path.join(source_path, '{}.tar.gz'.format(output_archive_name)), 'w:gz') as tar:
        for file_name in new_file_names:
            relative_path = '{}'.format(file_name[file_name.find(rel_path_finder):])
            tar.add(os.path.join(output_folder_dir, file_name), arcname=relative_path)


def clean_up(output_folder_dir):
    shutil.rmtree(output_folder_dir)


def is_imagenet(dataset_type):
    return dataset_type == 'imagenet'


if __name__ == '__main__':
    args = parser().parse_args()

    output_folder_dir = os.path.join(args.output_archive_dir, 'temp')
    output_archive_name = '{}_subset_{}_{}'.format(args.dataset_type, args.first_image, args.first_image + args.output_size)
    unarchive(args.source_archive_dir, output_folder_dir)

    if is_imagenet(args.dataset_type):
        imagenet_data = cut_imagenet(args.output_size, output_folder_dir, args.first_image)
        new_file_names = imagenet_data[0]
        rel_path_finder = imagenet_data[1]
    else:
        voc_data = cut_voc(args.output_size, output_folder_dir, args.first_image)
        new_file_names = voc_data[0]
        rel_path_finder = voc_data[1]

    archive(new_file_names, args.output_archive_dir, output_archive_name, output_folder_dir, rel_path_finder)
    clean_up(output_folder_dir)
