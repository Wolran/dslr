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

def print_pair_plot(index, path):
    selected_courses = [6, 7, 8, 9]  # 4 premieres matieres
    n_courses = len(selected_courses)
    
    # fig : conteneur principal qui contient tous les sous-graphiques
    # axes : sous-graphiques individuels dans fig
    # plt.subplots : creation de plusieurs graphiques
    fig, axes = plt.subplots(n_courses, n_courses, figsize=(15, 15)) #15 pouces
    
    for i in range(n_courses):
        for j in range(n_courses):
            current_ax = axes[i, j] # Selectionne l'axe courant
            plt.sca(current_ax)  # plt.sca : selectionne l'axe courant
            
            index1 = selected_courses[i]
            index2 = selected_courses[j]

            if i == j:  # Diagonale : histogrammes
                hist_print_data(ravenclaw, index1, 'blue', "ravenclaw", 0, path)
                hist_print_data(gryffindor, index1, 'red', "gryffindor", 0, path)
                hist_print_data(hufflepuff, index1, 'yellow', "hufflepuff", 0, path)
                hist_print_data(slytherin, index1, 'green', "slytherin", 0, path)
            else:  # Hors diagonale : scatter plots
                scatter_print_data(ravenclaw, index1, index2, 'blue', "ravenclaw", 0, path)
                scatter_print_data(gryffindor, index1, index2, 'red', "gryffindor", 0, path)
                scatter_print_data(hufflepuff, index1, index2, 'yellow', "hufflepuff", 0, path)
                scatter_print_data(slytherin, index1, index2, 'green', "slytherin", 0, path)

            if i == n_courses-1: # Derniere ligne
                plt.xlabel(course[index2 - 6], rotation=45)
            if j == 0: # Premiere colonne
                plt.ylabel(course[index1 - 6], rotation=45)

    plt.suptitle(f'Pair Plot - Matière : {path}', y=1.02)
    plt.tight_layout()
    plt.savefig(f'./graph/pair/{path}_pairplot.png')
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

    for i in range(6, 19):
        print_pair_plot(i, course[i - 6])

