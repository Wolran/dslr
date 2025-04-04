import csv
import math
import sys
import os

ravenclaw = []
gryffindor = []
hufflepuff = []
slytherin = []
data_all = []

def count(data, col_index):
	return sum(1 for row in data if row[col_index].strip())

def mean(data, col_index):
	values = [float(row[col_index]) for row in data if row[col_index].strip()]
	return sum(values) / len(values) if values else 0

def std(data, col_index):
	values = [float(row[col_index]) for row in data if row[col_index].strip()]
	if len(values) < 2:
		return 0
	avg = mean(data, col_index)
	variance = sum((x - avg) ** 2 for x in values) / (len(values) - 1)
	return math.sqrt(variance)

def percentile(data, col_index, percent):
	values = [float(row[col_index]) for row in data if row[col_index].strip()]
	if not values:
		return None
	values.sort()
	k = (len(values) - 1) * (percent / 100)
	f = math.floor(k)
	c = math.ceil(k)
	if f == c:
		return values[int(k)]
	d0 = values[f] * (c - k)
	d1 = values[c] * (k - f)
	return d0 + d1


def print_data():
	columns =  ["Index" ,"Arithmancy", "Astronomy", "Herbology", "Defense Against", "Divination", 
				"Muggle Studies", "Ancient Runes", "History of Magic", "Transfiguration", "Potions",
				"Care of Magica", "Charms", "Flying"]

	data = {
		"count": [count(data_all, 0), count(data_all, 6), count(data_all, 7), count(data_all, 8), count(data_all, 9), count(data_all, 10),  count(data_all, 11), count(data_all, 12), count(data_all, 13), count(data_all, 14), count(data_all, 15), count(data_all, 16), count(data_all, 17), count(data_all, 18)],
		"mean": [mean(data_all, 0), mean(data_all, 6), mean(data_all, 7), mean(data_all, 8), mean(data_all, 9), mean(data_all, 10), mean(data_all, 11), mean(data_all, 12), mean(data_all, 13), mean(data_all, 14), mean(data_all, 15), mean(data_all, 16), mean(data_all, 17), mean(data_all, 18)],
		"std": [std(data_all, 0) ,std(data_all, 6), std(data_all, 7), std(data_all, 8), std(data_all, 9), std(data_all, 10), std(data_all, 11), std(data_all, 12), std(data_all, 13), std(data_all, 14), std(data_all, 15), std(data_all, 16), std(data_all, 17), std(data_all, 18)],
		"min": [percentile(data_all, 0, 0), percentile(data_all, 6, 0), percentile(data_all, 7, 0), percentile(data_all, 8, 0), percentile(data_all, 9, 0), percentile(data_all, 10, 0), percentile(data_all, 11, 0), percentile(data_all, 12, 0), percentile(data_all, 13, 0), percentile(data_all, 14, 0), percentile(data_all, 15, 0), percentile(data_all, 16, 0), percentile(data_all, 17, 0), percentile(data_all, 18, 0)],
		"25%": [percentile(data_all, 0, 25), percentile(data_all, 6, 25), percentile(data_all, 7, 25), percentile(data_all, 8, 25), percentile(data_all, 9, 25), percentile(data_all, 10, 25), percentile(data_all, 11, 25), percentile(data_all, 12, 25), percentile(data_all, 13, 25), percentile(data_all, 14, 25), percentile(data_all, 15, 25), percentile(data_all, 16, 25), percentile(data_all, 17, 25), percentile(data_all, 18, 25)],
		"50%": [percentile(data_all, 0, 50), percentile(data_all, 6, 50), percentile(data_all, 7, 50), percentile(data_all, 8, 50), percentile(data_all, 9, 50), percentile(data_all, 10, 50), percentile(data_all, 11, 50), percentile(data_all, 12, 50), percentile(data_all, 13, 50), percentile(data_all, 14, 50), percentile(data_all, 15, 50), percentile(data_all, 16, 50), percentile(data_all, 17, 50), percentile(data_all, 18, 50)],
		"75%": [percentile(data_all, 0, 75), percentile(data_all, 6, 75), percentile(data_all, 7, 75), percentile(data_all, 8, 75), percentile(data_all, 9, 75), percentile(data_all, 10, 75), percentile(data_all, 11, 75), percentile(data_all, 12, 75), percentile(data_all, 13, 75), percentile(data_all, 14, 75), percentile(data_all, 15, 75), percentile(data_all, 16, 75), percentile(data_all, 17, 75), percentile(data_all, 18, 75)],
		"max": [percentile(data_all, 0, 100), percentile(data_all, 6, 100), percentile(data_all, 7, 100), percentile(data_all, 8, 100), percentile(data_all, 9, 100), percentile(data_all, 10, 100), percentile(data_all, 11, 100), percentile(data_all, 12, 100), percentile(data_all, 13, 100), percentile(data_all, 14, 100), percentile(data_all, 15, 100), percentile(data_all, 16, 100), percentile(data_all, 17, 100), percentile(data_all, 18, 100)],
		"Ravenclaw": [count(ravenclaw, 0), count(ravenclaw, 6), count(ravenclaw, 7), count(ravenclaw, 8), count(ravenclaw, 9), count(ravenclaw, 10), count(ravenclaw, 11), count(ravenclaw, 12), count(ravenclaw, 13), count(ravenclaw, 14), count(ravenclaw, 15), count(ravenclaw, 16), count(ravenclaw, 17), count(ravenclaw, 18)],
		"Gryffindor": [count(gryffindor, 0), count(gryffindor, 6), count(gryffindor, 7), count(gryffindor, 8), count(gryffindor, 9), count(gryffindor, 10), count(gryffindor, 11), count(gryffindor, 12), count(gryffindor, 13), count(gryffindor, 14), count(gryffindor, 15), count(gryffindor, 16), count(gryffindor, 17), count(gryffindor, 18)],
		"Hufflepuff": [count(hufflepuff, 0), count(hufflepuff, 6), count(hufflepuff, 7), count(hufflepuff, 8), count(hufflepuff, 9), count(hufflepuff, 10), count(hufflepuff, 11), count(hufflepuff, 12), count(hufflepuff, 13), count(hufflepuff, 14), count(hufflepuff, 15), count(hufflepuff, 16), count(hufflepuff, 17), count(hufflepuff, 18)],
		"Slytherin": [count(slytherin, 0), count(slytherin, 6), count(slytherin, 7), count(slytherin, 8), count(slytherin, 9), count(slytherin, 10), count(slytherin, 11), count(slytherin, 12), count(slytherin, 13), count(slytherin, 14), count(slytherin, 15), count(slytherin, 16), count(slytherin, 17), count(slytherin, 18)]
	}

	header = f"{'Subject':<20} {'Count':<10} {'Mean':<10} {'Std':<10} {'Min':<10} {'25%':<10} {'50%':<10} {'75%':<10} {'Max':<10} {'Ravenclaw':<10} {'Gryffindor':<10} {'Hufflepuff':<10} {'Slytherin':<10}"
	print(header)
	print("-" * len(header))

	for i, column in enumerate(columns):
		row = f"{column:<20} {data['count'][i]:<10} {data['mean'][i]:<10.2f} {data['std'][i]:<10.2f} {data['min'][i]:<10.2f} {data['25%'][i]:<10.2f} {data['50%'][i]:<10.2f} {data['75%'][i]:<10.2f} {data['max'][i]:<10.2f} {data['Ravenclaw'][i]:<10} {data['Gryffindor'][i]:<10} {data['Hufflepuff'][i]:<10} {data['Slytherin'][i]:<10}"
		print(row)



if __name__ == '__main__':
	#todo - read the dataset from the argument
	try:
		dataset = sys.argv[1]
	except IndexError:
		print("Usage: python describe.py <dataset>")
		sys.exit(1)
	except Exception as e:
		print(f"An error occurred: {e}")

	if not os.path.exists(dataset):
		print(f"File {dataset} does not exist.")
		sys.exit(1)
	elif not os.path.isfile(dataset):
		print(f"{dataset} is not a file.")
		sys.exit(1)
	elif not dataset.endswith('.csv'):
		print(f"{dataset} is not a CSV file.")
		sys.exit(1)

	
	with open(dataset, mode='r', encoding='utf-8') as file:
		reader = csv.reader(file)
		next(reader)
		for row in reader:
			data_all.append(row)
			if row[1] == "Ravenclaw":
				ravenclaw.append(row)
			elif row[1] == "Gryffindor":
				gryffindor.append(row)
			elif row[1] == "Hufflepuff":
				hufflepuff.append(row)
			elif row[1] == "Slytherin":
				slytherin.append(row)
	print_data()
