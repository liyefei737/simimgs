
import time
import cv2
import numpy
from skimage.metrics import structural_similarity


def timed_call(f, args):
    start_time = time.time()
    result = f(*args)
    elapsed_time = time.time() - start_time
    return result, elapsed_time


def get_similarity(image1_path, image2_path):
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)
    img2 = numpy.resize(img2, (img1.shape[0], img1.shape[1], img1.shape[2]))
    score = 1 - structural_similarity(img1, img2, multichannel=True)
    return round(score,2)
