#!/usr/bin/env python

import os
import subprocess

ufurl = os.getcwd()
ignore = tuple(['all_my_Py','pyparsing', 'python-dateutil', 'Python-2.7.8', 'SPAdes', 'matplotlib', 'lib', 'six'])

for topdir,currdir,contents in os.walk(ufurl):
    # print(ufurl)
    for f in contents:
        if 'Repo' in topdir or 'MFE' in topdir:
            continue
        if f.endswith('.py'):
            dont_cp = None
            full = os.path.join(topdir, f)
            for plc in full.split('/'):
               if plc.startswith(ignore):
                  dont_cp = True
            if not dont_cp:
               print(full)
            # with open(topdir+f, 'r') as peek:
            #     for i,line in enumerate(peek):
            #        if i == 2:
            #            continue
                  # if line.startswith('#!/usr/bin/env python'):
               cmd = ["cp", full, "/export/data/personal/jcollins_analysis/all_my_Py/"+f]
               p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
               for line in p.stdout:
                  print line
               p.wait()
               print p.returncode
                        # print(''.join(currdir)+f)
