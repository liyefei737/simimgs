import unittest
from utils import get_similarity


class TestSimimgs(unittest.TestCase):

    def testSimilaritySameImages(self):
        image1_path = './resources/images/giraffe1.jpg'
        image2_path = './resources/images/giraffe1.jpg'
        score = get_similarity(image1_path, image2_path)
        self.assertEqual(score, 0)

    def testSimilarityDiffImages(self):
        image1_path = './resources/images/giraffe1.jpg'
        image2_path = './resources/images/hippo.jpg'
        score = get_similarity(image1_path, image2_path)
        self.assertTrue(0 <= score <= 1)

    def testRelativeSimilarityImages(self):
        # imgA is more similar to imgC than it is to imgB
        imgA_path = './resources/images/giraffe1.jpg'
        imgB_path= './resources/images/giraffe2.jpg'
        imgC_path = './resources/images/hippo.jpg'
        score_AC = get_similarity(imgA_path, imgC_path)
        score_AB = get_similarity(imgA_path, imgB_path)
        self.assertTrue(score_AB < score_AC)

    # def testInvalidInputCSVNoOutputCSV(self):
    #     invalid_csv_path = ''

if __name__ == '__main__':
    unittest.main()
