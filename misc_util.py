from __future__ import print_function
from __future__ import division
from collections import Counter
import datetime
from functools import wraps
from itertools import chain
import matplotlib.font_manager as font_manager
# from matplotlib.ticker import FuncFormatter
from operator import itemgetter 
# import palettable
import pandas as pd
from scipy.interpolate import UnivariateSpline
from scipy.stats import linregress, ttest_ind
import sys
import time


# sns.set(rc={'axes.facecolor': '#F2F2F2'})
# df = pd.read_sql_query("select * from CFDNA_SAMPLE_RESULT_T1 where SAMPLENAME like '%CY38-10-77-16048B2-358B2%'", Oracle_con)
# df_bySmpl[df_bySmpl.index.str.startswith(tuple([x[0] for x in dups]))].to_csv(cwd+'/CARGOII_Seq01_duplicates_N=56.txt', sep='\t')

best_spectrum = [(0.725467917633003, 0.10980392156862745, 0.2196078431372549), '#1e488f', 
           '#be03fd', (0.44313725490196076, 0.44313725490196076, 0.88627450980392153), '#75bbfd', '#48E4BA', '#C4E448', '#f1da7a',  '#fac205', 
           (0.66666666666666674, 0.66666666666666663, 0.29078014184397138)]


# 1 
def get_tert_by_sample(Oracle_con):
    """return df"""
    df_T1 = pd.read_sql_query("select * from CFDNA_SAMPLE_RESULT_T1", Oracle_con)#, index_col=['SAMPLENAME'])
    df_T2 = pd.read_sql_query("select * from CFDNA_SAMPLE_RESULT_T2", Oracle_con)#, index_col=['SAMPLENAME'])
    # df_lab = pd.read_sql_query("select * from CFDNA_SAMPLE_INFO", Oracle_con, index_col=['SAMPLE_NAME'])
    # df_lab.rename(columns={'SAMPLE_NAME': 'SAMPLENAME'}, inplace=True)
    # df = pd.merge(df_T1, df_T2[df_T2.columns.difference(df_T1.columns)], left_index=True, right_index=True)
    df = pd.merge(df_T1, df_T2, on=['SAMPLENAME', 'RUN_ID'])
    # return pd.merge(df, df_lab[df_lab.columns.difference(df.columns)], how='outer', left_index=True, right_index=True, sort=True)
    return df

# 2
def use_Helvetica():
    """return prop.get_name()"""
    # path = '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/matplotlib/mpl-data/fonts/ttf/Helvetica.ttf'
    path = '/Users/jcollins/cfDNA/pyTools/Helvetica.ttf'
    prop = font_manager.FontProperties(fname=path)
    return prop.get_name()

# 3
def to_percent(y, position):
    """eturn s + '%'"""
    s = str(100 * y)
    return s + '%'

# 3
def len_all_dict_values(input_dict):
    """return len(list(chain(*input_dict.values())))"""
    return len(list(chain(*input_dict.values())))

# 4
def get_duplicates(input_list):
    """return [(item,count) for item,count in count_dict.iteritems() if count > 1]"""
    count_dict = Counter(input_list)
    return [(item,count) for item,count in count_dict.iteritems() if count > 1]

# 6
def sort_dict(input_dict, index=0):
    """return sorted(input_dict.iteritems(), key=itemgetter(index))"""
    return sorted(input_dict.iteritems(), key=itemgetter(index))

# 8
def print_sample_stats(df):
    """print("\n\n\033[31m{:^150s}\033[0m\n\n".format(" * "*5+"      "+' '.join([x for x in 'Sample Stats'])+"      "+" * "*5), file=sys.stderr)
    print(df.describe(include='all', percentiles=[0.05, 0.25, 0.5, 0.75, 0.95]), file=sys.stderr)"""
    use_these_cols = ['SEQUENCER', 'RUNNAME', 'EXPERIMENTNAME', 'TOTALCOVERAGE', 'COVERAGEVARIABILITY', 'NUMSNPSPASSQC', 'OVERALLBACKGROUND',
                     'RESULT', 'PASS']
    df = df.loc[:,use_these_cols]
    # \033[95m  \033[0m
    print("\n\n\033[31m{:^150s}\033[0m\n\n".format(" * "*5+"      "+' '.join([x for x in 'Sample Stats'])+"      "+" * "*5), file=sys.stderr)
    print(df.describe(include='all', percentiles=[0.05, 0.25, 0.5, 0.75, 0.95]), file=sys.stderr)

# 9
def print_progress(message, init, n_smpls):
    """print("\n{:^150s}\n\n{:^150s}\n{:^150s}\n\n{:^150s}\n".format(banner, message+str(round(time.time()-init,5))+" s", "N(smpls) = "+str(n_smpls), banner), file=sys.stderr)"""
    # banner = "   #  "*3+"  #  "*10+"  #   "*3
    banner = " # "*25
    print("\n{:^150s}\n\n{:^150s}\n{:^150s}\n\n{:^150s}\n".format(banner, message+str(round(time.time()-init,5))+" s", "N(smpls) = "+str(n_smpls), banner), file=sys.stderr)

# 10
def pandas_markdown_df(df, columns):
  """
  """
  # idxstats = pd.read_csv('./SH03-14-81a-2-83098.sorted.bam_idxstats.txt', sep='\t', header=None, names=['Chr', 'Mock chr length)', '# Mapped Reads', '# Unmapped Reads'])
  html_table = df.to_html(max_cols=15, justify='right', header=None, 
                          names=columns)
  return html_table



best_colors = {
# 'fuchsia':              '#FF00FF',
'darkorange':           '#FF8C00',
'darkorchid':           '#9932CC',
'dimgray':              '#696969',
'midnightblue':         '#191970',
'mediumblue':           '#0000CD',
'maroon':               '#800000',
# 'purple':               '#800080',
# 'crimson':              '#DC143C',
'goldenrod':            '#B8860B',
'darkgray':             '#A9A9A9',
'darkslateblue':        '#483D8B',
# 'darkslategray':        '#2F4F4F',
'darkred':              '#8B0000',
'red':                  '#FF0000',
# 'gold':                 '#FFFF00',
'yellowgreen':          '#ADFF2F',
'blue':                 '#0000FF',
}

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