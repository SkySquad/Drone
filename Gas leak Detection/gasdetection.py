# -*- coding: utf-8 -*-
""" This is  an artificial intelligence model to detect gas leak detection using bayesian decision theory

"""

import numpy as np
import cv2

normal_img_path = input('home/skysquad/thermal/normal ') 
normal_img = cv2.imread(normal_img_path)
normal_img_mean = np.mean(normal_img)
normal_img_std = np.std(normal_img)
snd_normal = stats.norm(normal_img_mean, normal_img_std)


gas_img_path = input('home/skysquad/thermal/detected - ')
gas_img = cv2.imread(gas_img_path)
gas_img_mean = np.mean(gas_img)
gas_img_std = np.std(gas_img)
snd_gas = stats.norm(gas_img_mean,gas_img_std)

x = np.linspace(normal_img_mean, gas_img_mean, 1000)
min_val =np.argmin(np.abs( snd_normal.pdf(x) - snd_gas.pdf(x)))
boundary = x[min_val]
