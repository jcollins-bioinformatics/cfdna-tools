#!/usr/bin/env python2.7

from __future__ import division
from __future__ import print_function
import collections
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as backend_pdf
import matplotlib
import numpy as np
import operator 
import random
import sys

basic_colors = {
'mediumblue':           '#0000CD',
'indigo':               '#4B0082',
'peru':                 '#CD853F',
'darkturquoise':        '#00CED1',
'darkgray':             '#A9A9A9',
'darkred':              '#8B0000',
'dimgray':              '#696969',
'gold':                 '#FFD700',
'mediumseagreen':       '#3CB371',
'steelblue':            '#4682B4',
'mediumvioletred':      '#C71585',
'tan':                  '#D2B48C',
#'black':                '#000000',
'orchid':               '#DA70D6',
'chartreuse':           '#7FFF00',
'fuchsia':              '#FF00FF',
'red':                  '#FF0000',
}

ext_colors = {
'mediumblue':           '#0000CD',
'indigo':               '#4B0082',
'peru':                 '#CD853F',
'darkturquoise':        '#00CED1',
'darkgray':             '#A9A9A9',
'darkred':              '#8B0000',
'dimgray':              '#696969',
'gold':                 '#FFD700',
'mediumseagreen':       '#3CB371',
'steelblue':            '#4682B4',
'mediumvioletred':      '#C71585',
'tan':                  '#D2B48C',
'black':                '#000000',
'orchid':               '#DA70D6',
'chartreuse':           '#7FFF00',
'fuchsia':              '#FF00FF',
'red':                  '#FF0000',
'burlywood':            '#DEB887',
'darkorange':           '#FF8C00',
'darkorchid':           '#9932CC',
'darksalmon':           '#E9967A',
'deepskyblue':          '#00BFFF',
'dimgray':              '#696969',
'forestgreen':          '#228B22',
'midnightblue':         '#191970',
'hotpink':              '#FF69B4',
'indianred':            '#CD5C5C',
'indigo':               '#4B0082',
}

best_colors = {
#'black':                '#000000',
'burlywood':            '#DEB887',
'darkorange':           '#FF8C00',
'darkorchid':           '#9932CC',
'darksalmon':           '#E9967A',
'deepskyblue':          '#00BFFF',
'dimgray':              '#696969',
'forestgreen':          '#228B22',
'midnightblue':         '#191970',
'olive':                '#808000',
'tomato':               '#FF6347',
'turquoise':            '#40E0D0',
'mediumblue':           '#0000CD',
'maroon':               '#800000',
'purple':               '#800080',
'crimson':              '#DC143C',
'darkgoldenrod':        '#B8860B',
'darkgray':             '#A9A9A9',
'mediumseagreen':       '#3CB371',
'darkseagreen':         '#8FBC8F',
'darkslateblue':        '#483D8B',
'darkslategray':        '#2F4F4F',
'darkturquoise':        '#00CED1',
}

all_colors = {
'aqua':                 '#00FFFF',
'aquamarine':           '#7FFFD4',
'black':                '#000000',
'blue':                 '#0000FF',
'blueviolet':           '#8A2BE2',
'brown':                '#A52A2A',
'burlywood':            '#DEB887',
'cadetblue':            '#5F9EA0',
'chartreuse':           '#7FFF00',
'chocolate':            '#D2691E',
'crimson':              '#DC143C',
'cyan':                 '#00FFFF',
'darkblue':             '#00008B',
'darkcyan':             '#008B8B',
'darkgoldenrod':        '#B8860B',
'darkgray':             '#A9A9A9',
'darkgreen':            '#006400',
'darkkhaki':            '#BDB76B',
'darkmagenta':          '#8B008B',
'darkolivegreen':       '#556B2F',
'darkorange':           '#FF8C00',
'darkorchid':           '#9932CC',
'darkred':              '#8B0000',
'darksalmon':           '#E9967A',
'darkseagreen':         '#8FBC8F',
'darkslateblue':        '#483D8B',
'darkslategray':        '#2F4F4F',
'darkturquoise':        '#00CED1',
'darkviolet':           '#9400D3',
'deeppink':             '#FF1493',
'deepskyblue':          '#00BFFF',
'dimgray':              '#696969',
'dodgerblue':           '#1E90FF',
'firebrick':            '#B22222',
'forestgreen':          '#228B22',
'fuchsia':              '#FF00FF',
'gainsboro':            '#DCDCDC',
'gold':                 '#FFD700',
'goldenrod':            '#DAA520',
'gray':                 '#808080',
'green':                '#008000',
'greenyellow':          '#ADFF2F',
'honeydew':             '#F0FFF0',
'hotpink':              '#FF69B4',
'indianred':            '#CD5C5C',
'indigo':               '#4B0082',
'lavenderblush':        '#FFF0F5',
'lawngreen':            '#7CFC00',
'lemonchiffon':         '#FFFACD',
'lime':                 '#00FF00',
'magenta':              '#FF00FF',
'maroon':               '#800000',
'mediumaquamarine':     '#66CDAA',
'mediumblue':           '#0000CD',
'mediumseagreen':       '#3CB371',
'mediumslateblue':      '#7B68EE',
'mediumspringgreen':    '#00FA9A',
'mediumturquoise':      '#48D1CC',
'mediumvioletred':      '#C71585',
'midnightblue':         '#191970',
'mistyrose':            '#FFE4E1',
'moccasin':             '#FFE4B5',
'navy':                 '#000080',
'olive':                '#808000',
'olivedrab':            '#6B8E23',
'orange':               '#FFA500',
'orangered':            '#FF4500',
'orchid':               '#DA70D6',
'peru':                 '#CD853F',
'pink':                 '#FFC0CB',
'purple':               '#800080',
'red':                  '#FF0000',
'rosybrown':            '#BC8F8F',
'royalblue':            '#4169E1',
'saddlebrown':          '#8B4513',
'salmon':               '#FA8072',
'sandybrown':           '#FAA460',
'skyblue':              '#87CEEB',
'slateblue':            '#6A5ACD',
'slategray':            '#708090',
'springgreen':          '#00FF7F',
'steelblue':            '#4682B4',
'tan':                  '#D2B48C',
'teal':                 '#008080',
'thistle':              '#D8BFD8',
'tomato':               '#FF6347',
'turquoise':            '#40E0D0',
'violet':               '#EE82EE',
'yellow':               '#FFFF00',
'yellowgreen':          '#9ACD32'}

matplotlib.rcParams.update({'font.size': 10})

SNP_input = sys.stdin

Patient_dict = collections.defaultdict(list)
Sample_SNP_dict = collections.defaultdict(list)
Patient_case_or_control = dict()

# skip_header = True
# with open('SF_Peds_Patient_IDs.txt','r') as PatientIDs:
# 	for line in PatientIDs:
# 		if skip_header:
# 			skip_header = False
# 			continue
# 		fields = line.split('\t')
# 		fields = [x.rstrip() for x in fields]
# 		Patient_dict[fields[1]].append(fields[0])
# 		Patient_case_or_control[fields[1]] = fields[3].split()[0]

header_saved = False
Sample_meta_dict = collections.defaultdict(list)
samples_deemed_passable = []
poss_pass = ['SU95-70-49', 'OH69-83-36', 'AQ42-75-79', 'ES41-82-06', 'SR06-03-41',
'LA95-28-73', 'OT05-30-95', 'KK74-16-18', 'PB47-02-86', 'JN33-20-96']
with open('SFPeds_all_outputBySample_151022_FINAL.txt','r') as outputBySample:
	for line in outputBySample:
		fields = line.split('\t')
		fields = [x.rstrip() for x in fields]
		#print(fields)
		if header_saved == False:
			header = fields
			header_saved = True
			continue
		sampleName = str(fields[8][:12]+"@"+fields[58])
		if 'HRZ' in sampleName or 'NIST' in sampleName:
			continue
		try:
			if fields[6].startswith('Passable') and fields[7].split()[0]=='TRUE':
				samples_deemed_passable.append(sampleName)
		except IndexError:
			pass
		Patient_dict[fields[9]].append(sampleName)
		print(fields)
 		Patient_case_or_control[fields[9]] = fields[21].split()[0]
		for num,cell in enumerate(fields):
			if header[num].lstrip() == 'RESULTQCFAIL':
				try:
					Sample_meta_dict[sampleName].append(round(float(cell),4))
				except ValueError:
					Sample_meta_dict[sampleName].append(cell)
			if header[num] == 'pass':
				Sample_meta_dict[sampleName].append(cell)
			if header[num] == 'QC Failure Reason':
				Sample_meta_dict[sampleName].append(cell)
			if header[num] == 'COVERAGEVARIABILITY':
				try:
					Sample_meta_dict[sampleName].append(round(float(cell),3))
				except ValueError:
					Sample_meta_dict[sampleName].append(cell)
			if header[num] == 'RECIPIENTHOMOCOUNTS':
				Sample_meta_dict[sampleName].append(cell)
			if header[num].lstrip() == 'FRACZEROS':
				try:
					Sample_meta_dict[sampleName].append(round(float(cell),3))
				except ValueError:
					Sample_meta_dict[sampleName].append(cell)
			if header[num].lstrip() == 'RECIPIENTHETEROPERCENT':
				try:
					Sample_meta_dict[sampleName].append(round(float(cell),3))
				except ValueError:
					Sample_meta_dict[sampleName].append(cell)
print(Sample_meta_dict.items())

skip_header = True
for line in SNP_input:
	if skip_header:
		skip_header = False
		continue
	fields = line.split('\t')
	fields = [x.rstrip() for x in fields]
	sampleName = fields[1]+"@"+fields[0]
	# if 'Redo' in fields[0]:
	# 	sampleName = sampleName+'_2'
	#SNP_ID = int(fields[3][5:])
	SNP_ID = fields[3]
	try:
		adjFreq = float(fields[32])
	except ValueError:
		continue
	Sample_SNP_dict[sampleName].append([SNP_ID,adjFreq])
#print(Sample_SNP_dict.items()[0])
sorted_PatientIDs = sorted(Patient_dict.items(), key=operator.itemgetter(0))

# test = 0
with matplotlib.backends.backend_pdf.PdfPages("/Users/jcollins/cfDNA/Stanford_Peds_Case_Control_waterfall_plots_deemed_passable_with_rsltNoDropouts.pdf") as pdf:
	color_set = random.sample(ext_colors,26)
	# plot each sample in patient ID group
	splot_index = 0
	fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
	subplots = (ax1, ax2, ax3, ax4)
	for splot in subplots:
	# splot.plot(mean_x_axis, mean_adjFreqs, marker='.', linestyle='--', linewidth=3.0, color='black', 
	# 			      label="Mean of samples that pass QC", alpha=0.95)
		splot.set_ylim(-0.005,.11)
		splot.set_xlim(-1,266)
		splot.set_xlabel("SNP Index")
		splot.set_ylabel("Alternate Allele Frequency")
	for patientID,samples in sorted_PatientIDs:
		# test += 1
		# if test > 5:
		# 	break
		# if patientID != 'P29':
		# 	continue

		# plot each sample in patient ID group
		# splot_index = 0
		# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
		# subplots = (ax1, ax2, ax3, ax4)
		# for splot in subplots:
		# # splot.plot(mean_x_axis, mean_adjFreqs, marker='.', linestyle='--', linewidth=3.0, color='black', 
		# # 			      label="Mean of samples that pass QC", alpha=0.95)
		# 	splot.set_ylim(-0.005,.11)
		# 	splot.set_xlim(-1,266)
		# 	splot.set_xlabel("SNP Index")
		# 	splot.set_ylabel("Alternate Allele Frequency")
		# color_set = (random.sample(basic_colors,15) if len(samples)<16 else random.sample(ext_colors,26))
		SNP_dict = collections.defaultdict(list)
		SNP_sample_dict = dict()
		for sample in samples:
			#print(sample)
			SNP_data = [x for x in Sample_SNP_dict[sample]]
			# calculate mean adjFreq only from samples that pass QC 
			#print(Sample_meta_dict[sample])
			for SNP in SNP_data:
				if Sample_meta_dict[sample][1] == 'TRUE':# and sample.startswith('OH70')==False:
					SNP_dict[SNP[0]].append(SNP[1])
				SNP_sample_dict[sample+SNP[0]] = SNP[1]
			# normalized x-axis 
			# sorted_SNP_data = sorted(SNP_data, key=operator.itemgetter(1), reverse=True)
			# SNP_axis = range(1,len(sorted_SNP_data)+1)
			# norm_SNP_axis = [x/mplt(SNP_axis) for x in SNP_axis]
			# adjFreqs = [x[1] for x in sorted_SNP_data]
			# # print(sorted_SNP_data)
			# # print(SNP_axis)
			# # print(adjFreqs)
			# plt.plot(norm_SNP_axis,adjFreqs, marker='o', linestyle='-', linewidth=5.0, color=color_set.pop(), label=sample, alpha=0.5)

		SNP_axis = dict()
		for SNP,freqs in SNP_dict.items():
			SNP_axis[SNP] = np.mean(freqs)
		# print(SNP_axis.items())
		# print(SNP_dict.items())
		sorted_SNP_axis = sorted(SNP_axis.items(), key=operator.itemgetter(1), reverse=True)
		# print(sorted_SNP_axis)
		sorted_samples = sorted(Sample_meta_dict.items(), key=lambda x: x[0])#, reverse=True)
		sorted_samples.sort(key=lambda x: x[1][1], reverse=True)
		# print(sorted_samples)

		# plot mean of all samples that pass QC
		mean_x_axis = [] # must be same order for all samples, which is 'sorted_SNP_axis'
		mean_adjFreqs = []
		x_pt = 0
		for SNP_ID in sorted_SNP_axis:
			x_pt += 1
			mean_adjFreqs.append(SNP_ID[1])
			mean_x_axis.append(x_pt)

		sample_count = 0
		for sample_meta in sorted_samples:
			sample = sample_meta[0]
			if sample not in samples:
				continue	
			if sample not in samples_deemed_passable:
				continue
			sample_count += 1	
			### individual plotting 
			# fig = plt.figure()
			# title = "Patient {} {}".format(patientID,Patient_case_or_control[patientID])
			# plt.title(title)
			# plt.xlabel("SNP Index")
			# plt.ylabel("Alternate Allele Frequency")
			# color_set = (random.sample(basic_colors,15) if len(samples)<16 else random.sample(ext_colors,26))
			# x_axis = [] # must be same order for all samples, which is 'sorted_SNP_axis'
			# adjFreqs = []
			# x_pt = 0
			# for SNP_ID in sorted_SNP_axis:
			# 	x_pt += 1
			# 	adjFreqs.append(SNP_ID[1])
			# 	x_axis.append(x_pt)
			# plt.plot(x_axis, adjFreqs, marker='.', linestyle='--', linewidth=3.0, color='black', 
			#       label="Mean of samples that pass QC", alpha=0.95)

			# unpack sample meta information
			ResultQCF = Sample_meta_dict[sample][0]
			smplPass = Sample_meta_dict[sample][1]
			failReason = Sample_meta_dict[sample][2]
			CovVar = Sample_meta_dict[sample][3]
			RhomoCounts = Sample_meta_dict[sample][5]
			FZ = Sample_meta_dict[sample][4]
			RHetPerc = Sample_meta_dict[sample][6]
			# if Sample_meta_dict[sample][1] == 'FALSE' and Sample_meta_dict[sample][2] > 1.2:
			# 	continue
			x_axis = [] # must be same order for all samples, which is 'sorted_SNP_axis'
			adjFreqs = []
			RecHomoFreqs = []
			x_pt = 0
			drouts = 0
			isDrout = False
			for SNP_ID in sorted_SNP_axis:
				x_pt += 1
				try:
					#print(SNP_sample_dict[sample+SNP_ID[0]])
					curr_freq = SNP_sample_dict[sample+SNP_ID[0]]
					adjFreqs.append(curr_freq)
					x_axis.append(x_pt)
					if SNP_ID[1] > 0.25:
						if curr_freq < 0.1:
							isDrout = True
							drouts += 1
					if isDrout==False and SNP_ID[1]<0.1 and curr_freq<0.1:
						RecHomoFreqs.append(curr_freq)
					isDrout = False
				except KeyError:
					continue

			# calculate dd-cfDNA after removing RecHet dropouts
			NinetyFifthPercentile = np.percentile(RecHomoFreqs,95)
			print(len(RecHomoFreqs))
			for freq in RecHomoFreqs:
				if freq >= NinetyFifthPercentile:
					RecHomoFreqs.remove(freq)
			print(len(RecHomoFreqs))
			rsltNoDrouts = np.mean(RecHomoFreqs)*2.111111111


			#print(adjFreqs)
			print("{}\t{}".format(sample,drouts),file=sys.stderr)
			if smplPass == 'TRUE':
				#continue
				subplots[splot_index].plot(x_axis, adjFreqs, marker='.', linestyle='-', linewidth=3.0, color=color_set.pop(), alpha=0.65,
					label="- {}, Pass={}\n    CovVar={}, RHomo={}, RHetPerc={},\n    ResultQCF={}, FracZero={}  ".format(sample,smplPass,CovVar,RhomoCounts,RHetPerc,ResultQCF,FZ))
				subplots[splot_index].set_title("Patient {} {}".format(patientID,Patient_case_or_control[patientID]))
				subplots[splot_index].legend(loc='upper right',prop={'size':6.5}, framealpha=0.75)
				subplots[splot_index].plot(mean_x_axis, mean_adjFreqs, marker='.', linestyle='--', linewidth=3.0, color='black', 
		 			      label="Mean of samples that pass QC", alpha=0.95, zorder=1)
				splot_index += 1
				# plt.plot(x_axis, adjFreqs, marker='.', linestyle='-', linewidth=3.0, color=color_set.pop(), 
				# 	      label="- {}, Pass={}, CovVar={},\n    RHomo={}, ResultQCF={}".format(sample,smplPass,CovVar,RhomoCounts,ResultQCF), alpha=0.65)
			elif smplPass == 'FALSE':
				#splot_index = 1
				subplots[splot_index].plot(x_axis, adjFreqs, marker='.', linestyle='-', linewidth=3.0, color=color_set.pop(), alpha=0.65,
					label="- {}\n  CovVar={}, RHomo={}, RHetPerc={},\n  ResultQCF={}, FracZero={}, Dropouts={}\n Pass={}, QC Fail Reasons:\n    {}\n Result without dropouts: {}".format(sample,
																												CovVar,RhomoCounts,RHetPerc,ResultQCF,FZ,drouts,smplPass,failReason,rsltNoDrouts))
				subplots[splot_index].set_title("Patient {} {}".format(patientID,Patient_case_or_control[patientID]))
				subplots[splot_index].legend(loc='upper right',prop={'size':6.5}, framealpha=0.75)
				subplots[splot_index].plot(mean_x_axis, mean_adjFreqs, marker='.', linestyle='--', linewidth=3.0, color='black', 
		 			      label="Mean of samples that pass QC", alpha=0.95, zorder=1)
				splot_index += 1
				# plt.plot(x_axis, adjFreqs, marker='.', linestyle='-', linewidth=3.0, color=color_set.pop(), 
				# 	      label="- {}, Pass={}, CovVar={},\n    RHomo={}, ResultQCF={}\n  QC Fail Reasons:\n    {}".format(sample,smplPass,CovVar,RhomoCounts,
				# 	      																									ResultQCF,failReason), alpha=0.65)
			else:
				continue
				plt.plot(x_axis, adjFreqs, marker='.', linestyle='-', linewidth=3.0, color=color_set.pop(), 
					      label="- {}, ResultQCF={}".format(sample,ResultQCF), alpha=0.65)

			# plt.ylim(-0.01,.11)
			# plt.xlim(50,266)
			# plt.legend(loc='upper right',prop={'size':6})
			# plt.grid(b=True, which='major', color='gray', linestyle='-', alpha=0.7)
			# plt.grid(b=True, which='minor', color='gray', linestyle='--', alpha=0.7)
			# pdf.savefig()
			# plt.close(fig)

			if splot_index == 4:# and sample_count != len(samples):
				# ax1.set_ylim(-0.01,.071)
				# ax1.set_xlim(50,266)
				# plt.legend(loc='upper right',prop={'size':6})
				# plt.grid(b=True, which='major', color='gray', linestyle='-', alpha=0.7)
				# plt.grid(b=True, which='minor', color='gray', linestyle='--', alpha=0.7)
				pdf.savefig()
				plt.close(fig)
				splot_index = 0
				fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
				subplots = (ax1, ax2, ax3, ax4)
				for splot in subplots:
					# splot.plot(mean_x_axis, mean_adjFreqs, marker='.', linestyle='--', linewidth=3.0, color='black', 
					# 	      label="Mean of samples that pass QC", alpha=0.95)
					splot.set_ylim(-0.005,.11)
					splot.set_xlim(-1,266)
					splot.set_xlabel("SNP Index")
					splot.set_ylabel("Alternate Allele Frequency")
				#color_set = (random.sample(basic_colors,15) if len(samples)<16 else random.sample(ext_colors,26))
				#color_set = random.sample(best_colors,22)


	pdf.savefig()
	plt.close(fig)








