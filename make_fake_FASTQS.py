#!/usr/bin/env python

import random
import string

DNA = ['A', 'C', 'T', 'G']

for fasta in range(0,200):
	print(">{}".format(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))))
	print("{}".format(''.join(random.choice(DNA) for _ in range(110))))

