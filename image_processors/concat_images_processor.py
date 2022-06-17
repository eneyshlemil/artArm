import cv2
import numpy as np


def concat_images_vertical(first_filename: str, second_filename: str) -> str:
    img1 = cv2.imread(first_filename)
    img2 = cv2.imread(second_filename)
    new_file_name = first_filename
    cv2.imwrite(new_file_name, np.concatenate((img1, img2), axis=0))

    return new_file_name
