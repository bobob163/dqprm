import pandas as pd

df = pd.read_csv("data/data_oxypleth.csv")

print("Dataset comprenant {} ligne(s) et {} colonne(s)".format(df.shape[0],df.shape[1]))
print(df.size)

#######
import matplotlib.pyplot as plt

df_crop = df.values.copy()[:300]

plt.subplots(1,2,figsize=(15,5))
plt.subplot(121)
plt.plot(df["data"])
#...
plt.title('Dataframe original (données complètes)')

plt.subplot(122)
plt.plot(df_crop)
#...
plt.title('Dataframe réduit (300 premières valeurs)')

print(*df_crop,sep=",") # permet d'afficher la liste des valeurs

####
import numpy as np

data = df.values

# Liste des indices des différents signal tags
tagindex = np.where(data == 254)[0]

print("List of tag index values:", tagindex)
# Check if for the first tag index value, the signal value is indeed 254
#print(data[tagindex[0]][0])

# Define a set of empty lists to store the clinically useful information
sat_arr = []
fc_arr = []
data_arr = data.copy()
valuestoremove = []

for i in range(tagindex.size):
    idx = tagindex[i]

    sat_arr.append(data.iloc[idx+1, 0])

    fc_arr.append(data.iloc[idx+2, 0])

    valuestoremove.extend([idx, idx+1, idx+2])


data_arr = np.delete(data, valuestoremove, axis=0)

print(sat_arr)
print(fc_arr)
print(valuestoremove)
print(data_arr)

###

plt.subplots(3,2,figsize=(15,13))

plt.subplot(3,2,1)
plt.plot(data)
plt.title('Données complètes')

plt.subplot(3,2,2)
plt.plot(data_arr)
plt.title('Données netoyées')

plt.subplot(3,2,3)
plt.plot(data_arr[0:300], 'g')
plt.title('Données netoyées réduites aux 300 premières valeurs')

plt.subplot(3,2,4)
plt.plot(fc_arr, 'b')
plt.title('Valeur de fréquence cardiaque')

plt.subplot(3,2,5)
plt.plot(sat_arr, 'r')
plt.title('Valeur de saturation')

plt.subplot(3,2,6)
plt.plot(fc_arr, 'b')
plt.plot(sat_arr, 'r')
plt.ylim(0, 120)
plt.title('Valeur de fréquence cardiaque et de saturation sur un même graphique')