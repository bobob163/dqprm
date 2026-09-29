import pandas as pd

df = pd.read_csv('ages_DQPRM.csv')
df.columns = ['Etudiant', 'Age']
df

###

import scipy.stats
import numpy as np

age_stats = scipy.stats.describe(df['Age'])
print(age_stats,'\n')
print("Age moyen :", age_stats.mean)
print("Age median :", np.median(df['Age']))

###

import matplotlib.pyplot as plt

plt.boxplot(df['Age'])
plt.title('Répartition des âges de la promotion DQPRM')
plt.ylabel('Age')
plt.grid()
plt.show()

###

import scipy.stats

# Test de Student pour comparer la moyenne
t_stat, pval = scipy.stats.ttest_1samp(df['Age'], 26)

print(f"Statistique t : {t_stat:.4f}")
print(f"Valeur p (p-value) : {pval:.4f}")

###

if pval < 0.05:
    print("Hypothèse nulle rejetée")
else:
    print("Hypothèse nulle acceptée")