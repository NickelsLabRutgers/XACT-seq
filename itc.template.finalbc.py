###	Code to identify left and right barcodes in the ITC template files

# Load packages
from Bio.SeqIO.QualityIO import FastqGeneralIterator
import time
import numpy
import re
import sys
start = time.time()

count = 0
valid_dna = 'ACTG'

# Output file
out_handle = open(sys.argv[2], "w")

# Output file columns (header)
out_handle.write("Seq_score\tLBC_seq\tLBC_qual\tLBC_score\tRBC_seq\tRBC_qual\tRBC_score\tINT_error\n")

# Intermediate sequence
bdsorig = ("GATAACAATTTCAA")

# Function to estimate hamming distance between two strings
def hamdist(str1, str2):
	diffs = 0
	for ch1, ch2 in zip(str1, str2):
		if ch1 != ch2:
			diffs += 1
	return diffs

with open(sys.argv[1]) as in_handle:
	for title, seq, qual in FastqGeneralIterator(in_handle): # Process fastq sequences and create 3 objects - title (not used again), seq (sequence), and qual (phred quality scores)
		count += 1 # counter for number of reads processed
		if (len(seq) <= 150 and len(seq) >= 43): # Only process reads whose lengths are at the max N17 BC
			phred = [ord(c)-33 for c in qual]	# Convert quality scores to numeric values
			phred_read = numpy.mean(phred)		# Calc mean read quality

			if phred_read > 25:
				bds0 = seq[11:25]							# Binding-site seq in read
				bds_dist0 = hamdist(bds0, bdsorig)			# Number of mismatches in the binding-site
				bds1 = seq[12:26]							# Binding-site seq in read
				bds_dist1 = hamdist(bds1, bdsorig)			# Number of mismatches in the binding-site
				bds2 = seq[13:27]							# Binding-site seq in read
				bds_dist2 = hamdist(bds2, bdsorig)			# Number of mismatches in the binding-site
				
				if bds_dist0 < 3:
					offset = 0
					bds_dist = bds_dist0
				elif bds_dist1 < 3:
					offset = 1
					bds_dist = bds_dist1
				elif bds_dist2 < 3:
					offset = 2
					bds_dist = bds_dist2
				else:
					offset = -1

				if offset >= 0:
					leftbc = seq[offset:(11+offset)]							# Extract left barcode
					qual_leftbc = qual[offset:(11+offset)]						# Left barcode quality
					phred_leftbc = numpy.mean(phred[offset:(11+offset)])		# Mean value of left barcode

					if all(i in valid_dna for i in leftbc):
						rightbc = seq[(29+offset):(43+offset)]						# Extract right barcode
						qual_rightbc = qual[(29+offset):(43+offset)]					# Right barcode quality
						phred_rightbc = numpy.mean(phred[(29+offset):(43+offset)])	# Mean value of right barcode

						# Save output in the output file
						out_handle.write("%.2f\t%s\t%s\t%.2f\t%s\t%s\t%.2f\t%i\n" % (phred_read, leftbc, qual_leftbc, phred_leftbc, rightbc, qual_rightbc, phred_rightbc, bds_dist))

		# Print time-taken for processing every 100k reads
		if(count%100000==0):
			elapsed = time.time() - start
			print("%.2f" % round(elapsed,2), "%i done" % (count))
