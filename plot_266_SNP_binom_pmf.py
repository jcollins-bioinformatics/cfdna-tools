from __future__ import division, print_function
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as backend_pdf
import matplotlib.mlab as mlab
from matplotlib.ticker import FuncFormatter
import matplotlib.font_manager as font_manager
import numpy as np
import os
from scipy.stats import binom, norm, poisson
import seaborn as sns
import sys

sns.set(rc={'axes.facecolor': '#ECECEC'})
cwd = os.getcwd()

# pmf = Probability mass functions:
#       Gives the exact probabillity of finding a particular value or 
#       permutation of values for any k in {0,1,...,N}
# ppf = Percent point functions:
#       return the x-axis 'k' discrete interval corresponding to
#       given probability percentile on the distribution 

with backend_pdf.PdfPages(cwd+
    '/n=180_SNP-zygos-binom-pmf_norm-poisson-approx_t2.pdf') as pdf:
    
    fig, ax1 = plt.subplots()
    plt.xlim(-5,271)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=12)
    plt.xlabel(r'Number of SNPs with shared zygosity'
         '\n'r'$f(x;n,p)=\Pr(X=x)=\frac{n!}{x!(n-x)!} * p^{x}(1-p)^{n-x}$'
         '\n'r'$from$ $\{x \in N : 0 \leq x \leq n \},$ $where$ '
         r'$N=\{0,1,2,...,266\}$', labelpad=15, fontsize=14, fontweight='bold')
    plt.ylabel(r"$\Pr(x)$", labelpad=15, fontsize=16)

    n, p = 180, 0.5

    # 1)
    # BINOMIAL PMF
    mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
    x = np.arange(0,n+1)
    binom_pmf = binom.pmf(x, n, p)
    plt.ylim(min(binom_pmf)*1e-1, 10)
    print(x)
    print(len(x))
    stddev = binom.std(n, p, loc=0)
    ax1.vlines(x, min(binom_pmf), binom.pmf(x, n, p), colors='k', lw=1.5, 
        alpha=0.15, zorder=2)
    x_99 = np.arange(binom.ppf(0.005, n, p),binom.ppf(0.995, n, p)+1)
    # Shade darker discrete interval where area contains 99% inner values
    ax1.vlines(x_99, min(binom_pmf), binom.pmf(x_99, n, p), color='k', lw=2, alpha=0.15, zorder=2)
    ax1.plot(x, binom_pmf, 'o', mfc='none', ms=7, mec='blue', mew=0.8, 
        alpha=0.8, zorder=3,
        label='\nbinom pmf\n'r'$\mu = {}$'.format(mean)+'\n'r'$\sigma (x) \approx {}$'.format(round(stddev,2))+'\n'r'$\sum_{i=73}^{107} x_i = 0.99$')
            # Note: summation range must be manually entered 
    print(x_99)
    for tl in ax1.get_yticklabels():
        tl.set_color('darkblue')

    # 2)
    # NORMAL PDF    
    # with mu, sigma from binom pmf (optional linear secondary y axis scale) 
    ax2 = ax1.twinx()
    ax2.plot(x, mlab.normpdf(x, mean, stddev),
        'r-', lw=2, alpha=0.9, zorder=4, label='norm pdf approx.\n'
        r'$\{\mu=90, \sigma\approx6.7; x \in \mathbb{R} : 0 \leq x \leq 180 \}$')

    # 3)
    # POISSON DIST from np.random 
    trials = int(10**8)
    rand_pois = np.random.poisson(mean, trials)
    # print(rand_pois)
    # plt.axvline(binom.ppf(1e-5,n,p), linewidth=3, color='k', linestyle='--', alpha=0.75, zorder=3)
    # plt.axvline(binom.ppf(1-1e-5,n,p), linewidth=3, color='k', linestyle='--', alpha=0.75, zorder=3)
    print(min(rand_pois),max(rand_pois))
    # print(binom.ppf(min(rand_pois),n,p),binom.ppf(max(rand_pois),n,p))
    hist_n, bins, patches = ax2.hist(rand_pois, histtype='bar', normed=True, bins=100, zorder=3, lw=0.5, fc=(0, 0, 0, 0), ec='g', label='Poisson random trials\n'+
        r'$\{\lambda=90, t=10^{8}; x \in \mathbb{Z} : 43 \lessapprox x \lessapprox 149 \}$')
            # Note: poisson distribution range must be manually entered 


    ax2.set_ylim(min(binom_pmf)*(1e-1), 10)
    ax2.set_xlim(-5,275)
    ax2.grid(b=False, axis='y')
    for tl in ax2.get_yticklabels():
        tl.set_color('r')
        tl.set_size(12)
    ax2.legend(loc='upper right', prop={'size':9, 'weight': 'bold'},
        framealpha=0.95)
    ax1.legend(loc='center right' ,prop={'size':12, 'weight': 'bold'}, 
        framealpha=0.95)
    plt.title("Probability mass function for: "r"$X$ $\backsim$ $Binomial(n={}, p=0.5)$".format(n), fontsize=14, fontweight='bold')
    ax1.yaxis.set_ticks_position('left')
    ax1.xaxis.set_ticks_position('bottom')
    ax1.tick_params('both', length=3, width=0.25, which='major', 
        direction='out')
    # ax1.gca().set_xscale('log')
    ax1.set_yscale('log')
    ax2.set_yscale('log')
    fig.tight_layout()
    pdf.savefig()
    plt.close(fig)


