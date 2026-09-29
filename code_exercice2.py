import pandas as pd
###
df = pd.read_csv("data/glycemie.csv")
df
###
import matplotlib.pyplot as plt

plt.figure(1)

for time in df.columns[1:]: # Identifier les colonnes de points de mesure par un slicing
    if not 'AUCUN' in time:
        plt.plot(df["Date"],df[time],label=str(time))
        plt.xticks(df["Date"], rotation = 45)
        plt.ylabel('Glycémie (g/l)',size=14)
        plt.xlabel('Date',size=14)
        plt.legend()