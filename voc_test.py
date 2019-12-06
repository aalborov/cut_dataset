import unittest
import os
import shutil
from cut_dataset import unarchive, cut_voc
from utils import source_archive, download, create_archive


class TestVOC(unittest.TestCase):

    def setUp(self):
        self.download_link = 'https://github.com/aalborov/cut_dataset/files/3895560/sample_voc.zip'
        current_dir = os.getcwd()
        self.dataset_type = 'voc'
        self.source_archive_dir = source_archive(self.download_link, current_dir)
        download(self.download_link, self.source_archive_dir)
        self.output_archive_dir = os.path.join(current_dir, 'subsets')
        self.output_folder_dir = os.path.join(self.output_archive_dir, 'subset_folder')
        self.output_archive_name = '{}_subset'.format(self.dataset_type)

    def test_output_exists_default_1st_image_size4(self):
        """Default first image value, 4 images in the output archive."""
        output_size = 4
        first_image = 0
        unarchive(self.source_archive_dir, self.output_folder_dir)
        voc_data = cut_voc(output_size, self.output_folder_dir, first_image)
        file_exists = create_archive(voc_data, self.output_archive_dir, self.output_archive_name, self.output_folder_dir)
        self.assertTrue(file_exists)

    def test_output_exists_customized_1st_image_size4(self):
        """The first image index is 1, 4 images in the output archive."""
        output_size = 4
        first_image = 1
        unarchive(self.source_archive_dir, self.output_folder_dir)
        voc_data = cut_voc(output_size, self.output_folder_dir, first_image)
        file_exists = create_archive(voc_data, self.output_archive_dir, self.output_archive_name, self.output_folder_dir)
        self.assertTrue(file_exists)

    def test_output_exists_customized_1st_image_size7(self):
        """The first image index is 2, 7 images in the output archive."""
        output_size = 7
        first_image = 2
        unarchive(self.source_archive_dir, self.output_folder_dir)
        voc_data = cut_voc(output_size, self.output_folder_dir, first_image)
        file_exists = create_archive(voc_data, self.output_archive_dir, self.output_archive_name, self.output_folder_dir)
        self.assertTrue(file_exists)

    def tearDown(self):
        os.remove(self.source_archive_dir)
        shutil.rmtree(self.output_archive_dir)


if __name__ == '__main__':
    unittest.main()

    