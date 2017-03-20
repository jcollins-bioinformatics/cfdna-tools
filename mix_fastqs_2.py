#!/usr/bin/env python2.7
"""
Multigenome in silico contamination project
John Collins
CareDx,Inc. 
"""

from __future__ import print_function
import random
import sys

# /share/data/personal/jcollins_analysis/contamination_analysis/multi_genomes_in_silico
# -rwxr-xr-x 1 jcollins informatics  95587291 Sep  3 11:49 HRZ-601-03-28_S1_L001_R1_001.fastq
# -rwxr-xr-x 1 jcollins informatics  97983540 Sep  3 11:49 HRZ-601-03-28_S1_L001_R2_001.fastq
# -rwxr-xr-x 1 jcollins informatics 114288380 Sep  3 11:44 HRZ-609-03-26_S15_L001_R1_001.fastq
# -rwxr-xr-x 1 jcollins informatics 115854611 Sep  3 11:44 HRZ-609-03-26_S15_L001_R2_001.fastq
# -rwxr-xr-x 1 jcollins informatics  72596967 Sep  3 11:47 HRZ-801-03-28_S1_L001_R1_001.fastq
# -rwxr-xr-x 1 jcollins informatics  74196059 Sep  3 11:47 HRZ-801-03-28_S1_L001_R2_001.fastq

# HRZ-6-1 = HCC78 (use as D1)
# HRZ-6-9 = RKO (use as D2)
# HRZ-8-1 = SW48 (use as background)




# create random indeces between 0 and 1M for mixing fastqs 
one_M = 600000
# batch 1 parameters 
set_D1 = [0.0,0.0025,0.005,0.01,0.02,0.03]
set_D2 = [0.0,0.0025,0.005,0.01,0.02,0.03]
# batch 2 parameters
# set_D1 = [0.0,0.005,0.01,0.015,0.02,0.025,0.03,0.04,0.05]
# set_D2 = [0.0,0.005,0.01,0.015,0.02,0.025,0.03,0.04,0.05]

# test = False
for rep in (range(1,4)):
	for X_D1 in set_D1:
		for X_D2 in set_D2:
			bg_collected_reads = 0.0
			D1_collected_reads = 0.0
			D2_collected_reads = 0.0
			# if test:
			# 	break
		 	NHV_Ab_R1_all_reads = []
			NHV_Ab_R2_all_reads = []
			NHV_Da_R1_all_reads = []
			NHV_Da_R2_all_reads = []
			NHV_Q1_R1_all_reads = []
			NHV_Q1_R2_all_reads = []
			NHV_Ab_R1_reads = []
			NHV_Ab_R2_reads = []
			NHV_Da_R1_reads = []
			NHV_Da_R2_reads = []
			NHV_Q1_R1_reads = []
			NHV_Q1_R2_reads = []
			X_bg = 1.0 - (X_D1+X_D2)
			
			#file_out = "SW48_" + str(int(1000*X_bg)) + "p_HCC78_" + str(int(1000*X_D1)) + "p_RKO_" + str(int(1000*X_D2)) + "p_rep" + str(int(rep))
			file_out = "NHV_Q1_" + str(int(1000*X_bg)) + "p_NHV_Ab_" + str(int(1000*X_D1)) + "p_NHV_Da_" + str(int(1000*X_D2)) + "p_rep" + str(int(rep))

			bg_index = random.sample(range(1,one_M),int(X_bg*one_M-1))
			bg_index.sort()
			D1_index = random.sample(range(1,one_M/10),int(X_D1*one_M))
			D1_index.sort()
			D2_index = random.sample(range(1,one_M/10),int(X_D2*one_M))
			D2_index.sort()

			with open ('Ab_S2_L001_R1_001.fastq','r') as NHV_Ab_R1:
				line_count = 0
				read_count = 0
				curr_read = []
				# collect ALL fastq reads into an array 
				for line in NHV_Ab_R1:
					line_count += 1
					curr_read.append(line)
					if line_count == 4:
						line_count = 0
						read_count += 1
						#if read_count in D1_index:
						NHV_Ab_R1_all_reads.append(curr_read)
						#bg_collected_reads += 1
						# D1_index = [read_count:]
						curr_read = []
				# retain only reads that fall within randomized index 
				for index in D1_index:
					NHV_Ab_R1_reads.append(NHV_Ab_R1_all_reads[index])
					D1_collected_reads += 1

			with open ('Ab_S2_L001_R2_001.fastq','r') as NHV_Ab_R2:
				line_count = 0
				read_count = 0
				curr_read = []
				# collect ALL fastq reads into an array 
				for line in NHV_Ab_R2:
					line_count += 1
					curr_read.append(line)
					if line_count == 4:
						line_count = 0
						read_count += 1
						#if read_count in D1_index:
						NHV_Ab_R2_all_reads.append(curr_read)
						#bg_collected_reads += 1
						# D1_index = [read_count:]
						curr_read = []
				# retain only reads that fall within randomized index 
				for index in D1_index:
					NHV_Ab_R2_reads.append(NHV_Ab_R2_all_reads[index])
					D1_collected_reads += 1

			with open ('Da_S7_L001_R1_001.fastq','r') as NHV_Da_R1:
				line_count = 0
				read_count = 0
				curr_read = []
				# collect ALL fastq reads into an array 
				for line in NHV_Da_R1:
					line_count += 1
					curr_read.append(line)
					if line_count == 4:
						line_count = 0
						read_count += 1
						#if read_count in D1_index:
						NHV_Da_R1_all_reads.append(curr_read)
						#bg_collected_reads += 1
						# D1_index = [read_count:]
						curr_read = []
				# retain only reads that fall within randomized index 
				for index in D2_index:
					NHV_Da_R1_reads.append(NHV_Da_R1_all_reads[index])
					D2_collected_reads += 1

			with open ('Da_S7_L001_R2_001.fastq','r') as NHV_Da_R2:
				line_count = 0
				read_count = 0
				curr_read = []
				# collect ALL fastq reads into an array 
				for line in NHV_Da_R2:
					line_count += 1
					curr_read.append(line)
					if line_count == 4:
						line_count = 0
						read_count += 1
						#if read_count in D1_index:
						NHV_Da_R2_all_reads.append(curr_read)
						#bg_collected_reads += 1
						# D1_index = [read_count:]
						curr_read = []
				# retain only reads that fall within randomized index 
				for index in D2_index:
					NHV_Da_R2_reads.append(NHV_Da_R2_all_reads[index])
					D2_collected_reads += 1

			with open ('150701-Q1_S10_L001_R1_001.fastq','r') as NHV_Q1_R1:
				line_count = 0
				read_count = 0
				curr_read = []
				# collect ALL fastq reads into an array 
				for line in NHV_Q1_R1:
					line_count += 1
					curr_read.append(line)
					if line_count == 4:
						line_count = 0
						read_count += 1
						#if read_count in D1_index:
						NHV_Q1_R1_all_reads.append(curr_read)
						#bg_collected_reads += 1
						# D1_index = [read_count:]
						curr_read = []
				# retain only reads that fall within randomized index 
				for index in bg_index:
					NHV_Q1_R1_reads.append(NHV_Q1_R1_all_reads[index])
					bg_collected_reads += 1

			with open ('150701-Q1_S10_L001_R2_001.fastq','r') as NHV_Q1_R2:
				line_count = 0
				read_count = 0
				curr_read = []
				# collect ALL fastq reads into an array 
				for line in NHV_Q1_R2:
					line_count += 1
					curr_read.append(line)
					if line_count == 4:
						line_count = 0
						read_count += 1
						#if read_count in D1_index:
						NHV_Q1_R2_all_reads.append(curr_read)
						#bg_collected_reads += 1
						# D1_index = [read_count:]
						curr_read = []
				# retain only reads that fall within randomized index 
				for index in bg_index:
					NHV_Q1_R2_reads.append(NHV_Q1_R2_all_reads[index])
					bg_collected_reads += 1


			NHV_Ab = NHV_Ab_R1_reads + NHV_Ab_R2_reads
			NHV_Da =  NHV_Da_R1_reads + NHV_Da_R2_reads
			NHV_Q1 =  NHV_Q1_R1_reads + NHV_Q1_R2_reads
			ThreeGenomesMixture = NHV_Ab + NHV_Da + NHV_Q1

			output = open(file_out, 'w')
			for read in ThreeGenomesMixture:
				for line in read:
					output.write("{}".format(line))

			output.close()
			# test = True 

			print("{}\t{}\t{}\t{}\t".format(file_out,bg_collected_reads,D1_collected_reads,D2_collected_reads),file=sys.stderr) 



		# with open ('HRZ-601-03-28_S1_L001_R2_001.fastq','r') as NHV_Ab_R2:
		# 	line_count = 0
		# 	read_count = 0
		# 	curr_read = []
		# 	for line in NHV_Ab_R2:
		# 		line_count += 1
		# 		curr_read.append(line)
		# 		if line_count == 4:
		# 			line_count = 0
		# 			read_count += 1
		# 			if read_count in D1_index:
		# 				NHV_Ab_R2_reads.append(curr_read)
		# 				bg_collected_reads += 1
		# 			# D1_index = [read_count:]
		# 			curr_read = []

		# with open ('HRZ-609-03-26_S15_L001_R1_001.fastq','r') as NHV_Da_R1:
		# 	line_count = 0
		# 	read_count = 0
		# 	curr_read = []
		# 	for line in NHV_Da_R1:
		# 		line_count += 1
		# 		curr_read.append(line)
		# 		if line_count == 4:
		# 			line_count = 0
		# 			read_count += 1
		# 			if read_count in D2_index:
		# 				NHV_Da_R1_reads.append(curr_read)
		# 				bg_collected_reads += 1
		# 			# D1_index = [read_count:]
		# 			curr_read = []

		# with open ('HRZ-609-03-26_S15_L001_R2_001.fastq','r') as NHV_Da_R2:
		# 	line_count = 0
		# 	read_count = 0
		# 	curr_read = []
		# 	for line in NHV_Da_R2:
		# 		line_count += 1
		# 		curr_read.append(line)
		# 		if line_count == 4:
		# 			line_count = 0
		# 			read_count += 1
		# 			if read_count in D2_index:
		# 				NHV_Da_R2_reads.append(curr_read)
		# 				bg_collected_reads += 1
		# 			# D1_index = [read_count:]
		# 			curr_read = []

		# with open ('HRZ-801-03-28_S1_L001_R1_001.fastq','r') as NHV_Q1_R1:
		# 	line_count = 0
		# 	read_count = 0
		# 	curr_read = []
		# 	for line in NHV_Q1_R1:
		# 		line_count += 1
		# 		curr_read.append(line)
		# 		if line_count == 4:
		# 			line_count = 0
		# 			read_count += 1
		# 			if read_count in bg_index:
		# 				NHV_Q1_R1_reads.append(curr_read)
		# 				bg_collected_reads += 1
		# 			# D1_index = [read_count:]
		# 			curr_read = []

		# with open ('HRZ-801-03-28_S1_L001_R2_001.fastq','r') as NHV_Q1_R2:
		# 	line_count = 0
		# 	read_count = 0
		# 	curr_read = []
		# 	for line in NHV_Q1_R2:
		# 		line_count += 1
		# 		curr_read.append(line)
		# 		if line_count == 4:
		# 			line_count = 0
		# 			read_count += 1
		# 			if read_count in bg_index:
		# 				NHV_Q1_R2_reads.append(curr_read)
		# 				bg_collected_reads += 1
		# 			# D1_index = [read_count:]
		# 			curr_read = []


