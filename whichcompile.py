import subprocess
import glob
import sys
import os
import shutil

dnull = open(os.devnull, 'w')

total = 0.0
compiled = 0

for f in glob.glob(sys.argv[1]):
    if "orig" in f:
        continue
    total += 1
    r = subprocess.call(["../build/solc/solc " + f], stdout=dnull, stderr=dnull, shell=True)
    if r == 0:
        compiled += 1
        name = sys.argv[2] + "/c" + str(compiled)
        os.mkdir(name)
        shutil.copy(f, name + "/contract.sol")
        print (f, "COMPILES", compiled/total)
