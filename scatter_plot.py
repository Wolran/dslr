import csv          
import os          
import math        
import matplotlib.pyplot as plt  
import numpy as np  

# Stocke les donnees de chaque maison
ravenclaw = []
gryffindor = []
hufflepuff = []
slytherin = []

course = "Arithmancy,Astronomy,Herbology,Defense Against the Dark Arts,Divination,Muggle Studies,Ancient Runes,History of Magic,Transfiguration,Potions,Care of Magical Creatures,Charms,Flying".split(",")

def scatter_print_data(house, index1, index2, colors, name, reset, path, show_legend=True, point_size=20):
    # Extraction des paires de notes valides
    valid_pairs = []
    x_values = []
    y_values = []
    for row in house:
        if row[index1].strip() and row[index2].strip():
            x = float(row[index1])
            y = float(row[index2])
            x_values.append(x) # ajoute la note x à la liste x_values
            y_values.append(y) # ajoute la note y à la liste y_values
    
	# boucle pour normaliser les notes car elles sont sur des echelles differentes
    for x, y in zip(x_values, y_values):
        x = (x - min(x_values)) / (max(x_values) - min(x_values))
        y = (y - min(y_values)) / (max(y_values) - min(y_values))
        valid_pairs.append((x, y))
    
    if valid_pairs:
        # separation des coordonnees x et y
        x_coords = [pair[0] for pair in valid_pairs]
        y_coords = [pair[1] for pair in valid_pairs]
        
        plt.scatter(x_coords, y_coords, color=colors, label=name, alpha=0.8, s=point_size)
    
    plt.xlabel(course[index1 - 6])
    plt.ylabel(course[index2 - 6])
    if show_legend:
        plt.legend()

    if reset == 1:
        plt.savefig(f"./graph/scatter/{path}.png")
        plt.clf()

def calculate_correlation(x_values, y_values):
    # calcul de la correlation 
    x_mean = sum(x_values) / len(x_values) # moyenne des notes x
    y_mean = sum(y_values) / len(y_values) # moyenne des notes y
    
	#numerateur : somme des produits des notes x et y moins les moyennes des notes x et y
	#denominateur : racine carree de la somme des carres des notes x moins la moyenne des notes x et la somme des carres des notes y moins la moyenne des notes y
    numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_values, y_values))
    denominator = math.sqrt(sum((x - x_mean) ** 2 for x in x_values) * 
                          sum((y - y_mean) ** 2 for y in y_values))
    
    return abs(numerator / denominator) if denominator != 0 else 0

if __name__ == '__main__':
    # Lecture du fichier CSV
    with open('./datasets/dataset_train.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # saute la premiere ligne (entete)
        for row in reader:
            if row[1] == "Ravenclaw":
                ravenclaw.append(row)
            elif row[1] == "Gryffindor":
                gryffindor.append(row)
            elif row[1] == "Hufflepuff":
                hufflepuff.append(row)
            elif row[1] == "Slytherin":
                slytherin.append(row)

    # Creer le dossier pour les graphiques
    graph_dir = "./graph/scatter"
    if not os.path.exists(graph_dir):
        os.makedirs(graph_dir)

    course = [x.strip() for x in course]

    # Compare chaque paire de matieres une seule fois
    best_correlation = 0
    best_pair = None

    # Trouver les deux matieres les plus similaires en evitant les doublons
    for i in range(6, 18):
        for j in range(i + 1, 19):
            # Collecter toutes les paires valides pour cette comparaison
            x_values = []
            y_values = []
            for house in [ravenclaw, gryffindor, hufflepuff, slytherin]:
                for row in house:
                    if row[i].strip() and row[j].strip():
                        x_values.append(float(row[i]))
                        y_values.append(float(row[j]))
            
            # Calculer la correlation pour cette paire
            correlation = calculate_correlation(x_values, y_values)
            
            # mettre a jour la correlation et la paire si la correlation est meilleure
            if correlation > best_correlation:
                best_correlation = correlation
                best_pair = (i, j)

    # creer le scatter pour les deux matieres les plus similaires
    plt.figure(figsize=(10, 10))
    scatter_print_data(ravenclaw, best_pair[0], best_pair[1], 'blue', "ravenclaw", 0, "similar_features")
    scatter_print_data(gryffindor, best_pair[0], best_pair[1], 'red', "gryffindor", 0, "similar_features")
    scatter_print_data(hufflepuff, best_pair[0], best_pair[1], 'yellow', "hufflepuff", 0, "similar_features")
    scatter_print_data(slytherin, best_pair[0], best_pair[1], 'green', "slytherin", 1, "similar_features")

