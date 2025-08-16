import glob
import shutil

interesting = []
for d in glob.glob("new_*"):
    for f in glob.glob(d + "/queue/*+cov"):
        if "orig" not in f:
            shutil.copy(f, "nc")
