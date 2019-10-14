import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import style
import warnings
from collections import Counter
style.use("fivethirtyeight")
print( -2**2)
print( 0**2)
print( -2**2+ 0**2)
test= sqrt((1-3)**2 +(3-3)**2)
print( test)
print( sqrt(4))
# print( -2 * -2 *-2)
def EucDist(plot, goalplot):
    euclidian= sqrt((plot[0]-goalplot[0])**2 +(plot[1]-goalplot[1])**2)
    print(euclidian)
    plt.scatter(plot[0],plot[1], s=100)

plot= [1,3]
goalplot= [3,3]
plot2= [6,9]
plt.scatter(goalplot[0],goalplot[1], s=150)
EucDist(plot,goalplot)
# plot2= [5,7]

EucDist(plot2,goalplot)

EucDist(goalplot,goalplot)
plt.ylim(ymin=0)
# plt.set_xlim(xmin=0)
plt.show()

#De olika värdena i vår datasett
# dataset = {'k': [[1,2],[2,3],[3,1]],'g': [[3,2],[6,3],[4,1]],  'r': [[6,5],[7,7],[8,6]]}
# #Ålder inkomst
# dataset = {'Hus': [[35,35],[37,37],[42,32],[60,34],[63,36],[61,35],[65,22],[76,16]],
# 'Hyresrätt': [[23,12],[26,33],[28,20],[19,6],[97,9]],
# 'Bostadsrätt': [[57,45],[24,28],[26,30]],
#   'Radhus': [[37,21],[45,47],[32,42],[55,24],[61,25]]}
# #Länka rubrikerna med värden

# #Nytt värde
# new_features = [50,36]
# #Funkttionen för att räkna ut närmsta grannen, skickar in data, prediction och antalet grannar som ska kollas
# def k_nearest_neighbors(data, predict, k =3):
#     if len(data) >= k: #om datan är mindre än antalet grannar man ska leta på så ge en varning
#         warnings.warn('K is set to a value less then the total warning groups!')
#     distances = []
#     for group in data:
#         for features in data[group]:
#             euclidian_distance= np.linalg.norm(np.array(features)-np.array(predict)) #Använder numpys funktion fär att räkna ut Euklides avstånd snabbare
#             distances.append([euclidian_distance,group]) #Skapar avståndet och värden i en array
#     votes=[i[1] for i in sorted(distances) [:k]]  #Tittar på de tre lägsta avstånden (mellan prdict och de befintliga feuturarna)
#     print(Counter(votes).most_common(1)) #Skriver ut de vanligaste och hur många av k som 'tyckte' det
#     votes_result = Counter(votes).most_common(1)[0][0]    #Här plockar vi bara ut vilken kategori som 'vann'
#     return votes_result

# result= k_nearest_neighbors(dataset,new_features, k=8)
# colors= {'Hus':'r','Hyresrätt': 'g',  'Bostadsrätt':'k',  'Radhus':'b'}
# print(result+" är gruppen Knearest tycker featuren tillhör")
# #Samma fast som oneliner
# [[plt.scatter(ii[0], ii[1],s=11,color=colors[i]) for ii in dataset[i]] for i in dataset]
# #ritar ut nya objektet featuren
# plt.scatter(new_features[0], new_features[1], s=100)
# window = plt.get_current_fig_manager().window
# screen_x, screen_y = window.wm_maxsize()
# plt.ylabel("Inkomst")
# plt.xlabel("Ålder")
# plt.show()