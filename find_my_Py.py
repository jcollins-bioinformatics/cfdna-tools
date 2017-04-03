#!/usr/bin/env python
""" Full recurs. scan of a given directory tree to make copies of all python  
    scripts to a separator unified folder. 
"""
import os
import subprocess

unfurl = os.getcwd()

ignore = tuple(['all_my_Py','pyparsing', 'python-dateutil', 'Python-2.7.8', 'SPAdes', 'matplotlib', 'lib', 'six'])

for topdir,currdir,contents in os.walk(unfurl):
    # print(unfurl)
    for fn in contents:
        # if 'Repo' in topdir or 'MFE' in topdir:
        #     continue
        if fn.endswith('.py'):
            dont_cp = None
            full = os.path.join(topdir, fn)
            for place in full.split('/'):
               if place.startswith(ignore):
                  dont_cp = True
            if ~ dont_cp:
               print(full)
               cmd = ["cp", full, "/export/data/personal/jcollins_analysis/all_my_Py/"+f]
               p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
               for line in p.stdout:
                  print line
               p.wait()
               print p.returncode
               # print(''.join(currdir)+f)

            # with open(topdir+f, 'r') as peek:
            #     for i,line in enumerate(peek):
            #        if i == 2:
            #            continue
            # if line.startswith('#!/usr/bin/env python'):
