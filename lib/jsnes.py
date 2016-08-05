import os
import subprocess as subp
import sys

class Bench:
    moreisbetter = False

    def run(interp):
        os.chdir(os.path.join(sys.path[0], 'vendor', 'jsnes', 'test'))
        res = subp.run([interp, 'shell-bench.js'], stdout=subp.PIPE, universal_newlines=True)
        if res.returncode != 0:
            raise "Error when trying to run jsnes with interpreter " + interp + "!"
        warmup, result = 0., 0.
        nwarmup, nresult = 0., 0.
        for line in res.stdout.split('\n'):
            res = line.split(':')
            if len(res) != 2:
                continue
            if res[0] == 'warmup':
                warmup += float(res[1])
                nwarmup += 1
            elif res[0] == 'result':
                result += float(res[1])
                nresult += 1
        return {
            'warmup': warmup / nwarmup,
            '~~~~ Result': result / nresult,
        }
