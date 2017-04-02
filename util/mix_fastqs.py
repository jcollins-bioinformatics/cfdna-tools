#!/usr/bin/env python2.7

import random

# -rwxr-xr-x 1 jcollins informatics  95587291 Sep  3 11:49 HRZ-601-03-28_S1_L001_R1_001.fastq
# -rwxr-xr-x 1 jcollins informatics  97983540 Sep  3 11:49 HRZ-601-03-28_S1_L001_R2_001.fastq
# -rwxr-xr-x 1 jcollins informatics 114288380 Sep  3 11:44 HRZ-609-03-26_S15_L001_R1_001.fastq
# -rwxr-xr-x 1 jcollins informatics 115854611 Sep  3 11:44 HRZ-609-03-26_S15_L001_R2_001.fastq
# -rwxr-xr-x 1 jcollins informatics  72596967 Sep  3 11:47 HRZ-801-03-28_S1_L001_R1_001.fastq
# -rwxr-xr-x 1 jcollins informatics  74196059 Sep  3 11:47 HRZ-801-03-28_S1_L001_R2_001.fastq

"""
Mix 1:
3 percent HCC78 (6-1) & 2 percent RKO (6-9) in SW48 (8-1) background
--> creates two new R1 & R2 fastq files 

Mix 2:
?

"""

collected_reads = 0.0
HRZ_6_1_R1_reads = []
HRZ_6_1_R2_reads = []
HRZ_6_9_R1_reads = []
HRZ_6_9_R2_reads = []
HRZ_8_1_R1_reads = []
HRZ_8_1_R2_reads = []


with open ('HRZ-601-03-28_S1_L001_R1_001.fastq','r') as HRZ_6_1_R1:
	line_count = 0
	curr_read = []
	for line in HRZ_6_1_R1:
		line_count += 1
		curr_read.append(line)
		if line_count == 4:
			line_count = 0
			if random.random() <= 0.015:
				HRZ_6_1_R1_reads.append(curr_read)
				collected_reads += 1
			curr_read = []

with open ('HRZ-601-03-28_S1_L001_R2_001.fastq','r') as HRZ_6_1_R2:
	line_count = 0
	curr_read = []
	for line in HRZ_6_1_R2:
		line_count += 1
		curr_read.append(line)
		if line_count == 4:
			line_count = 0
			if random.random() <= 0.015:
				HRZ_6_1_R2_reads.append(curr_read)
				collected_reads += 1
			curr_read = []

with open ('HRZ-609-03-26_S15_L001_R1_001.fastq','r') as HRZ_6_9_R1:
	line_count = 0
	curr_read = []
	for line in HRZ_6_9_R1:
		line_count += 1
		curr_read.append(line)
		if line_count == 4:
			line_count = 0
			if random.random() <= 0.01:
				HRZ_6_9_R1_reads.append(curr_read)
				collected_reads += 1
			curr_read = []

with open ('HRZ-609-03-26_S15_L001_R2_001.fastq','r') as HRZ_6_9_R2:
	line_count = 0
	curr_read = []
	for line in HRZ_6_9_R2:
		line_count += 1
		curr_read.append(line)
		if line_count == 4:
			line_count = 0
			if random.random() <= 0.01:
				HRZ_6_9_R2_reads.append(curr_read)
				collected_reads += 1
			curr_read = []

with open ('HRZ-801-03-28_S1_L001_R1_001.fastq','r') as HRZ_8_1_R1:
	line_count = 0
	curr_read = []
	for line in HRZ_8_1_R1:
		line_count += 1
		curr_read.append(line)
		if line_count == 4:
			line_count = 0
			if random.random() <= 0.475:
				HRZ_8_1_R1_reads.append(curr_read)
				collected_reads += 1
			curr_read = []

with open ('HRZ-801-03-28_S1_L001_R2_001.fastq','r') as HRZ_8_1_R2:
	line_count = 0
	curr_read = []
	for line in HRZ_8_1_R2:
		line_count += 1
		curr_read.append(line)
		if line_count == 4:
			line_count = 0
			if random.random() <= 0.475:
				HRZ_8_1_R2_reads.append(curr_read)
				collected_reads += 1
			curr_read = []


collected_reads = collected_reads * .90
HRZ_HCC78_mix = random.sample(HRZ_6_1_R1_reads,int(round(collected_reads*.015,1))) + random.sample(HRZ_6_1_R2_reads,int(round(collected_reads*.015,1)))
HRZ_RKO_mix = random.sample(HRZ_6_9_R1_reads,int(round(collected_reads*.005,1))) + random.sample(HRZ_6_9_R2_reads,int(round(collected_reads*.005,1)))
HRZ_SW48_mix = random.sample(HRZ_8_1_R1_reads,int(round(collected_reads*.49,1))) + random.sample(HRZ_8_1_R2_reads,int(round(collected_reads*.49,1)))

ThreeGenomesMixture = HRZ_HCC78_mix + HRZ_RKO_mix + HRZ_SW48_mix
#random.shuffle(ThreeGenomesMixture)

# print(len(ThreeGenomesMixture))
# print(len(ThreeGenomesMixture[0]))
# print(ThreeGenomesMixture[0])
# print(len(ThreeGenomesMixture[0][1]))
# print(len(HRZ_6_1_R1_reads))
# print(HRZ_6_1_R1_reads[0][:50])


for line in ThreeGenomesMixture:
	for item in line:
		print(item),




