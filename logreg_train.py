import pandas as pd
import numpy as np
import csv
import os
import sys

ravenclaw = []
gryffindor = []
hufflepuff = []
slytherin = []
data_all = []


# change this
theta0, theta1 = 0, 0

def estimatePrice(mileage, theta0, theta1):
	#change this too
	return theta0 + (theta1 * mileage)


def normalise(mileage, price):
	# Normalisation (entre 0 et 1)
	mileage_min, mileage_max = np.min(mileage), np.max(mileage)
	price_min, price_max = np.min(price), np.max(price)

	if mileage_max != mileage_min:
		mileage_normalized = (mileage - mileage_min) / (mileage_max - mileage_min)
	else:
		mileage_normalized = mileage
	if price_max != price_min:
		price_normalized = (price - price_min) / (price_max - price_min)
	else:
		price_normalized = price

	return mileage_normalized, price_normalized, price_min, price_max, mileage_min, mileage_max


def linear_algo(theta0, theta1, mileage, price, iterations=10000, learningRate=0.01):

	# Normalisation des données
	mileage_normalized, price_normalized, price_min, price_max, mileage_min, mileage_max = normalise(mileage, price)

	for _ in range(iterations):
		sum_theta0 = 0
		sum_theta1 = 0

		for i in range(m):
			estimated_price = estimatePrice(mileage_normalized[i], theta0, theta1)
			error = estimated_price - price_normalized[i]
			sum_theta0 += error
			sum_theta1 += error * mileage_normalized[i]

		tmp_theta0 = learningRate * (1 / m) * sum_theta0
		tmp_theta1 = learningRate * (1 / m) * sum_theta1

		theta0 -= tmp_theta0
		theta1 -= tmp_theta1

	theta0_final = price_min + (price_max - price_min) * (theta0 - theta1 * mileage_min / (mileage_max - mileage_min))
	theta1_final = (price_max - price_min) * theta1 / (mileage_max - mileage_min)

	return theta0_final, theta1_final


if __name__ == "__main__":

	with open("./dataset_train.csv", mode='r', encoding='utf-8') as file:
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

	for i in range(len(data_all)):
		data_all[i] = [float(x) for x in data_all[i][6:]] 



	#theta0_final, theta1_final = linear_algo(theta0, theta1, mileage, price, iterations=10000, learningRate=0.01)


# ou est le 0.5 ? moyenne : mediane ou autre ou moyenne des note / median des 4 maisonsS