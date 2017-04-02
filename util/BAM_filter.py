#!/usr/bin/env python2.7
""" Read input BAM(s) line by line, and print to output only 
the reads that have >= 35 mapped bases.

Use Hawk 150702 as first test.

Command line:
samtools view -h -f 3 filename | $p278/python $myTools/parse_mapped_portions.py > output_file
"""

import collections
import re
import sys


def filter_BAM(BAM_input):
	'''
	'''
	for line in BAM_input:
		if line.startswith('@'):
			yield(line)
		else:
			fields = line.split()
			# read_name = fields[0]
			# full_read = fields[9]
			# read_length = len(full_read)
			# full_qual = fields[10]
			CIGAR = fields[5]
			map_operations = re.split('([A-Z])', CIGAR)
			# e.g., ['20', 'S', '150', 'M', '30', 'S', '']
			mapped_bases_count = 0
			# keep count through iteration of CIGAR elements
			i = -1
			for element in map_operations[:-1]:
				i += 1
				if element.isdigit():
					if map_operations[i+1]=='M':
						mapped_bases_count += int(map_operations[i])
			if mapped_bases_count > 80:
				yield(line)


def main(args):
	'''
	'''
	for new_BAM_line in filter_BAM(sys.stdin):
		print(new_BAM_line),


if __name__ == "__main__" :
		sys.exit(main(sys.argv))



	# seq_run_names = []
	# with open('/share/data/personal/jcollins_analysis/analytical_validation/all_dirs.txt', 'r') as AV_dirs:
	# 	for line in AV_dirs:
	# 		seq_run_names.append(line.split()[0])
	# AV_dirs.close()

	# subprocess.call(["module","load","samtools-0.1.19"])

	# for dirname, dirs, files in os.walk("/share/data/cfDNA/pipelineRuns"):
	# 	if dirname in AV_dirs:
	# 		PUSF = (dirname+"PUSF.txt", "w")
	# 		for topdir, subdirs, files in os.walk(dirname):
	# 			if topdir == "BAMs":
	# 				for BAM in files:
	# 					new_BAM = filter_BAM(BAM)
	# 					new_pileup = subprocess.check_output(["samtools","mpileup"])
	# 					print(tabulate_pileup(new_pileup), file=PUSF)



	# use os.walk to find select directories 
	# filter bams 
	# use subprocess.check_output() on samtools mpileup 

	# final output = PUSF 

	# 1) Filter through all BAMs in a particular seq run
 	#   -> use os.walk to filter through all dirs and find matches to dirs list file 
	# 2) Iterate by read
	# 3) Parse CIGAR 
	# 4) If less than 35 total matched bases, remove read (do not append to new BAM)
	# 5) Samtools mpileup on new filtered BAM files
	# 6) Tabulate PUSF from pileups





