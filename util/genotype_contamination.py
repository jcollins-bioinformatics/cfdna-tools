#!/usr/bin/env python2.7
""" Investigate potential contamination of NHV Streck samples 
"""

import sys
import collections

SNP_samples_dict = collections.defaultdict(list)
SNP_allele_freqs_dict = collections.defaultdict(list)
SNP_sample_genoCall = dict()
SNP_sample_genotype = dict()
SNP_sample_adjFreq = dict()
sample_DNA_type = dict()
samples_list = []
SNPs = []

# iterate through outputBySNP tertiary input file 
SNP_input = sys.stdin
skip = True
for line in SNP_input:
	# skip first line in file containing header
	if skip:
		skip = False
		continue
	fields = line.split("\t")
	sampleName = fields[1]#+"_"+fields[0][:1]
	if sampleName.startswith('HRZ') or fields[2].startswith('HRZ'):
	 	sample_DNA_type[sampleName] = 'HRZ'
	elif sampleName.startswith('DLS'):
		sample_DNA_type[sampleName] = 'DLS'
	else:
	 	sampleName = fields[2]#+"_"+fields[0][:1]
	 	sample_DNA_type[sampleName] = 'NHV'
	#uniqName = fields[2].strip()
	SNP_Name = fields[3].strip()
	genotype = fields[24] # tertiary column called "substitution"
	adjustedFreq = fields[32].strip()
	genocall = fields[33]
	SNP_samples_dict[SNP_Name].append(sampleName)
	SNP_sample_adjFreq[sampleName+SNP_Name] = adjustedFreq
	SNP_sample_genotype[sampleName+SNP_Name] = genotype
	SNP_sample_genoCall[sampleName+SNP_Name] = genocall
	if sampleName not in samples_list and len(sampleName)>0:
		samples_list.append(sampleName)
	if SNP_Name not in SNPs:
		SNPs.append(SNP_Name)

# compare donor alleles of RecHomo SNPs with AF > 0.01% adjFreq
sorted_SNPs = sorted(SNPs)
sorted_samples = sorted(samples_list)
sample_pair_scores = collections.defaultdict(int)
donorAlleles = collections.defaultdict(str)
recAlleles = collections.defaultdict(str)

#print(len(samples_list))
# collect both donor & recipient RH genotypes for all samples
for sample in sorted_samples:
	for SNP in sorted_SNPs:
		if sample in SNP_samples_dict[SNP]:
			adjFreq = SNP_sample_adjFreq[sample+SNP]
			genotype = SNP_sample_genotype[sample+SNP]
			genoCall = SNP_sample_genoCall[sample+SNP]
			if genoCall == 'Recipient Homo':
				# use zero cutoff as cutoff for donor AF's
				if float(adjFreq) > 0.0008:
					donorAlleles[sample+SNP] = genotype[1]
					recAlleles[sample+SNP] = genotype[0]
				else:
					recAlleles[sample+SNP] = genotype[0]

shared_RH_snps = collections.defaultdict(list)
sample_pair_max_scores = collections.defaultdict(int)
for sample_a in sorted_samples:
	if sample_a.startswith('HRZ-801A'):
		for sample_b in sorted_samples:
			max_score = 0
			for SNP in sorted_SNPs:
				if sample_a in SNP_samples_dict[SNP] and sample_b in SNP_samples_dict[SNP]:
					a_D_allele = donorAlleles[sample_a+SNP]
					b_R_allele = recAlleles[sample_b+SNP]
					if len(a_D_allele)>0 and len(b_R_allele)>0:
						max_score += 1
						shared_RH_snps["D_"+sample_a+"_R_"+sample_b].append(SNP)
						if a_D_allele == b_R_allele:
							sample_pair_scores["D_"+sample_a+"_R_"+sample_b] += 1
			sample_pair_max_scores["D_"+sample_a+"_R_"+sample_b] = max_score


for k,v in sample_pair_scores.items():
	if sample_pair_max_scores[k] > 10:
		print("{}\t{}\t{}\t{}\t".format(k,sample_DNA_type[k.split('_')[1]],v,sample_pair_max_scores[k]))#,shared_RH_snps[k]))



# for k,v in recAlleles.items():
# 	print(k,v)

# print("\t"),
# for sample in sorted_samples:
# 	print("{}\t".format(sample)),
# print("")
# for sample_a in sorted_samples:
# 	print("{}\t".format(sample_a)),
# 	for sample_b in sorted_samples:
# 		# create vectors for calculating correlation scores
# 		a_genos = []
# 		b_genos = []
# 		score = 0
# 		for SNP in sorted_SNPs:
# 			if sample_a in SNP_samples_dict[SNP] and sample_b in SNP_samples_dict[SNP]:
# 				a_adjFreq = SNP_sample_adjFreq[sample_a+SNP]
# 				b_adjFreq = SNP_sample_adjFreq[sample_b+SNP]
# 				a_genotype = SNP_sample_genotype[sample_a+SNP]
# 				b_genotype = SNP_sample_genotype[sample_b+SNP]
# 				a_genoCall = SNP_sample_genoCall[sample_a+SNP]
# 				b_genoCall = SNP_sample_genoCall[sample_b+SNP]
# 				if a_genoCall == 'Recipient Homo' and b_genoCall == 'Recipient Homo':
# 					if float(a_adjFreq) > 0.0001 and float(b_adjFreq) > 0.0001:
# 						a_genos.append(a_genotype)
# 						b_genos.append(b_genotype)
# 						if a_genos == b_genos:
# 							score += 1
# 		sample_pair_scores[sample_a+sample_b] = score
							







