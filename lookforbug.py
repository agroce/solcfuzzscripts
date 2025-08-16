from __future__ import print_function

import subprocess
import glob
import os
import time

dnull = open(os.devnull,'w')

g = glob.glob("latest_corpus/*.sol")
count = 1

for f in g:
    if (count % 50) == 0:
        print("CHECKING TEST #" + str(count))
    stime = time.time()
    r = subprocess.call(["ulimit -t 10; ../build/test/tools/solfuzzer " + f], stderr=dnull, stdout=dnull, shell=True)
    elapsed = time.time() - stime
    if r != 0:
        if elapsed < 8:
            print(f, "FAILED!")
        else:
            print(f, "TIMED OUT!")
    count += 1
