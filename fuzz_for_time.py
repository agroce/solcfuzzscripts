import sys
import os
import signal
import subprocess
from subprocess import Popen, PIPE, TimeoutExpired
import time

fuzzer = sys.argv[1]
timeout = int(sys.argv[2])
runs = int(sys.argv[3])
outdirs = sys.argv[4]

for i in range(runs):
    outdir = outdirs + "." + str(i)
    print("RUN", i, " --> ", outdir)
    cmd = fuzzer + " -d -m 60 -i corpus -o " + outdir + " ../build/test/tools/solfuzzer"
    start = time.time()
    with Popen(cmd, shell=True, stdout=PIPE, preexec_fn=os.setsid) as process:
        while True:
            time.sleep(1)
            if (time.time() - start) > timeout:
                os.killpg(process.pid, signal.SIGINT)
                print("KILLING AFTER", time.time()-start)
                break
            else:
                print(".", end="")
                sys.stdout.flush()
        



