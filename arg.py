#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 17:40:31 2018

@author: chengyu
"""


alignments_path=None
avg_color_adjust=True
blur_size=2
converter='Masked'
detector='hog'
discard_frames=False
erosion_kernel_size=None
filter=None
frame_ranges=None

gpus=1
input_aligned_dir=None
input_dir='/home/chengyu/Dev/face_swap/faceswap_test/data/test_images/video'
mask_type='facehullandrect'
match_histogram=True
model_dir='/home/chengyu/Dev/face_swap/faceswap_test/data/models'
nfilter=None
output_dir='/home/chengyu/Dev/face_swap/faceswap_test/data/test_images/video_out'
ref_threshold=0.6
seamless_clone=True
serializer='json'
sharpen_image=True
smooth_mask=True
swap_model=False
trainer='Original'
verbose=False
