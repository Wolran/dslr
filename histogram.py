import csv
import os
import math
import matplotlib.pyplot as plt
import numpy as np

ravenclaw = []
gryffindor = []
hufflepuff = []
slytherin = []
course = "Arithmancy,Astronomy,Herbology,Defense Against the Dark Arts,Divination,Muggle Studies,Ancient Runes,History of Magic,Transfiguration,Potions,Care of Magical Creatures,Charms,Flying".split(",")


def print_data(house, index, colors, name, reset, path):

	data = [float(row[index]) for row in house if row[index].strip()]

	plt.hist(data, bins=50, color=colors, label=name)
	
	
	# plt.plot(data, data, color='black', label="Histogram")

	plt.xlabel("note")
	plt.ylabel("frequency")
	plt.title(path)
	plt.legend()

	if reset == 1:
		plt.savefig(f"./graph/hist/{path}.png")
		plt.clf()
	


if __name__ == '__main__':
	#todo add index from the argument for another program
	with open('./datasets/dataset_train.csv', mode='r', encoding='utf-8') as file:
		reader = csv.reader(file)
		next(reader)
		for row in reader:
			if row[1] == "Ravenclaw":
				ravenclaw.append(row)
			elif row[1] == "Gryffindor":
				gryffindor.append(row)
			elif row[1] == "Hufflepuff":
				hufflepuff.append(row)
			elif row[1] == "Slytherin":
				slytherin.append(row)
	# i keep the data in the house list for after idk if i need it
	graph_dir = "./graph/hist"
	if not os.path.exists(graph_dir):
		os.makedirs(graph_dir)

	# index = 6
	# data = [float(row[index]) for row in ravenclaw if row[index].strip()]
	# print(data[0])

	course = [x.strip() for x in course]

	for i in range(6, 19):
		print_data(ravenclaw, i, 'blue', "ravenclaw", 0, course[i - 6])
		print_data(gryffindor, i, 'red', "gryffindor", 0, course[i - 6])
		print_data(hufflepuff, i, 'yellow', "hufflepuff", 0, course[i - 6])
		print_data(slytherin, i, 'green', "slytherin", 1, course[i - 6])

	print("done")

