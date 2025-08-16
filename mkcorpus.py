import shutil
import glob
import os
import sys

N = 0

d = ""
g = glob.glob(sys.argv[1] + d + "/*.sol")

while len(g) > 0:
    for f in g:
        n = f.split("/")[-1]
        if os.path.exists("corpus/" + n):
            N += 1
            shutil.copy(f, "corpus/" + n.replace(".sol", "." + str(N) + ".sol"))
        else:
            shutil.copy(f, "corpus/")
    d += "/*"
    g = glob.glob(sys.argv[1] + d + "/*.sol")
            
                                                 
