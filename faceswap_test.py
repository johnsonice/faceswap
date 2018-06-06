#!/usr/bin/env python3
""" The master faceswap.py script """
import sys
from scripts.convert import Convert as script
import arg as arg
import os 
import shutil
from subprocess import call

if sys.version_info[0] < 3:
    raise Exception("This program requires at least python3.2")
if sys.version_info[0] == 3 and sys.version_info[1] < 2:
    raise Exception("This program requires at least python3.2")

    
#process = script(arg)
#process.process()
#clearn up allignment file 

#%%
def delete_file(file_dir):
    if os.path.exists(file_dir):
        try:
            os.remove(file_dir)
            print('Old face alignment file deleted, creating a new one now.')
        except:
            print ("Error: {}.".format(file_dir))
    else:  
        print("No alignment found, creating a new face alignment.json file")

def extract_from_vid(video_in,img_out_folder):
    cmd = ['python', 'tools.py', 'effmpeg', '-a','extract', '-i', video_in, '-o', img_out_folder, '-fps','-1','-m']
    status = call(cmd)
    print(status)

def process_images(input_dir = None,output_dir=None,model_dir=None,swap_model=False):
    if input_dir and os.path.exists(input_dir):
        arg.input_dir = input_dir
    else:
        print('Input image folder does not exist')
        return
    if model_dir and os.path.exists(model_dir):
        arg.model_dir = model_dir
    else:
        print('can not find pretrained model.')
        return 
    if output_dir:
        arg.output_dir = output_dir 
    if swap_model:
        arg.swap_model = swap_model 
        
    alignment_dir = os.path.join(input_dir,'alignments.json')
    delete_file(alignment_dir)
    
    process = script(arg)
    process.process()

def generate_video(input_dir,reference_video,output_video):
    cmd =['python', 'tools.py', 'effmpeg', '-a','gen-vid', '-i', input_dir, '-r', reference_video,'-o', output_video, '-fps','-1','-m']
    status = call(cmd)
    print(status)

def convert_video(input_video,extract_dir,output_video,model_dir):
    extract_img_dir = os.path.join(extract_dir,'extracted_imgs')
    processed_img_dir = os.path.join(extract_dir,'processed_imgs')

    extract_from_vid(input_video,extract_img_dir)
    print('step 1: images extracted from video file ...')
    process_images(extract_img_dir,processed_img_dir,model_dir)
    print('step 2: images converted')
    generate_video(processed_img_dir,input_video,output_video)
    print('video transform successed!')
    shutil.rmtree(extract_dir)


def train(images_A_dir, images_B_dir,extract_dir,model_dir):
    # To convert image a:
    extract_dir_a = os.path.join(extract_dir, 'A')
    cmd_a = ['python', 'faceswap.py', 'extract', '-i', images_A_dir, '-o', extract_dir_a]
    status = call(cmd_a)
    #python faceswap.py extract -i ~/faceswap/photo/trump -o ~/faceswap/data/trump
    # To convert image b:
    extract_dir_b = os.path.join(extract_dir, 'B')
    cmd_b = ['python', 'faceswap.py', 'extract', '-i', images_B_dir, '-o', extract_dir_b]
    status = call(cmd_b)
    #python faceswap.py extract -i ~/faceswap/photo/cage -o ~/faceswap/data/cage
    
    ## starting training 
    cmd = ['python', 'faceswap.py', 'train', '-A','extract_dir_a', '-B', extract_dir_b, '-m', model_dir]
    #python faceswap.py train -A ~/faceswap/data/trump -B ~/faceswap/data/cage -m ~/faceswap/models/
    
    status = call(cmd)
    print(status)
    
#%%
#cmd =['python', 'tools.py', 'effmpeg', '-a','gen-vid', '-i', './data/test_images/video_out', '-r', './data/test_images/input_trump_short.mp4','-o', './data/test_images/out_trump_short.mp4', '-fps','-1','-m']
#call(cmd)
#%%

