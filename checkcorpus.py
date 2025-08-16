from __future__ import print_function
import shutil
import glob
import os
import sys
import subprocess
import time

dnull = open(os.devnull, 'w')

path = "*/*.sol"
depth = 0
while depth < 20:
    depth += 1
    for f in glob.glob("libsolidity/" + path):
        stime = time.time()
        r = subprocess.call(["ulimit -t 10; ../build/test/tools/solfuzzer " + f], stderr=dnull, stdout=dnull, shell=True)
        elapsed = time.time() - stime
        if r != 0:
            if elapsed < 8:
                print(f, "FAILED!")
            else:
                print(f, "TIMED OUT!")        
    path = "*/" + path
                                                 
