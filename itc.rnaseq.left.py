# Load packages
from Bio.SeqIO.QualityIO import FastqGeneralIterator
import time
import re
import sys
from itertools import groupby

start = time.time()

count = 0
oklen = 0

with open(sys.argv[1]) as in_handle:
	for title, seq, qual in FastqGeneralIterator(in_handle): # Process fastq sequences and create 3 objects - title (not used again), seq (sequence), and qual (phred quality scores)
		count += 1 # counter for number of reads processed
			
		if (len(seq) <= 32 and len(seq) >= 28):
			oklen = 1
			
			n11 = seq[(len(seq)-11):len(seq)]	# Extract left barcode
			pren11 = seq[:(len(seq)-11)]
			groups = groupby(pren11)
			result = [(sum(1 for _ in group)) for label, group in groups]
	
			polyA = result[-1]-2
			print n11, oklen, polyA
		else:
			print "NA", oklen, "X"
			
		oklen = 0
