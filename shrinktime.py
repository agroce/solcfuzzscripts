import subprocess
import os

dnull = open(os.devnull, 'w')

code = []

with open("start.sol", 'r') as f:
    code = f.readlines()

changed = True
while changed:
    changed = False
    for pos in range(len(code)):
        with open("try.sol", 'w') as f:
            i = 0
            for line in code:
                if i != pos:
                    f.write(line)
                i += 1
        r = subprocess.call(["ulimit -t 70;../build/test/tools/solfuzzer < try.sol"], shell=True, stdout=dnull, stderr=dnull)
        if r == 137:
            print("REMOVING LINE", pos, "WORKED:")
            print(code[pos])
            print("NEW LENGTH:", len(code)-1)
            changed = True
            newcode = code[:pos] + code[pos+1:]
            code = newcode
            with open("finish.sol", 'w') as f:
                for line in code:
                    f.write(line)
            break
