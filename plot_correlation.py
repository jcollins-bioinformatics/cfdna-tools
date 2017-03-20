#!/usr/bin/env python2.7

from __future__ import division
from collections import defaultdict
import math
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as backend_pdf
from matplotlib.ticker import FuncFormatter
import matplotlib
import numpy as np
import operator 
import re
from scipy import stats as scistats 
import seaborn as sns
import sys


sns.set(font_scale=1.6, style='ticks') 
matplotlib.rcParams.update({'font.size': 16})#, 'marker.linewidth': 10.0})

disc_patients = ['P2', 'P02', 'P3', 'P03', 'P4', 'P04', 'P11', 'P20']

def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)
    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] is True:
        return s + r'$\%$'
    else:
        return s + '%'



AS_results = []
SG_results = []
AS_results_b3 = []
SG_results_b3 = []
with open('/Users/jcollins/cfDNA/Stanford Peds/Batch 3 analysis/SF_Peds_AlloSure_with_JFB_Shotgun_batch3update.txt', 'r') as AS_vs_SG:	
	header_saved = False
	for i,line in enumerate(AS_vs_SG):
		fields = [x.strip() for x in line.split('\t')]
		# print(fields)
		if header_saved == False:
			header = fields
			header_saved = True
			continue
		for num,cell in enumerate(fields[:len(header)]):
			if header[num] == 'Patient_ID+Timepoint':
				PID_tp = cell
			if header[num] == 'RUNNAME':
				run_ID = cell
			if header[num] == 'RESULTQCFAIL':
				AS_result = cell
			if header[num] == 'Error':
				SG_error = cell
			if header[num] == 'Counts-T':
				SG_countsT = cell
			if header[num] == 'Diff':
				SG_result = cell

		try:
			AS_result = float(AS_result)
			SG_result = float(SG_result)/100
			run_ID = int(run_ID[:6])
			SG_countsT = int(SG_countsT)
			SG_error = float(SG_error)
		except ValueError:
			continue	
		# if PID_tp.startswith(tuple(disc_patients)):
		# 	continue	
		if SG_countsT < 1000 or SG_error > 0.15:# or AS_result > 0.05:
			continue
		# if AS_result < 0.0037 or AS_result > 0.05:
		# 	continue
		if run_ID < 160500:
			AS_results.append(AS_result)
			SG_results.append(SG_result)
		else:
			AS_results_b3.append(AS_result)
			SG_results_b3.append(SG_result)


print(AS_results)
print(SG_results)


with backend_pdf.PdfPages('/Users/jcollins/cfDNA/Stanford Peds/Batch 3 analysis/SF_Peds_ASvsSG_batch3update_correlation_plot_n1pmin.pdf') as pdf:

	fig = plt.figure()

	plt.xlim(-0.01, 0.25)
	plt.ylim(-0.01, 0.25)
	plt.ylabel("AlloSure results", labelpad=15)
	plt.xlabel("Shotgun results", labelpad=15)
	plt.yticks(fontsize=16)
	plt.xticks(fontsize=16)

	# plt.gca().set_aspect('equal')

	slope, intercept, r_value, p_value, std_err = scistats.linregress([SG_results+SG_results_b3], [AS_results+AS_results_b3])
	# slope, intercept, r_value, p_value, std_err = scistats.linregress([SG_results_b3], [AS_results_b3])
	# linRegLine = []
	# linRegLine.append(0.001*slope + intercept)
	# for x in SG_results:
	# 	linRegLine.append(slope*x + intercept)

	plt.scatter(SG_results, AS_results, marker='o', color='k', alpha=0.8, s=80, zorder=3)
	plt.scatter(SG_results_b3, AS_results_b3, marker='o', color='r', alpha=0.8, s=80, zorder=3)#, label="May 2016 - Batch 3")

	plt.plot([-0.01, 0.25], [-0.01, 0.25], 'k-', lw=0.5, zorder=1)
	plt.plot([-0.01, 0.25], [intercept, 0.25*slope+intercept], 'b-', lw=1.0, label='$R^2$ = {}'.format(round(r_value**2,3)), zorder=2)

	# plt.gca().set_xscale('log')
	# plt.gca().set_yscale('log')

	plt.legend(loc='upper left', prop={'size':14})

	plt.title("AS vs. SG overlap, N = {}".format(len(AS_results+AS_results_b3)))
	# plt.title("AS vs. SG overlap, N = {}".format(len(AS_results_b3)))


	# Create the formatter using the function to_percent. This multiplies all the
	# default labels by 100, making them all percentages
	formatter = FuncFormatter(to_percent)
	# Set the formatter
	plt.gca().yaxis.set_major_formatter(formatter)
	plt.gca().xaxis.set_major_formatter(formatter)

	plt.grid(b=True, which='major', color='gray', linestyle='-', alpha=0.5, zorder=2, lw=0.5)
	plt.grid(b=True, which='minor', color='gray', linestyle='-', alpha=0.25, lw=0.5)

	# # Hide the right and top spines
	# plt.gca().spines['right'].set_visible(False)
	# plt.gca().spines['top'].set_visible(False)
	# # Only show ticks on the left and bottom spines
	plt.gca().yaxis.set_ticks_position('left')
	plt.gca().xaxis.set_ticks_position('bottom')

	# plt.gca().tick_params('both', length=7, width=2, which='major')#, direction='out')

	# sns.despine(ax=plt.gca(), offset=10, trim=True)

	fig.tight_layout()

	pdf.savefig()
	plt.close(fig)


