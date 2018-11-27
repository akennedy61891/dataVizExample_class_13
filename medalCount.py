import csv
import matplotlib.pyplot as plt

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

pct_gold = len(golds) / line_count * 100
pct_silver = len(silvers) / line_count * 100
pct_bronze = len(bronzes) / line_count * 100

#do some math here and draw a pie chart based on last week's example 
labels = "Gold", "Silver", "Bronze"
sizes = [pct_gold, pct_silver, pct_bronze]
colors = ['yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Medals by Colour")
plt.show()
plt.show()