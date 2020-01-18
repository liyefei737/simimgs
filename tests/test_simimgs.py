import os
import csv
import unittest
from simimgs import simimgs
from utils import get_similarity


def _row_count(csv_path):
    with open(csv_path, "r") as f:
        return len(list(csv.reader(f, delimiter=",")))


class TestSimimgs(unittest.TestCase):

    def testSimilaritySameImages(self):
        image1_path = './tests/resources/images/giraffe1.jpg'
        image2_path = './tests/resources/images/giraffe1.jpg'
        score = get_similarity(image1_path, image2_path)
        self.assertEqual(score, 0)

    def testSimilarityDiffImages(self):
        image1_path = './tests/resources/images/giraffe1.jpg'
        image2_path = './tests/resources/images/hippo.jpg'
        score = get_similarity(image1_path, image2_path)
        self.assertTrue(0 <= score <= 1)

    def testRelativeSimilarityImages(self):
        # imgA is more similar to imgC than it is to imgB
        imgA_path = './tests/resources/images/giraffe1.jpg'
        imgB_path = './tests/resources/images/giraffe2.jpg'
        imgC_path = './tests/resources/images/hippo.jpg'
        score_AC = get_similarity(imgA_path, imgC_path)
        score_AB = get_similarity(imgA_path, imgB_path)
        self.assertTrue(score_AB < score_AC)

    def testSimilarityImagesDiffSize(self):
        img_small = './tests/resources/images/giraffe1.jpg'
        # same image resized twice as large
        img_large = './tests/resources/images/giraffe1_large.jpg'
        score = get_similarity(img_small, img_large)
        self.assertTrue(score < 0.5)

    def testSimilarityImagesDifferentTypes(self):
        # jpeg and png types
        img_jpg = './tests/resources/images/giraffe1.jpg'
        img_png = './tests/resources/images/giraffe.png'
        score = get_similarity(img_jpg, img_png)
        self.assertTrue(0 <= score <= 1)

    def testInvalidInputCSVNoOutputCSV(self):
        invalid_csv_path = 'sdfhjkdskjfhsdjk/haskjkjhsd.csv'
        out_csv_path = './out_csv'
        simimgs(invalid_csv_path, out_csv_path)
        self.assertFalse(os.path.exists(out_csv_path))

    def testPartiallyCorrectInputCSVHasPartialOutput(self):
        # input file has 1 correct row and 1 incorrect row
        # output file should contain results for the good rows (1 row in this case)
        partially_correct_in = './tests/resources/csvs/partially_correct_in.csv'
        out_csv_path = './out_csv'
        simimgs(partially_correct_in, out_csv_path)
        row_count = _row_count(out_csv_path)
        os.remove(out_csv_path)
        self.assertTrue(row_count == 2)  # header row is also counted

    def testCorrectInputCSVCorrectlOutput(self):
        # some of the rows in the input has error
        # output should give result s the rows where there is no error
        correct_in = './tests/resources/csvs/correct_in.csv'
        out_csv_path = './out_csv'
        simimgs(correct_in, out_csv_path)
        row_count_in, row_count_out = _row_count(out_csv_path), _row_count(correct_in)
        os.remove(out_csv_path)
        self.assertEqual(row_count_in, row_count_out)


if __name__ == '__main__':
    unittest.main()
