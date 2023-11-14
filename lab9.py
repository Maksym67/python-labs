import pandas as pd
import matplotlib.pyplot as plt
from numpy import ceil

equipment_df = pd.read_csv('C:/Users/Максим/Desktop/IT Step Univ/Python/lab9/russia_losses_equipment.csv')
corrections_df = pd.read_csv('C:/Users/Максим/Desktop/IT Step Univ/Python/lab9/russia_losses_equipment_correction.csv')
personnel_df = pd.read_csv('C:/Users/Максим/Desktop/IT Step Univ/Python/lab9/russia_losses_personnel.csv')

print(equipment_df.head())
print(corrections_df.head())
print(personnel_df.head())
clear_equipment_na = equipment_df.dropna()
clear_equipment_dubl = equipment_df.drop_duplicates()

print(clear_equipment_na)
print(clear_equipment_dubl)
clear_corrections_na = corrections_df.dropna()
clear_corrections_dubl = corrections_df.drop_duplicates()

print(clear_corrections_na)
print(clear_corrections_dubl)
clear_personnel_na = personnel_df.dropna()
clear_personnel_dubl = personnel_df.drop_duplicates()

print(clear_personnel_na)
print(clear_personnel_dubl)
average_value_equipment = equipment_df['tank'].mean()
average_value_equipment = ceil(average_value_equipment)
print(average_value_equipment)

average_value_corrections = corrections_df['helicopter'].mean()
average_value_corrections = ceil(average_value_corrections)
print(average_value_corrections)

average_value_personnel  = personnel_df['personnel'].mean()
average_value_personnel  = ceil(average_value_personnel )
print(average_value_personnel)

plt.figure(figsize=(10,5))
plt.plot(equipment_df['date'], equipment_df['aircraft'])
plt.xlabel('Дата')
plt.ylabel('Кількість втраченої техніки')
plt.title('Динаміка втрат літаків')
plt.show()

plt.figure(figsize=(10,5))
plt.plot(personnel_df['date'], personnel_df['personnel'])
plt.xlabel('Дата')
plt.ylabel('Кількість втраченого особового складу')
plt.title('Динаміка втрат особового складу')
plt.show()