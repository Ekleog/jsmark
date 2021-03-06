import os
import subprocess as subp
import sys

class Bench:
    moreisbetter = True

    def run(interp):
        os.chdir(os.path.join(sys.path[0], 'vendor', 'octane'))
        res = subp.run([interp, 'run.js'], stdout=subp.PIPE, stderr=subp.PIPE, universal_newlines=True)
        if res.returncode != 0:
            return (
                "Error when trying to run octane with interpreter " + interp + "!\n"
                "Return code: " + str(res.returncode) + "\n"
                "stdout:\n\n"
                "----------8<----------8<----------8<----------\n"
                + res.stdout +
                "---------->8---------->8---------->8----------\n\n"
                "stderr:\n\n"
                "----------8<----------8<----------8<----------\n"
                + res.stderr +
                "---------->8---------->8---------->8----------\n\n"
            )
        result = {}
        for line in res.stdout.split('\n'):
            res = line.split(':')
            if len(res) != 2:
                continue
            result[res[0].replace('Score', '~~~~ Score')] = float(res[1])
        return result
