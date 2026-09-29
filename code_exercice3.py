import pandas as pd

df = pd.read_csv("data/Table.csv", sep ="\t", index_col =0)

rho_g_per_cm3 = 1.03
df['Masse [g]'] = rho_g_per_cm3 * df['Volume [cm3]']

m_foie_lobe_d = df.loc["lobe_droit",'Masse [g]']

###D'après le modèle de partitionnement, on doit estimer le  rapport de concentration entre la tumeur et le foie perfusé,
import numpy as np

delta_Mev_per_Bq_s = 0.9336
T_y90_s = 64.05*3600
dose_foie_limite_Gy = 120
act_1 = (120*m_foie_lobe_d*10**(-3)*np.log(2))/(T_y90_s*0.9336e6*1.6e-19/(10**(-9)))
print(f"L'activité à injecter est de {act_1:.2f} GBq pour atteindre {dose_foie_limite_Gy} Gy au lobe droit.")

ratio_tum_lobe = (df.loc["tum_dome_SPECT","Mean"])/(df.loc["lobe_droit","Mean"])
print(f"Le rapport des concentrations est estimé à {ratio_tum_lobe:.2f}")

m_tum = df.loc["tum_dome_SPECT","Masse [g]"]
A_n = act_1/(1+ratio_tum_lobe*(m_tum/m_foie_lobe_d))
A_t = ratio_tum_lobe*A_n*(m_tum)/(m_foie_lobe_d)
print(f'Les activités dans le foie perfusé et la tumeur sont {A_n*1000:.2f} et {A_t*1000:.2f} MBq respectivement.')

### On peut alors estimer la dose à la tumeur
dose_t = A_t*1e9*T_y90_s*0.9336e6*1.6e-19/(m_tum*1e-3*np.log(2))
print(f'La dose à la tumeur est {dose_t:.2f} Gy')