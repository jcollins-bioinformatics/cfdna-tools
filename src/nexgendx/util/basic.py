""" A widely applicable module defining functions expected to be
    useful for bioinformatics analysis scripts. 
"""
from __future__ import division, print_function
from collections import Counter, defaultdict
from datetime import datetime 
from functools import wraps
from itertools import chain
from math import log, sqrt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.font_manager import FontProperties
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import FuncFormatter
from operator import itemgetter 
from scipy.interpolate import UnivariateSpline
from scipy.stats import binom, norm, poisson
# import plotly
# import seaborn as sns   
import datetime
import django
import ggplot
import matplotlib as mpl
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import random
import re
import sys
import time, timeit
import warnings 

    


### FUNCTIONS
def deprecated(func):
    '''This is a decorator which can be used to mark functions
       as deprecated. It will result in a warning being emitted
       when the function is used. Licensed by PacBio.'''
    def new_func(*args, **kwargs):
        if not new_func.__called:
            warnings.warn('Call to deprecated function "{0}".'.format(func.__name__),
                          stacklevel=2)
            new_func.__called = True
        return func(*args, **kwargs)
    new_func.__name__ = func.__name__
    new_func.__doc__ = func.__doc__
    new_func.__dict__.update(func.__dict__)
    new_func.__called = False
    return new_func

def get_duplicates(input_list):
    '''Count the number of occurences for items in list and return as 
       tuple.'''
    count_dict = Counter(input_list) 
    return [(item,count) for item,count in count_dict.iteritems() if count > 1]  

def get_tert_by_sample(Oracle_con):
    '''Uses received cx_Oracle connection object to download and merge
       the AlloSure tertiary outputBySample T1 & T2 files.'''
    df_T1 = pd.read_sql_query("select * from CFDNA_SAMPLE_RESULT_T1", Oracle_con)
    df_T2 = pd.read_sql_query("select * from CFDNA_SAMPLE_RESULT_T2", Oracle_con)
    df = pd.merge(df_T1, df_T2, on=['SAMPLENAME', 'RUN_ID'])
    return df  

def pandas_markdown_df(df, columns):
    '''Export pandas DataFrame as HTML file.'''
    html_table = df.to_html(max_cols=15, justify='right', header=None, 
                            names=columns)
    return html_table

def print_progress(message, init, n_smpls):
    '''Print to sys.stderr execution time & given update message.'''
    banner = " # "*25
    print("\n{:^150s}\n\n{:^150s}\n{:^150s}\n\n{:^150s}\n".format(banner, 
          message+str(round(time.time()-init,5))+" s", "N(smpls) = " + 
          str(n_smpls), banner), file=sys.stderr)

def print_sample_stats(df, use_this_cols):
    '''Print pd.DataFrame description stats for core columns.'''
    df = df.loc[:,use_these_cols]
    # \033[95m  \033[0m
    print("\n\n\033[31m{:^150s}\033[0m\n\n".format(
          " * "*5+"      "+' '.join([x for x in 'Sample Stats']) 
          + "      "+" * "*5), 
          file=sys.stderr)
    print(df.describe(include='all',), file=sys.stderr)

def sort_dict(input_dict, index=0):
    '''Return dictionary as list of tuples sorted by keys.'''
    return sorted(input_dict.iteritems(), key=itemgetter(index))

def to_percent(y, position):
    '''Use with matplotlib FuncFormatter to convert an axis label to 
       percent unit (%).'''
    s = str(100 * y)
    return s + '%'

te

def use_Helvetica():
    '''Use Helevetica as matplotlib default font type instead of 
       Bitstream Vera Sans. Returned object must be given to 
       mpl.FuncFormatter.'''
    prop = mpl.font_manager.FontProperties(fname=path)
    return prop.get_name()


### COLOR PALETTES

spectrum1 = [(0.725467917633003, 0.10980392156862745, 0.2196078431372549),
'#1e488f', '#be03fd', (0.44313725490196076, 0.44313725490196076,
0.88627450980392153), '#75bbfd', '#48E4BA', '#C4E448', '#f1da7a',  '#fac205',
(0.66666666666666674, 0.66666666666666663, 0.29078014184397138)]

headings1 = 
{
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

headings2 = 
{
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
