import glob
import subprocess
import sys

messages = {}

for f in glob.glob(sys.argv[1] + "/crashes/id*"):
    with open("solfuzzer.out", 'w') as outf:
        r = subprocess.call(["../build/test/tools/solfuzzer", f], stderr=outf, stdout=outf)
    if r != 0:
        with open("solfuzzer.out") as inf:
            for line in inf:
                if "Output JSON" in line:
                    if line in messages:
                        messages[line] += 1
                    else:
                        messages[line] = 1

for m in messages:
    print m, messages[m]
