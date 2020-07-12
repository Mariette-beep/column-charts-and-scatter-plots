#!/bin/python


from pandas import read_csv
import pandas as pd
import numpy as np



file1 = 'sample_data.csv'
file2 = 'sample_data2.csv'
file3 = 'sample_data3.csv'

elements_file1 = pd.read_csv( file1 )['name'].tolist()
elements_file2 = pd.read_csv( file2 )['name'].tolist()
elements_file3 = pd.read_csv( file3 )['name'].tolist()

#print (elements_file1)


tetha = list(set(elements_file1 + elements_file2 + elements_file3))
#print( tetha )



n_tetha = len(tetha)
#print( n_tetha)

F = [elements_file1, elements_file2, elements_file3]

print(F)

list_file = [file1, file2, file3]
#print(list_file)

#y[len(F)][n_tetha]
y = []



for i in range(len(tetha)): 
    for j in range(len(F)):
        found = False
        for k in range(len(F[j])): 
            if F[j][k] == tetha[i] : 
                # y.append([list_file[j],tetha[i],1])
                y.append([list_file[j], tetha[i], 1])
                found = True
                break

        if found == False :
            # y.append([list_file[j],tetha[i],0])		
            y.append([list_file[j], tetha[i], 0])


for items in y:
   
    
    print(items[0], items[1], items[2])
y = [] 	




import matplotlib.pyplot as plt #enables the plots to be possible
import numpy as np

import matplotlib as mpl
tetha = list(set(elements_file1 + elements_file2 + elements_file3))

objects =  ['one', 'two', 'three', 'four', 'five'] #data #elements of tetha names found in the different files


performance= [3, 3, 3, 2, 1] #data corresponding number of times the names appear in the three csv files

y_pos =  objects #because pltbar doesnt value strings and objects are made of strings we create y_pos to make it accomodatable.

plt.bar(y_pos, performance, align='center')# this creates the bar chart aligned at the center 
plt.xticks(y_pos, objects) #this enables the values to be coverted back to object(names:one ,two,...) of the column chart
plt.xlabel('names in each file') # labels the x axis
plt.ylabel('number of times it appears') #labels the y axis
plt.title('New Column Chart') # gives the title of the chart







plt.show()





