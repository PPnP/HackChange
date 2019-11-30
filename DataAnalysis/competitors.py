import pandas as pd
import json


data = pd.read_excel('data/postamats.xls')
area = data[(data['Область'] == 'Калужская обл.') | (data['Область'] == 'Тульская обл.')]

competitors = area.loc[area['Название пункта приема/выдачи'].apply(lambda x: x.find('Пятерочка') == -1 and x.find('Карусель') == -1)]

coords = dict()
for index, row in competitors.iterrows():
    coords[row['Адрес пункта приема/выдачи']] = [str(row['Долгота']), str(row['Широта'])]

with open('data/competitors.json', 'w') as output:
    json.dump(coords, output)
