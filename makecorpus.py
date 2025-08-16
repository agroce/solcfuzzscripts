import glob
import shutil

oldprefix = ""
for f in glob.glob("new_*/queue/id*"):
    prefix = f.split("/")[0]
    if prefix != oldprefix:
        print prefix
        oldprefix = prefix
    fname = f.split("/")[-1]
    shutil.copy(f, "newcorpus/" + prefix + "." + fname)

