import numpy as np
import os

PATH = 'three-laps-large'

for file in os.listdir(PATH):
    if file.endswith('.npz'):
        data = np.load(PATH + '/' + file)
        data = data['points']
        data.tofile('velodyne/' + file[:-4] + '.bin')