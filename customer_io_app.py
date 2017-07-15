import csv
import operator
#Opening the CSV and creating a dictionary with a count of each error as a key with its number of hits as a value
with open('customerio_sample_data.csv') as csvfile:
	readerfile = csv.reader(csvfile)
	error_dict = dict()
	for row in readerfile:
		if row[1] not in error_dict:
			error_dict[row[1]] = 1
		elif row[1] in error_dict:
			error_dict[row[1]] += 1
#Creating a list sorted by the number of hits for each error
dictlist = []
for key, value in error_dict.items():
	dictlist.append([key, value])
sort_list = sorted(dictlist, key=operator.itemgetter(1), reverse=True)
#Iterating through the highest 10 hits and printing them
i = 0
for key, value in sort_list:
	while i < 10:
		print('Error reason: ' + str(key) + ' \nNumber of incidents: ' + str(value))
		i += 1
		break