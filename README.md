jsmark
======

jsmark runs multiple benchmarks a number of times, and performs statistical
analysis of the results.

It runs continuously, outputting stats at the end of each benchmark run, and
tries to find the benchmark for which the confidence interval would be most
reduced if it was run again, so as to minimize the time spent running
benchmarks.

Note that the wording always assumes there is a JS shell with and without a
patch, as it was designed to compare different versions of the same engine. It
is only a matter of wording, though: the words "better" and "worse" in the
output of jsmark are saying that the version "with the patch" (ie. the second
one passed on the command line) is better or worse than the version "without the
pach" (ie. the first one passed on the command line).


Usage
=====

First, clone the repository with the submodules (the actual benchmarks):
```
git clone --recursive -j4 https://github.com/Ekleog/jsmark
```

Go into the directory
```
cd jsmark
```

Finally, run it with
```
./jsmark [path to JS shell without the patch] [path to JS shell with the patch]
```

Watch until you are happy with the results, and Ctrl-C it when done!


License
=======

The source code of jsmark itself is under the MIT license. The source code of
the benchmarks are under their own respective licenses.
