#!/usr/bin/env python3
""" The master faceswap.py script """
import sys
from scripts.convert import Convert as script
import arg as arg

if sys.version_info[0] < 3:
    raise Exception("This program requires at least python3.2")
if sys.version_info[0] == 3 and sys.version_info[1] < 2:
    raise Exception("This program requires at least python3.2")

    
process = script(arg)
process.process()
# clearn up allignment file 

#%%
from subprocess import call
#%%
#cmd =['python', 'tools.py', 'effmpeg', '-a gen-vid', '-i ./data/test_images/video_out', '-r ./data/test_images/input_trump_short.mp4','-o ./data/test_images/out_trump_short.mp4', '-fps 24','-m']
#call(cmd)
call(['python', 'tools.py', 'effmpeg', '-a','gen-vid', '-i', './data/test_images/video_out', '-r', './data/test_images/input_trump_short.mp4','-o', './data/test_images/out_trump_short.mp4', '-fps','-1','-m'])


