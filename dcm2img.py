import pydicom as dicom
import matplotlib.pyplot as plt
import os
import cv2
import PIL  # optional
import pandas as pd
import csv  # make it True if you want in PNG format

PNG = False  # Specify the .dcm folder path
folder_path = "/home/sandip/us-dicoms"  # Specify the .jpg/.png folder path
jpg_folder_path = "/home/sandip/us-pngs"
images_path = os.listdir(folder_path)  # list of attributes available in dicom image

for n, image in enumerate(images_path):
    ds = dicom.dcmread(os.path.join(folder_path, image))
    pixel_array_numpy = ds.pixel_array
    if PNG == False:
        image = image.replace('.dcm', '.jpg')
    else:
        image = image.replace('.dcm', '.png')
    cv2.imwrite(os.path.join(jpg_folder_path, image), pixel_array_numpy)
    if n % 50 == 0:
        print('{} image converted'.format(n))

