#!/usr/bin/env python2.7

""" 
Output, tab-delimited: 
CIGAR_string    count 

Command line:
samtools view -f 3 filename | $p278/python $myTools/parse_CIGAR_strings.py > output_file
OR samtools view -F 4 ...
"""

from __future__ import print_function
import collections
import sys


# parse CIGAR string from every line (6th field)
def read_BAM(BAM_input):
	''' Count occurences of unique CIGAR strings 
	'''
	output_list = []
	CIGAR_dict = collections.defaultdict(int)
	chr_reg_dict = collections.defaultdict(int)
	for line in BAM_input:
		# skip initial header lines until line no longer begins with '@'
		if line.startswith('@'):
			pass
		else:
			fields = line.split()
			# 6th field = CIGAR string
			# CIGAR format (7 operations)
			# M: match/mismatch
			# I: insertion
			# D: deletion
			# N: skipped bases with respect to reference
			# S: soft clipping
			# H: hard clipping
			# P: padding
			# read_name = fields[0]
			# full_read = fields[9]
			# read_length = len(full_read)
			# full_qual = fields[10]
			flag = fields[1]
			chr_reg = fields[2]
			CIGAR = fields[5].rstrip()
			CIGAR_dict[str(CIGAR)] += 1
			chr_reg_dict[str(chr_reg)] += 1
			#print(CIGAR)
	return CIGAR_dict, chr_reg_dict



def main(args):
	''' Call read_BAM function to collect output stats 
	'''
	print("CIGAR\tcount")
	CIGAR_hist, chr_reg_hist = read_BAM(sys.stdin)
	# sort CIGAR string dictionary by descending count
	#sorted_hist = sorted(CIGAR_hist.iteritems(), key=lambda (k,v): v[0], reverse=True)
	sorted_CIGAR_hist = sorted(CIGAR_hist, key=CIGAR_hist.get, reverse=True)
	sorted_chr_reg_hist = sorted(chr_reg_hist, key=CIGAR_hist.get, reverse=True)
	# for item in sorted_chr_reg_hist:
	# 	print ("{}\t{}".format(item,chr_reg_hist[item]))
	for item in sorted_CIGAR_hist:
		print ("{}\t{}".format(item,CIGAR_hist[item]))


if __name__ == "__main__" :
	sys.exit(main(sys.argv))
