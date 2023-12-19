import unittest
from Dao.Artwork import Artwork

class TestGalleryDao(unittest.TestCase):
    def setUp(self):
        self.gallery_dao=Artwork()

    def test_update_gallery(self):
        result=self.gallery_dao.update()
        self.assertTrue(result,True)
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()