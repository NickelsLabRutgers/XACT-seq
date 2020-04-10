# Load packages
import sys

with open(sys.argv[1]) as f:
	for content in f:
		content = content.rstrip() 
		words = content.split(" ")

		n14 = words[-1][(len(words[-1])-17):(len(words[-1])-3)]   # Extract right barcode
		link = words[-1][(len(words[-1])-23):(len(words[-1])-17)]
		cross = words[-1][10:(len(words[-1])-23)]
		n10 = words[-1][:10]
		ligation = words[-1][7:14]
		print words[0], n10, ligation, cross, link, n14
