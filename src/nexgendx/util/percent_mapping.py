#!/usr/bin/env python2.7


import os
import sys
import subprocess



for topdir, dirs, contents in os.walk("/share/data/cfDNA/pipelineRuns"):
	#if topdir.endswith('BAMs'):
	#if topdir.split('/')[-1].endswith('Osprey'):
		for dirname, subdirs, files in os.walk(topdir):
			if dirname.endswith('BAMs'): 
				#curr_files = subprocess.check_output(['ls','-l',topdir]).split('\n')
				os.chdir(dirname)
				subprocess.call('/share/data/personal/jcollins_analysis/tools/percent_unmapped.sh',shell=True)
				mapstats = dirname+'/mapstats.txt'
				header = False
				with open(mapstats,'r') as read_mapstats:
					for line in read_mapstats:
						line = line.strip()
						if header == False:
							header = True 
							continue
						print("{}\t{}\t".format(dirname.split('/')[6],line))
				

				