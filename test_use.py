#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 16:55:20 2018

@author: huang
"""

import faceswap_test as fs
import os 
#%%
input_dir = './data/test_images'
output_dir =os.path.join(input_dir,'output')
model_dir = './data/models'
swap_model = False

## if you are converting video
input_video = './data/test_images/trump.mp4'
extract_dir = './data/test_images/extract'
output_video = './data/test_images/trump_convert.mp4'
#%%
#fs.process_images(input_dir,output_dir,model_dir,swap_model)

#fs.convert_video(input_video,extract_dir,output_video,model_dir)