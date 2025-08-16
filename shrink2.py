import subprocess
import os

dnull = open(os.devnull, 'w')

code = []

with open("best.sol", 'r') as f:
    code = f.read()

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
        r = subprocess.call(["../build/test/tools/solfuzzer < try.sol"], shell=True, stdout=dnull, stderr=dnull)
        if r != 0:
            print("REMOVING CHAR", pos, "WORKED:")
            print(code[pos])
            print("NEW LENGTH:", len(code)-1)
            changed = True
            newcode = code[:pos] + code[pos+1:]
            code = newcode
            with open("charshrink.sol", 'w') as f:
                for line in code:
                    f.write(line)
            break
