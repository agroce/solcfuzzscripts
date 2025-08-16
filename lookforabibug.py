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
    with open(f,"r") as testf:
        d = testf.read()
    if "pragma experimental ABIEncoderV2" not in d:
        tname = f.split("/")[-1].replace(".sol","_ABIV2.sol")
        with open(tname, 'w') as newf:
            newf.write("pragma experimental ABIEncoderV2;\n")
            newf.write(d)
        stime = time.time()
        r = subprocess.call(["ulimit -t 10; ../build/test/tools/solfuzzer " + tname], stderr=dnull, stdout=dnull, shell=True)
        elapsed = time.time() - stime
        if r != 0:
            if elapsed < 8:
                print(tname, "FAILED!")
            else:
                print(tname, "TIMED OUT!")
                os.rename(tname, tname.replace(".sol","_timeout.sol"))
        else:
            os.remove(tname)
    count += 1
