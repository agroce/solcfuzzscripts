from __future__ import print_function
import shutil
import glob
import os
import sys
import subprocess

dnull = open(os.devnull, 'w')

path = "*/*.sol"
depth = 0
while depth < 20:
    depth += 1
    for f in glob.glob("libsolidity/" + path):
        r = subprocess.call(["ulimit -t 5; ../build/test/tools/solfuzzer " + f], shell=True, stdout=dnull, stderr=dnull)
        if r != 0:
            print("SKIPPING FAILING TEST", f)
            continue
        fname = f.replace("libsolidity.","").replace("/","_")
        shutil.copy(f, sys.argv[1] + "/" + fname)
        with open(f, 'r') as tf:
            d = tf.read()
        if "pragma experimental SMTChecker" not in d:
            tname = fname.replace(".sol", "_SMT.sol")
            with open(sys.argv[1] + "/" + tname, 'w') as outf:
                outf.write("pragma experimental SMTChecker;\n")
                outf.write(d)
            r = subprocess.call(["ulimit -t 5; ../build/test/tools/solfuzzer " + sys.argv[1] + "/" + tname], shell=True, stdout=dnull, stderr=dnull)
            if r != 0:
                print(tname, "FAILED OR TIMED OUT!")
                os.remove(sys.argv[1] + "/" + tname)
        # No ABIEncoderV2 variant: ABI coder v2 is the default since Solidity 0.8.0,
        # so "pragma experimental ABIEncoderV2" only adds a deprecation warning.
    path = "*/" + path
                                                 
