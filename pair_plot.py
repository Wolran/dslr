import csv          
import os          
import math        
import matplotlib.pyplot as plt  
import numpy as np  
from histogram import hist_print_data
from scatter_plot import scatter_print_data

ravenclaw = []
gryffindor = []
hufflepuff = []
slytherin = []

course = "Arithmancy,Astronomy,Herbology,Defense Against the Dark Arts,Divination,Muggle Studies,Ancient Runes,History of Magic,Transfiguration,Potions,Care of Magical Creatures,Charms,Flying".split(",")

def print_pair_plot():
    n_courses = len(course)
	# fig : conteneur principal qui contient tous les sous-graphiques
    # axes : sous-graphiques individuels dans fig
    # plt.subplots : creation de plusieurs graphiques
    fig, axes = plt.subplots(n_courses, n_courses, figsize=(20, 20))
    
    # fonction pour afficher les labels sur les bords
    def wrap_text(text, width=10):
        words = text.split()
        lines = []
        current_line = []
        current_length = 0
        
		# boucle pour ajouter les mots dans les lignes et faire un retour à la ligne si la longueur dépasse la largeur
        for word in words: 
            if current_length + len(word) <= width:
                current_line.append(word)
                current_length += len(word) + 1
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word) + 1
        lines.append(' '.join(current_line))
        return '\n'.join(lines)

    for i in range(n_courses):
        for j in range(n_courses):
            current_ax = axes[i, j]
            plt.sca(current_ax) #plt.sca : permet de changer l'axe actuel
            
            index1 = i + 6
            index2 = j + 6

            if i == j:
                hist_print_data(ravenclaw, index1, 'blue', "ravenclaw", 0, course[i], False)
                hist_print_data(gryffindor, index1, 'red', "gryffindor", 0, course[i], False)
                hist_print_data(hufflepuff, index1, 'yellow', "hufflepuff", 0, course[i], False)
                hist_print_data(slytherin, index1, 'green', "slytherin", 0, course[i], False)
            else:
                scatter_print_data(ravenclaw, index1, index2, 'blue', "ravenclaw", 0, course[i], False, point_size=3)
                scatter_print_data(gryffindor, index1, index2, 'red', "gryffindor", 0, course[i], False, point_size=3)
                scatter_print_data(hufflepuff, index1, index2, 'yellow', "hufflepuff", 0, course[i], False, point_size=3)
                scatter_print_data(slytherin, index1, index2, 'green', "slytherin", 0, course[i], False, point_size=3)

            # Supprime les labels des axes pour tous les sous-graphiques
            current_ax.set_xlabel('')
            current_ax.set_ylabel('')
            
            # Garder uniquement les labels sur les bords
            if i != n_courses-1:  # si c est pas la derniere ligne, on supprime les labels x
                current_ax.set_xticks([])
            if j != 0:  # si c est pas la premiere colonne, on supprime les labels y
                current_ax.set_yticks([]) 

            # ajoute les labels sur les bords
            if i == n_courses-1:  # derniere ligne
                current_ax.set_xlabel(wrap_text(course[j]), fontsize=8)  # horizontal
            if j == 0:  # premiere colonne
                current_ax.set_ylabel(wrap_text(course[i]), fontsize=8, rotation=90)  # vertical

    plt.tight_layout()
    plt.savefig('./graph/pair/all_features_pairplot.png')
    plt.close()

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

    graph_dir = "./graph/pair"
    if not os.path.exists(graph_dir):
        os.makedirs(graph_dir)

    course = [x.strip() for x in course]
    
    print_pair_plot()

