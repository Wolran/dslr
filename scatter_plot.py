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

def scatter_print_data(house, index1, index2, colors, name, reset, path):
    # Extraction des paires de notes valides
    valid_pairs = []
    for row in house:
        if row[index1].strip() and row[index2].strip():
            x = float(row[index1])
            y = float(row[index2])
            valid_pairs.append((x, y))
    
    if valid_pairs:
        # Séparation des coordonnées x et y
        x_coords = [pair[0] for pair in valid_pairs]
        y_coords = [pair[1] for pair in valid_pairs]
        
        # Creation du nuage de points
        plt.scatter(x_coords, y_coords, color=colors, label=name, alpha=0.8) #alpha : transparence
    
    plt.xlabel(course[index1 - 6])
    plt.ylabel(course[index2 - 6])
    plt.title(f"{course[index1 - 6]} vs {course[index2 - 6]}")
    plt.legend()

    if reset == 1:
        plt.savefig(f"./graph/scatter/{path}.png")
        plt.clf()

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

    # compare toutes les paires pour trouver les matieres similaires
    for i in range(6, 18):
        for j in range(i + 1, 19):  # compare uniquement avec les matieres suivantes
            scatter_print_data(ravenclaw, i, j, 'blue', "ravenclaw", 0, f"{course[i-6]}_{course[j-6]}")
            scatter_print_data(gryffindor, i, j, 'red', "gryffindor", 0, f"{course[i-6]}_{course[j-6]}")
            scatter_print_data(hufflepuff, i, j, 'yellow', "hufflepuff", 0, f"{course[i-6]}_{course[j-6]}")
            scatter_print_data(slytherin, i, j, 'green', "slytherin", 1, f"{course[i-6]}_{course[j-6]}")

