import pandas as pd
import matplotlib.pyplot as plt

equipment_df = pd.read_csv('russia_losses_equipment.csv')
corrections_df = pd.read_csv('russia_losses_equipment_correction.csv')
personnel_df = pd.read_csv('russia_losses_personnel.csv')

equipment_df.drop_duplicates(inplace=True)
corrections_df.drop_duplicates(inplace=True)
personnel_df.drop_duplicates(inplace=True)

equipment_df.dropna(inplace=True)
corrections_df.dropna(inplace=True)
personnel_df.dropna(inplace=True)

equipment_stats = equipment_df.describe()
corrections_stats = corrections_df.describe()
personnel_stats = personnel_df.describe()

grouped_equipment = equipment_df.groupby(equipment_df['date'].str.slice(0, 4)).sum()

sorted_equipment = equipment_df.sort_values(by='aircraft', ascending=False)

plt.figure(figsize=(10, 5))
plt.plot(equipment_df['date'], equipment_df['aircraft'], label='Втрати техніки')
plt.xlabel('Дата')
plt.ylabel('Кількість втраченої техніки')
plt.title('Динаміка втрат техніки')
plt.legend()
plt.show()