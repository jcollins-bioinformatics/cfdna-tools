#!/usr/bin/env python

import random
import string

DNA = ['A', 'C', 'T', 'G']

fake_chroms = ['chr_mock1', 'chr_mock2', 'chr_mock3']

for fasta in range(0,10):
	print(">{}{}".format('chr_mock_',''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))))
	for _ in range(0,18):
		print("{}".format(''.join(random.choice(DNA) for _ in range(60))))

