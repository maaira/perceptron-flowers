import random
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

x1 = [] 
x2 = []
y  = []

with open('entrada.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(" ") for line in stripped if line)
    for lines in stripped:
        dates = lines.split()
        x1.append(float(dates[0]))
        x2.append(float(dates[1]))
        y.append(float(dates[2]))
        
w  = [random.randint(-1, 1),random.randint(-1, 1),random.randint(-1, 1)]
#w = [0.65 , -1.35 , 0.65]
adjust = 0.05

listofresults = []
cont = 1
x = 0
tam_of_epoch = len(x1)


for x in range (1000) :
    
    print('-----Epoca ' + str(x) + '-----')
    correct = 0
    for i in range(tam_of_epoch):
        print ('__________________________________________')
        print ('Set ' + str(i+1))
        print ('__________________________________________')

        print('Pesos: w1: '+ str(w[0]) + ' w2: '+ str(w[1]) + ' w3: '+ str(w[2]))
        
        result = x1[i]*w[0] + x2[i]*w[1] + w[2]
        if result >= 0 :
            yresult = 2        
        else :
            yresult = 1            

        if yresult != y[i]:
            erro = y[i] - result                     
            w[0] = w[0] + adjust * erro * x1[i] 
            w[1] = w[1] + adjust * erro * x2[i] 
            w[2] = w[2] + adjust * erro                  
            
        else :
            correct +=1

        print('Result :' + str(result) + '   Y: '+ str(yresult))
        
    if correct == tam_of_epoch :
        print('-----Correct Epoca-----')
        break
    else :
        print('-----Incorrect Epoca-----')

#PLOTAR GRAFICO
if w[0] == 0:
    w[0] == 0.000009
if w[1] == 0:
    w[0] == 0.000009

for t in range(tam_of_epoch):
    if y[t] == 1 :
        plt.scatter(x1[t], x2[t], color = 'black')
    else :
        plt.scatter(x1[t], x2[t], color = 'gray')


xp1 = ((-1) * w[2]) / w[0]
xp2 = ((-1) * w[2]) / w[1]
print(str(xp1) + "," + str(xp2))

pontos = [[0, xp1], [xp2, 0]]

z = np.polyfit(pontos[0], pontos[1], 1)
p = np.poly1d(z)
aux= np.arange(10)
yaux = p(aux)
plt.plot(aux, yaux, '-')

plt.show()
print("Finalizado")



plt.show()