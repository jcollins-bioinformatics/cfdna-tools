<img src="./doc/design/nexgendx_logo.png" width=60%>

<h1 align="left" underline=0 >diagnostic cell-free DNA<br/>
analysis tools
</h1>

```py
[bash]~$ python3
>>> import nexgendx as ngs
>>> # simple command prompt example
>>> tumor_genome = ngs.teraget(, con=ngs.sqlalcmy(...))
>>> # do more
>>> https://github.com/jcollins-bioinformatics/nexgendx/blob/master/README.md
>>> very 
>>> basic
>>> nice illustrative
>>> example 
>>> load / calc stats / visualize 
>>> :Dctrl+d
ctrl+c
```



<br>

<br>

1. Select a panel of SNPs using NCBI's dbSNP that have MAF's close to 50%
 - show binomial/Mendelian principles behind utility of MAF=~0.50 SNPs
 - output annotation information 
 - generate BED & FASTQ mapping reference file for these SNPs
2. Download selected panel-matching regions of genomes in NIST GIAB samples
 - create in silico "donor-derived" cf-DNA mixtures incorporating MNase-Seq data 
 + TSS annotations
 - "mix" fastqs (while introducing a variable error rate) at a series of dilutions
 - create mock three-genome contaminated sample(s) 
 - create both related (parent donates to child) and unrelated (CEU vs. other) spike-ins
 - create replication of varying coverage density and read uniqueness, and create
 sample replicates both for blanks & spike-ins 
3. Mapping & variant calling pipeline
 - etc
 - etc 
4. Tertiary analysis 
 - 
 -
 -


<br>

## Getting Started

Dependencies:
 - <a href="">``bedtools``</a>
 - <a href="">``BWA``</a>
 
> from <a href="">htslib</a>: 
 - ``faidx`` + ``samtools`` + ``bcftools``
 
<br>

> from <a href="">the Broad Institute</a>: 
 - ``Picard`` + ``GATK(-Protected)`` java suite
 
<br>

> from <a href="">the Python library collection</a>:
> (``pip`` or ``conda`` recommended for install; *=optional)
 - ``asyncio`` + ``asycnpg``* + ``concurrent.futures``*
 - ``blaze``* 
 - ``dask``*
 - ``django``* + ``flask``* + ``bottle``* + ``sanic``*
 - ``ggplot``
 - ``matplotlib2.0``
 - ``numba``*
 - ``numpy`` + ``scipy``
 - ``pandas``
 - ``plotly``
 - ``seaborn``
 - ``SQLAlchemy``*
<br>

Example datasets:
> <a href="">FTP download / AWS access from NCBI</a>
>  * Genome in a Bottle Consortium pilot genome reference standard NA12878
>  * <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4896128/">12X-NGS-platform (BioNano Genomics, Complete Genomics paired-end and LFR, Ion Proton exome, Oxford Nanopore, Pacific Biosciences, SOLiD, 10X Genomics GemCode WGS, and Illumina exome and WGS paired-end, mate-pair, and synthetic long reads)</a> highly orthogonally validated genotype determination for high-confidence regions (2016), useful as a new "gold standard" for benchmarking NGS error (i.e. false-positives rate, sensitivity/specificity, etc.) in an unbiased fashion.
>  * See Jupyter notebooks folder under ``./examples`` for some basic analysis workflow demonstrations that are easily replicated with NA12878, harnessing the ``nexgendx`` tool suite for data I/O, stats analysis, custom pipeline setup, launch & QC, and visualization. 


## License 


<big>®</big> All rights reserved. Free to copy, modify, use for personal analysis/education, share with friends, 
but not patent, sell, distribute on large-scale, use for any commerical/for-profit purposes, etc. 
(see <a href="">my LICENSE</a>, <a href="">GATK LICENSE</a>, & <a href="">more</a>)

NOT INTENDED FOR COMMERCIAL USE.
<div align="center">

<br>

---------

<img src="./doc/design/nucleosome_spacewaves_1.gif">

</div>

## Tools for the nucleosome space.

<br>

<div align="center">

``⊰♘𝚿⚔⊱ 2017 | J.Collins | ⚕ nexgendx.``                            ➉❶①⓪🄵🅡ⓔⓔ🄲🅾ⓓⓔ㊝①➓➀

<br>

~~~ py
(1*2^8 + 0*2^7 + 1*2^6 + 1*2^5 + 0*2^4 + 1*2^3 + 1*2^2 + 0*2^1 + 1*2^0) = 365
~~~

<br>

<h6>[logo image source]:</h6>
<h4>See <a href="https://pdb101.rcsb.org/motm/7">Protein DataBank's Educational Portal</a> for more about nucleosomes.</h4>

<br>

## 𐃠

</div>






