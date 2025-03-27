import csv
import math
import pandas as pd

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
	#todo find another way to do this bc this is ugly

	columns =  ["    Arithmancy", "    Astronomy", "       Herbology", "Defense Against", "Divination"]
	columns2 = ["Muggle Studies", "Ancient Runes", "History of Magic", "Transfiguration", "   Potions"]
	columns3 = ["Care of Magica", "       Charms", "          Flying"]

	data = {
		# "": ["    Arithmancy", "    Astronomy", "       Herbology", "Defense Against", "Divination"],
	    "count": [count(data_all, 6), count(data_all, 7), count(data_all, 8), count(data_all, 9), count(data_all, 10)],
	    "mean": [mean(data_all, 6), mean(data_all, 7), mean(data_all, 8), mean(data_all, 9), mean(data_all, 10)],
	    "std": [std(data_all, 6), std(data_all, 7), std(data_all, 8), std(data_all, 9), std(data_all, 10)],
	    "min": [percentile(data_all, 6, 0), percentile(data_all, 7, 0), percentile(data_all, 8, 0), percentile(data_all, 9, 0), percentile(data_all, 10, 0)],
	    "25%": [percentile(data_all, 6, 25), percentile(data_all, 7, 25), percentile(data_all, 8, 25), percentile(data_all, 9, 25), percentile(data_all, 10, 25)],
	    "50%": [percentile(data_all, 6, 50), percentile(data_all, 7, 50), percentile(data_all, 8, 50), percentile(data_all, 9, 50), percentile(data_all, 10, 50)],
	    "75%": [percentile(data_all, 6, 75), percentile(data_all, 7, 75), percentile(data_all, 8, 75), percentile(data_all, 9, 75), percentile(data_all, 10, 75)],
	    "max": [percentile(data_all, 6, 100), percentile(data_all, 7, 100), percentile(data_all, 8, 100), percentile(data_all, 9, 100), percentile(data_all, 10, 100)]
	}
	data2 = {
		# "": ["Muggle Studies", "Ancient Runes", "History of Magic", "Transfiguration", "   Potions"],
		"count": [count(data_all, 11), count(data_all, 12), count(data_all, 13), count(data_all, 14), count(data_all, 15)],
		"mean": [mean(data_all, 11), mean(data_all, 12), mean(data_all, 13), mean(data_all, 14), mean(data_all, 15)],
		"std": [std(data_all, 11), std(data_all, 12), std(data_all, 13), std(data_all, 14), std(data_all, 15)],
		"min": [percentile(data_all, 11, 0), percentile(data_all, 12, 0), percentile(data_all, 13, 0), percentile(data_all, 14, 0), percentile(data_all, 15, 0)],
		"25%": [percentile(data_all, 11, 25), percentile(data_all, 12, 25), percentile(data_all, 13, 25), percentile(data_all, 14, 25), percentile(data_all, 15, 25)],
		"50%": [percentile(data_all, 11, 50), percentile(data_all, 12, 50), percentile(data_all, 13, 50), percentile(data_all, 14, 50), percentile(data_all, 15, 50)],
		"75%": [percentile(data_all, 11, 75), percentile(data_all, 12, 75), percentile(data_all, 13, 75), percentile(data_all, 14, 75), percentile(data_all, 15, 75)],
		"max": [percentile(data_all, 11, 100), percentile(data_all, 12, 100), percentile(data_all, 13, 100), percentile(data_all, 14, 100), percentile(data_all, 15, 100)]
	}
	data3 = {
		# "": ["Care of Magica", "       Charms", "          Flying"],
		"count": [count(data_all, 16), count(data_all, 17), count(data_all, 18)],
		"mean": [mean(data_all, 16), mean(data_all, 17), mean(data_all, 18)],
		"std": [std(data_all, 16), std(data_all, 17), std(data_all, 18)],
		"min": [percentile(data_all, 16, 0), percentile(data_all, 17, 0), percentile(data_all, 18, 0)],
		"25%": [percentile(data_all, 16, 25), percentile(data_all, 17, 25), percentile(data_all, 18, 25)],
		"50%": [percentile(data_all, 16, 50), percentile(data_all, 17, 50), percentile(data_all, 18, 50)],
		"75%": [percentile(data_all, 16, 75), percentile(data_all, 17, 75), percentile(data_all, 18, 75)],
		"max": [percentile(data_all, 16, 100), percentile(data_all, 17, 100), percentile(data_all, 18, 100)]
	}

	df = pd.DataFrame(data, index=columns)
	df2 = pd.DataFrame(data2, index=columns2)
	df3 = pd.DataFrame(data3, index=columns3)
	# df = pd.DataFrame(data).transpose()
	# df2 = pd.DataFrame(data2).transpose()
	# df3 = pd.DataFrame(data3).transpose()
	df = df.transpose()
	df2 = df2.transpose()
	df3 = df3.transpose()

	print(df, '\n')
	print(df2, '\n')
	print(df3)


if __name__ == '__main__':
	#todo - read the dataset from the argument
	with open('./datasets/dataset_train.csv', mode='r', encoding='utf-8') as file:
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
	# i keep the data in the house list for after idk if i need it
	print_data()
