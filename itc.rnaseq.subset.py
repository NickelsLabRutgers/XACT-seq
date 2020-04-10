import sys
from Bio.SeqIO.QualityIO import FastqGeneralIterator

input_file = sys.argv[1]
id_file = sys.argv[2]
output_file = sys.argv[3]

with open(id_file) as id_handle:
    # Taking first word on each line as an identifer
	wanted = set(line.rstrip("\n").split(None,1)[0] for line in id_handle)
print("Found %i unique identifiers in %s" % (len(wanted), id_file))

count = 0
with open(input_file) as in_handle:
	with open(output_file, "w") as out_handle:
		for title, seq, qual in FastqGeneralIterator(in_handle):
			# The ID is the first word in the title line (after the @ sign):
			if title.split(None, 1)[0] in wanted:
			# this produces a standard 4-line fastq entry:
				out_handle.write("@%s\n%s\n+\n%s\n" % (title, seq, qual))
				count += 1
print("Saved %i records from %s to %s" % (count, input_file, output_file))

if count < len(wanted):
	print("Warning %i IDs not found in %s" % (len(wanted) - count, input_file))
