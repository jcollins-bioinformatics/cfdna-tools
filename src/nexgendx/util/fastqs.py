import random as rd
import string

DNA = ['A', 'C', 'T', 'G']

def create_rand_fastqs(num_seq,len_seq):
    ''' Generate any amount of any-length fastqs with random DNA sequence,
        and random IDs (if not given; should be unique, ~36^10 odds). 
    '''
    for fasta in range(0,num_seq):
    	yield(">{}\n{}".format(
                        ''.join(rd.choice(string.ascii_uppercase +
                                string.digits) for _ in range(10)),
                        ''.join(rd.choice(DNA) for _ in range(len_seq))))

