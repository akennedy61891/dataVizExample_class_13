import csv

golds = []
silvers = []
bronzes = []

categories = []

with open('data/OlympicsWinter.csv') as csvfile: 
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0: 
			categories.append(row)
			line_count += 1
		else:
			if row[7] == "Gold":
				golds.append(row[7])
			elif row [7] == "Silver":
				silvers.append(row[7])
			else:
				bronzes.append(row[7])
			line_count += 1 

print('processed', line_count, 'rows of data')
print('gold medals won: ', len(golds))
print('silver medals won:', len(silvers))
print('bronze medals won:', len(bronzes))