full = '../data/higgs.csv'
test = '../data/higgs-testing.csv'

i = 11000000

with open(test, 'w') as outfile:
	with open(full, 'r') as infile:
		for line in infile:
			if (i%50000 == 0):
				print i
			if (i < 500000):
				outfile.write(line)
			i = i-1;
			
