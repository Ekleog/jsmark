import os
import subprocess as subp
import sys

class Bench:
    moreisbetter = False

    def run(interp):
        os.chdir(os.path.join(sys.path[0], 'vendor', 'jsbench'))
        tests = subp.run("echo -n */*/*.js", shell=True, stdout=subp.PIPE,
                         universal_newlines=True)
        if tests.returncode != 0:
            raise RuntimeError("Error when listing the test cases of jsbench!")
        result = {}
        for test in tests.stdout.split(' '):
            res = subp.run([interp, test], stdout=subp.PIPE,
                           universal_newlines=True)
            if res.returncode != 0:
                raise RuntimeError("Error when trying to run jsbench " + test + " with interpreter " + interp + "!")
            res = res.stdout.split(' ')
            if len(res) != 2:
                continue
            res = res[1].split('m')
            if len(res) != 2:
                continue
            result[test] = float(res[0])
        return result
