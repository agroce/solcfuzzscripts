import glob
import subprocess
import sys

messages = {}
pragmac = 0

for f in glob.glob(sys.argv[1] + "/crashes/id*"):
    with open("solfuzzer.out", 'w') as outf:
        r = subprocess.call(["build/solc/solc " + f], shell=True, stderr=outf, stdout=outf)
    with open(f, 'r', encoding='utf-8') as ff:
        if "pragma experimental solidity" in ff.read():
            pragmac += 1
            continue
    if r != 0:
        with open("solfuzzer.out") as inf:
            for line in inf:
                if ".cpp" in line:
                    if line in messages:
                        messages[line] += 1
                    else:
                        messages[line] = 1
    else:
        print(f, "DID NOT CRASH")
                    

for m in messages:
    print (m, messages[m])

print("IGNORED", pragmac, "FILES WITH solidity pragma")
