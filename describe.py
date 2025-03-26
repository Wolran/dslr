import csv
import math

ravenclaw = []
gryffindor = []
hufflepuff = []
slytherin = []
test_all = []

def count(data, col_index):
	return len(data)

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

if __name__ == '__main__':
	#todo - read the dataset from the argument
	with open('./datasets/dataset_train.csv', mode='r', encoding='utf-8') as file:
		reader = csv.reader(file)
		next(reader)
		for row in reader:
			test_all.append(row)
			if row[1] == "Ravenclaw":
				ravenclaw.append(row)
			elif row[1] == "Gryffindor":
				gryffindor.append(row)
			elif row[1] == "Hufflepuff":
				hufflepuff.append(row)
			elif row[1] == "Slytherin":
				slytherin.append(row)

						# 		Arithmancy,Astronomy,Herbology,Defense Against the Dark Arts,Divination,Muggle Studies,Ancient Runes,History of Magic,Transfiguration,Potions,Care of Magical Creatures,Charms,Flying
	col_index = 6 		# 	6 = Arithmancy 

	# idk exactly what stat they want, so i have test_all for all stats, and the other 4 for each house

	print("all Stats test:")
	print("Count:", count(test_all, col_index))
	print("Mean:", mean(test_all, col_index))
	print("Std:", std(test_all, col_index))
	print("Min:", percentile(test_all, col_index, 0))
	print("25%:", percentile(test_all, col_index, 25))
	print("50%:", percentile(test_all, col_index, 50))
	print("75%:", percentile(test_all, col_index, 75))
	print("Max:", percentile(test_all, col_index, 100))

	print("\nRavenclaw:")
	print("Count:", count(ravenclaw, col_index))
	print("Mean:", mean(ravenclaw, col_index))
	print("Std:", std(ravenclaw, col_index))
	print("Min:", percentile(ravenclaw, col_index, 0))
	print("25%:", percentile(ravenclaw, col_index, 25))
	print("50%:", percentile(ravenclaw, col_index, 50))
	print("75%:", percentile(ravenclaw, col_index, 75))
	print("Max:", percentile(ravenclaw, col_index, 100))

	print("\nGryffindor:")
	print("Count:", count(gryffindor, col_index))
	print("Mean:", mean(gryffindor, col_index))
	print("Std:", std(gryffindor, col_index))
	print("Min:", percentile(gryffindor, col_index, 0))
	print("25%:", percentile(gryffindor, col_index, 25))
	print("50%:", percentile(gryffindor, col_index, 50))
	print("75%:", percentile(gryffindor, col_index, 75))
	print("Max:", percentile(gryffindor, col_index, 100))

	print("\nHufflepuff:")
	print("Count:", count(hufflepuff, col_index))
	print("Mean:", mean(hufflepuff, col_index))
	print("Std:", std(hufflepuff, col_index))
	print("Min:", percentile(hufflepuff, col_index, 0))
	print("25%:", percentile(hufflepuff, col_index, 25))
	print("50%:", percentile(hufflepuff, col_index, 50))
	print("75%:", percentile(hufflepuff, col_index, 75))
	print("Max:", percentile(hufflepuff, col_index, 100))

	print("\nSlytherin:")
	print("Count:", count(slytherin, col_index))
	print("Mean:", mean(slytherin, col_index))
	print("Std:", std(slytherin, col_index))
	print("Min:", percentile(slytherin, col_index, 0))
	print("25%:", percentile(slytherin, col_index, 25))
	print("50%:", percentile(slytherin, col_index, 50))
	print("75%:", percentile(slytherin, col_index, 75))
	print("Max:", percentile(slytherin, col_index, 100))
