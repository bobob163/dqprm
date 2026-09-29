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

############# à complèter stp :)

for i in range(tagindex.size):
    # Store value of saturation for each tag index
    sat_arr.append(...)
    # Store value of pulse rate for each tag index
    fc_arr.append(...)
    # Store corresponding indices as well as tag and closing values ones
    valuestoremove.append(...)

# Remove these values from the original data
data_arr=np.delete(...)

plt.subplots(3,2,figsize=(15,13))

...