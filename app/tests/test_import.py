import unittest
import os.path

class Test_Import(unittest.TestCase):

    # Check to make sure that .csv file exists
    def test_file_exists(self):
        self.assertTrue(os.path.exists("movie_metadata.csv"))

if __name__ == '__main__':
    unittest.main()
