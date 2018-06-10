#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 16:55:20 2018

@author: huang
"""

import wraper as fs
#import os 
#%%

def run_images():
    input_dir = './data/test_images/input'
    output_dir ='./data/test_images/output'
    model_dir = './data/models'
    swap_model = False

    ## process using images
    fs.process_images(input_dir,output_dir,model_dir,swap_model)

#%%
## if you are converting video
    
def run_video():
    input_video = './data/test_images/A.mp4'
    extract_dir = './data/test_images/extract'
    output_video = './data/test_images/A_out.mp4'
    model_dir = './data/models'
    
    ## convert using video
    fs.convert_video(input_video,extract_dir,output_video,model_dir,extract=True,swap_model=False)

#%%
# training
def run_training():
    images_A_dir = './data/train/trump'
    images_B_dir = './data/train/cage'
    extract_dir = './data/train/extract'
    model_dir = './data/models'
    epochs = 10000
    
    fs.train(images_A_dir,images_B_dir,extract_dir,model_dir,epochs,False)

#cmd = ['python', 'faceswap.py', 'train', '-A', './data/train/extract/A', '-B', './data/train/extract/B', '-m', './data/models', '-ep', 100, '-v']

#%%
## train with video inputs 
def run_training_video():
    input_video_A = './data/train/A.mp4'
    input_video_B = './data/train/B.mp4'
    
    extract_vid_A = './data/train/vid_img_A'
    extract_vid_B = './data/train/vid_img_B'
    
    extract_dir = './data/train/vid_img_extract'
    
    model_dir = './data/models'
    
    epochs = 10000
    ## first extract video to images 
    fs.extract_from_vid(input_video_A,extract_vid_A)
    fs.extract_from_vid(input_video_B,extract_vid_B)
    #%%
    
    ## train with extracted images 
    fs.train(extract_vid_A,extract_vid_B,extract_dir,model_dir,epochs,extract=False)
    
#%%
    
# test run images 
print('test, run trainings.')
#run_training_video()
#run_images()
run_video()