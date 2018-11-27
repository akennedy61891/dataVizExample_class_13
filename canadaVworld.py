import csv 

italy = []
world = []
bronzes =[]

categories = []

with open('data/OlympicsWinter.csv') as csvfile: 
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "ITA":
			italy.append([int(row[0]), row[5], row [6], row[7]])
		else:
			world.append([int(row[0]), row[5], row [6], row[7]])
		line_count += 1

print('total medals for Italy:', len(italy))
print('rest of the world:', len(world))

print(italy[0])

print('processed', line_count, 'rows of data')

gold_1924 = []
gold_1948 = []
gold_1972 = []
gold_2002 = []
gold_2014 = []

for medal in italy: 
	if medal[0] == 1924 and medal[3] == "Gold":
		gold_1924.append(medal)
	if medal[0] == 1948 and medal[3] == "Gold":
		gold_1948.append(medal)
	if medal[0] == 1972 and medal[3] == "Gold":
		gold_1972.append(medal)    
	if medal[0] == 2002 and medal[3] == "Gold":
		gold_2002.append(medal)
	if medal[0] == 2014 and medal[3] == "Gold":
		gold_2014.append(medal)

print('italy won', len(gold_1924), 'gold medals in 1924')
print('italy won', len(gold_2014), 'gold medals in 2014')

#filter the 2014 array by gender



