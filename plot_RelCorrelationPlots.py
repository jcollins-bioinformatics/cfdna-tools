#!/usr/bin/env python2.7
""" Log-log correlation plots for Relationship Study tertiary
	pipeline dd-cfDNA results vs. expected. 
"""

from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as backend_pdf
import matplotlib.font_manager as font_manager
from matplotlib.ticker import FuncFormatter
import matplotlib
import numpy as np
from operator import itemgetter
import os
import palettable
import pandas as pd
import re
from scipy.interpolate import UnivariateSpline
from scipy import stats as scistats 
import seaborn as sns
import sys
import time
import UniversalUtilities as univ

sns.set(rc={'axes.facecolor': '#F2F2F2'})
path = '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/matplotlib/mpl-data/fonts/ttf/Helvetica.ttf'
prop = font_manager.FontProperties(fname=path)
matplotlib.rcParams['font.family'] = prop.get_name()

# Keep track of time & space 
init_time = time.time()
univ.printPeriodicTime()
currDate = int(time.strftime("%y%m%d"))
cwd = os.getcwd() # directory where command was entered
script_path = sys.path[0] # directory where script is saved 

# Filter Relationship Study merged data by SampleName Index 
df = pd.read_csv(cwd+'/NIPT_outputBySample_withRecalc.txt', sep='\t')
df.set_index('SAMPLENAME', inplace=True)
df = df[df.PASS] # N = 120
# df['Expected %dd-cfDNA'] = df['Expected %dd-cfDNA'].map(lambda x: float(re.sub('%', '', x))/100.0)
# df['Donor Relationship ID'] = df['Donor Relationship ID'].map(lambda x: ' '.join(x.split()[:2]))
df = df[df['DONORRELATIONSHIPDESCRIPTION']=='Parent']

# Collect vectors for linear regressions calc
rel_results = df.RESULT.values
# rel_expected = df['Expected %dd-cfDNA'].values
# rel_posCntrlRecalc = df['dd-cfDNA_cntrlTrim'].values
rel_noTrim_m4p0 = df['dd-cfDNA_noTrim_m4.0'].values
# rel_noTrim_m4p5 = df['dd-cfDNA_noTrim_m4.5'].values
# rel_trim99p9_m4 = df['dd-cfDNA_trim99p9_m4.0'].values

# Dict to match samples with siblings panel
smpl_PanelDict = defaultdict(list)
for k,v in zip(df.index, df.index):
	smpl_PanelDict[k].append(v)

num_smpls = univ.lenAllDictValues(smpl_PanelDict)
print(num_smpls)

colors = sns.blend_palette(univ.best_spectrum, num_smpls)
with backend_pdf.PdfPages(cwd+'/NIPT_noRecHomoTrim_mult4p0.pdf') as pdf:

	x_vals = rel_results

	fig = plt.figure()
	# fig.subplots_adjust(top=0.15)
	plt.xlim(0.005, 0.13)
	plt.ylim(0.005, 0.13)
	plt.ylabel("dd-cfDNA result_recalc\nRecHomo_trim: none, Mult.: 4.0", labelpad=15, fontsize=14, fontweight='bold')
	plt.xlabel("dd-cfDNA result (PassQC=True)\nRecHomo_trim: top 5%, Mult.: 4.22", labelpad=15, fontsize=14, fontweight='bold')
	plt.yticks(fontsize=14)#, fontweight='bold')
	plt.xticks(fontsize=14)#, fontweight='bold')
	plt.title("NIPT, (N={})\n No trimming vs. standard".format(len(df['RESULT'].values)), fontsize=16, fontweight='bold')
	# plt.title("RecHomo trimming: none, Multiplier: 4.0", fontsize=12, fontweight='bold')

	# Simple linear regression, R^2
	slope, intercept, r_value, p_value, std_err = scistats.linregress(x_vals, rel_noTrim_m4p0)

	# Plot tertiary dd-cfDNA results vs. expected
	for panel, grp_smpls in sorted(smpl_PanelDict.items(), key=itemgetter(0)):
		y_results = [df.loc[smpl, 'dd-cfDNA_noTrim_m4.0'] for smpl in grp_smpls]
		indep_results = [df.loc[smpl, 'RESULT'] for smpl in grp_smpls]
		sorted_results = sorted(zip(indep_results, y_results), key=itemgetter(0))
		y_results = [x[1] for x in sorted_results]
		indep_results = [x[0] for x in sorted_results]
		# noTrim_results = 
		color = colors.pop()
		plt.scatter(indep_results, y_results, zorder=3, facecolors='none', edgecolors=color, marker='o', alpha=0.95, s=50, label="{}".format(panel), 
					linewidth=2.5)#facecolors='none',

	# Calculate smooth line
	spl = UnivariateSpline(x_vals, rel_noTrim_m4p0)
	xs = np.linspace(min(x_vals), max(x_vals), 1000)
	spl.set_smoothing_factor(0.5)
	plt.plot(xs, spl(xs), 'k--', lw=1.25, zorder=5, alpha=0.9)
	plt.plot(xs, spl(xs), '--', color='white', lw=2.5, zorder=4, alpha=0.6)

	plt.plot([0.0001, 0.5], [0.0001, 0.5], 'k-', lw=0.5, zorder=1)
	plt.plot([0.001, 0.25], [0.001*slope + intercept, 0.25*slope + intercept], 'k--', lw=1.0, label='$R^2$ = {}'.format(round(r_value**2,5)), zorder=2, alpha=0.0)

	plt.gca().set_xscale('log')
	plt.gca().set_yscale('log')
	plt.gca().set_aspect('equal')

	leg = plt.legend(loc='upper left', prop={'size':8, 'weight':'bold'}, frameon=False, framealpha=0.5, bbox_to_anchor=(1,1))
	leg.get_frame().set_facecolor('white')
	leg.get_frame().set_linewidth(0.75)
	leg.get_frame().set_edgecolor('k')

	# Create the formatter using the function to_percent. This multiplies all the
	# default labels by 100, making them all percentages
	formatter = FuncFormatter(univ.to_percent)
	# Set the formatter
	plt.gca().yaxis.set_major_formatter(formatter)
	plt.gca().xaxis.set_major_formatter(formatter)
	plt.grid(b=True, which='major', color='gray', linestyle='-', alpha=0.5, zorder=2, lw=0.5)
	# plt.grid(b=True, which='minor', color='gray', linestyle='-', alpha=0.2, lw=0.5)

	# # Hide the right and top spines
	# plt.gca().spines['right'].set_visible(False)
	# plt.gca().spines['top'].set_visible(False)
	# # Only show ticks on the left and bottom spines
	plt.gca().yaxis.set_ticks_position('left')
	plt.gca().xaxis.set_ticks_position('bottom')

	plt.gca().tick_params('both', length=3, width=0.5, which='major', direction='out')
	# plt.gca().tick_params('both', length=4, width=1, which='minor', direction='out')

	# sns.despine(ax=plt.gca(), offset=10, trim=True)
	fig.tight_layout()

	pdf.savefig()
	plt.close(fig)


