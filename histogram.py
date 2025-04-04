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


def hist_print_data(house, index, colors, name, reset, path, show_legend=True):
	data = [float(row[index]) for row in house if row[index].strip()]
	
	# normalisation des notes
	if data:
		data = [(x - min(data)) / (max(data) - min(data)) for x in data]
	
	# Creation de l'histogramme
	# data : notes des eleves
	# bins=50 : nombre d'intervalles pour regrouper les notes
	plt.hist(data, bins=50, density=True, color=colors, label=name, alpha=0.8)
	
	plt.xlabel(f"Notes pour {course[index-6]}")
	plt.ylabel("Densité")
	if show_legend:
		plt.legend()

	if reset == 1:
		plt.savefig(f"./graph/hist/{path}.png")
		plt.clf()


def calculate_homogeneity(houses_data):
	# calcule l'ecart-type des moyennes des notes pour chaque maison
	means = [np.mean(data) for data in houses_data]
	return np.std(means)  # plus c est proche de 0, plus les moyennes sont proches


if __name__ == '__main__':
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

	graph_dir = "./graph/hist"
	if not os.path.exists(graph_dir):
		os.makedirs(graph_dir)

	course = [x.strip() for x in course]

	# trouver la matiere la plus homogene
	most_homogeneous = None
	best_homogeneity = float('inf')

	for i in range(6, 19):
		# collecte des notes pour chaque maison
		houses_data = [
			[float(row[i]) for row in house if row[i].strip()]
			for house in [ravenclaw, gryffindor, hufflepuff, slytherin]
		]
		
		homogeneity = calculate_homogeneity(houses_data)
		if homogeneity < best_homogeneity:
			best_homogeneity = homogeneity
			most_homogeneous = i

	# creer l'histogramme pour la matiere la plus homogene
	plt.figure(figsize=(10, 6))
	hist_print_data(ravenclaw, most_homogeneous, 'blue', "ravenclaw", 0, "most_homogeneous")
	hist_print_data(gryffindor, most_homogeneous, 'red', "gryffindor", 0, "most_homogeneous")
	hist_print_data(hufflepuff, most_homogeneous, 'yellow', "hufflepuff", 0, "most_homogeneous")
	hist_print_data(slytherin, most_homogeneous, 'green', "slytherin", 1, "most_homogeneous")

