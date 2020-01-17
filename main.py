


import os
import csv

from utils import get_similarity, timed_call

in_csv_path = 'in.csv'
out_csv_path = 'out.csv'

try:
    with open(in_csv_path, 'rt', encoding='utf-8') as csv_in:
        with open(out_csv_path, 'wt', encoding='utf-8') as csv_out:
            csv_reader = csv.reader(csv_in, delimiter=',')
            csv_writer = csv.writer(csv_out, delimiter=',')
            next(csv_reader)
            csv_writer.writerow(['image1', 'image2', 'similar', 'elapsed'])

            for row in csv_reader:
                #csv_writer.writerow(row)
                #print(row)
                im1_path, im2_path = row
                # 1 or 2 image files do not exist in the computer
                # log out which paths do not exist and move on the the next paris
                if not os.path.exists(im1_path) or not os.path.exists(im2_path):
                    # continue
                    pass

                # both file exist
                else:
                    similarity_score, run_time = timed_call(get_similarity, [im1_path,im2_path])
                    csv_writer.writerow([im1_path, im2_path, similarity_score, run_time])

except Exception as e:
    print('Error: ', e)
