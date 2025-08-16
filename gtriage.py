import glob
import subprocess
import sys

messages = {}
files = {}

for f in sorted(glob.glob(sys.argv[1] + "/*.sol*")):
    with open("solfuzzer.out", 'w') as outf:
        r = subprocess.call(["../build/solc/solc", f, "--optimize"], stderr=outf, stdout=outf)
    if r != 0:
        fc = False
        with open("solfuzzer.out") as inf:
            lines = inf.readlines()
            for line in lines:
                if (".h" not in line) and (".cpp" not in line) and ("ption" not in line):
                    continue
                if line in messages:
                    messages[line] += 1
                    fc = True
                    break
                else:
                    messages[line] = 1
                    files[line] = f
                    fc = True
                    break
        if not fc:
            print "NO TRIAGE FOR", f
    else:
        with open("solfuzzer.out", 'w') as outf:        
            r = subprocess.call(["../build/test/tools/solfuzzer", f], stderr=outf, stdout=outf)
        if r != 0:
            print f, "FAILS with solfuzzer, but not solc"

for m in messages:
    print m, messages[m], files[m]
    print "="*80
