# Load packages
import sys

with open(sys.argv[1]) as f:
	for content in f:
		content = content.rstrip() 
		words = content.split(" ")

		if (len(words[-1]) >= 21 and len(words[-1]) <= 22):
			n17 = words[-1][(len(words[-1])-17):len(words[-1])]   # Extract right barcode
			print words[0], words[2], n17
