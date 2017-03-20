#usr/bin/env python2.7
"""
"""

from __future__ import division
# from __future__ import print_function
from collections import defaultdict 
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as backend_pdf
import matplotlib
import numpy as np
import operator 
import re
import random
import sys



# input file for decrypting sample IDs into Patient IDs
Patient_ID_longitudinal = {}
with open('/Users/jcollins/cfDNA/Stanford Peds/Batch 2 analysis/match_encrypted_IDs_160303.txt') as match_IDs:
	header_saved = False
	for i,line in enumerate(match_IDs):
		fields = [x.strip() for x in line.split('\t')]
		if header_saved == False:
			header = fields
			header_saved = True
			continue
		for num,cell in enumerate(fields):
			if header[num] == ('Encrypted ID'):
				encrypted_ID = cell[:10]
			if header[num] == ('Patient ID'):
				patient_ID = cell
			if header[num] == ('Timepoint'):
				timepoint = cell
		Patient_ID_longitudinal[encrypted_ID] = patient_ID



# only use final analysis samples (N=434)
final_results = []
with open('/Users/jcollins/cfDNA/Stanford Peds/Batch 2 analysis/All_SF_Peds_final_results_for_analysis_160309.txt') as outputBySample:
	header_saved = False
	for i,line in enumerate(outputBySample):
		fields = [x.strip() for x in line.split('\t')]
		if header_saved == False:
			header = fields
			header_saved = True
			continue
		for num,cell in enumerate(fields):
			if header[num] == ('SAMPLENAME'):
				smpl_ID = cell
			if header[num] == ('RUNNAME'):
				seq_ID = cell
			if header[num] == ('RUN_ID'):
				run_ID = cell
			if header[num] == ('EXPERIMENTNAME'):
				exp = cell
		uniq_smpl_ID = smpl_ID+'@'+exp+'@'+run_ID
		final_results.append(uniq_smpl_ID)

# print(final_results)
# print(len(final_results))

# key: Patient ID, value: dictionary of list of SNP freqs
Patient_SNP_means = defaultdict(lambda: defaultdict(list))
# key: uniq sample ID, value: dictionary of SNP freqs 
smpl_SNP_freqs_dict = defaultdict(lambda: {})
Samples_seen_perSNP = defaultdict(set)
SNPs_detected = set()
with open('/Users/jcollins/cfDNA/Stanford Peds/Batch 2 analysis/all_SFPeds_outputBySNP_160303.txt') as outputBySNP:
	header_saved = False
	for i,line in enumerate(outputBySNP):
		fields = [x.strip() for x in line.split('\t')]
		if header_saved == False:
			header = fields
			header_saved = True
			continue
		for num,cell in enumerate(fields):
			if header[num] == ('EXPERIMENT_NAME'):
				cell = re.sub('[-]', '', cell).upper()
				exp = re.sub('REDOPOOL', 'REPOOL', cell)
			if header[num] == ('RUN_ID'):
				run_ID = cell
			if header[num] == ('SAMPLE_NAME'):
				smpl = cell[:10]
			if header[num] == ('SNP_NAME'):
				SNP_ID = cell
			if header[num] == ('ADJUSTEDFREQUENCY'):
				try:
					adjFreq = float(cell)
				except ValueError:
					adjFreq = 'NA'
		if smpl.startswith('NIST'):
			continue
		if smpl.startswith('HRZ'):
			continue

		patient_ID = Patient_ID_longitudinal[smpl[:10]]
		uniq_smpl_ID = smpl+'@'+exp+'@'+run_ID
		if uniq_smpl_ID not in final_results:
			continue
		# check if unique sample ID in N=434 final SF Peds samples to use for analysis 
		SNPs_detected.add(SNP_ID)
		Samples_seen_perSNP[SNP_ID].add(patient_ID+'@'+uniq_smpl_ID)
		smpl_SNP_freqs_dict[patient_ID+'@'+uniq_smpl_ID][SNP_ID] = adjFreq



### Iterate through every sample-sample combination, & calculate correlation coefficient 
sorted_samples = [x[0] for x in sorted(smpl_SNP_freqs_dict.items(), key=lambda (k,v): k)]
sorted_SNPs = sorted(SNPs_detected)

# print(sorted_samples)
# print(sorted_SNPs)

smpl_smpl_corr_coefs = {}
print("\t"),
for sample in sorted_samples:
	print("{}\t".format(sample)),
print("")

for sample_a in sorted_samples:
	print("{}\t".format(sample_a)),
	for sample_b in sorted_samples:
		a_freqs = []
		b_freqs = []
		for SNP in sorted_SNPs:
			if sample_a in Samples_seen_perSNP[SNP] and sample_b in Samples_seen_perSNP[SNP]:
				try:
					a_adjFreq = float(smpl_SNP_freqs_dict[sample_a][SNP])
					b_adjFreq = float(smpl_SNP_freqs_dict[sample_b][SNP])
				except ValueError:
					continue
				a_freqs.append(a_adjFreq)
				b_freqs.append(b_adjFreq)
		if len(a_freqs) == 0:
			continue
		ab_corr = np.corrcoef(a_freqs,b_freqs)
		smpl_smpl_corr_coefs[sample_a+sample_b] = ab_corr
		if ab_corr[0][1] > 0.9 and sample_a.split('@')[0]!=sample_b.split('@')[0]:
				ab_corr = ab_corr + 1
				print(sample_a,sample_b)
		# print(ab_corr)
		# print("{}\t".format(ab_corr[0][1])),
		# print("{},{}\t".format(a_freqs,b_freqs)),
	print("")













