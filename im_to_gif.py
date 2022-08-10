import imageio
import os
import glob
import re
import cv2
import numpy as np


def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)


DES = 'result_blur1'
fps = 60
l = os.listdir(DES)
l2 = sorted_alphanumeric(l)
print(l)
print(l2)


img_array = []
# --- addd to beginning
im = cv2.imread('{}/{}'.format(DES, l2[0]))
for i in range(fps):
    img_array.append(im)
# ----
for file in l2:
    im = cv2.imread('{}/{}'.format(DES, file))
    size = (im.shape[1], im.shape[0])
    img_array.append(im)
# --- reverse
for i in img_array[::-1]:
    img_array.append(i)
# --- addd to end
im = cv2.imread('{}/{}'.format(DES, l2[0]))
for i in range(fps):
    img_array.append(im)
# ----



out = cv2.VideoWriter('1.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, size, True)
for i in range(len(img_array)):
    # out.write(c)
    out.write(img_array[i])
out.release()