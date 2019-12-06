import urllib.request
import os
from cut_dataset import archive


def source_archive(url, current_dir):
    source_archive_name = os.path.basename(url)
    source_archive_dir = os.path.join(current_dir, source_archive_name)
    return source_archive_dir


def download(url, source_archive_dir):
    urllib.request.urlretrieve(url, source_archive_dir)


def create_archive(data, output_archive_dir, output_archive_name, output_folder_dir):
    new_file_names = data[0]
    rel_path_finder = data[1]
    archive(new_file_names, output_archive_dir, output_archive_name, output_folder_dir, rel_path_finder)
    return os.path.isfile(os.path.join(output_archive_dir, '{}.tar.gz'.format(output_archive_name)))

