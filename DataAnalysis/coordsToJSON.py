import json

with open('data/coords.json', 'r', encoding='utf-8') as input:
    data = json.load(input)
with open('data/top50_postamats.json', 'r', encoding='utf-8') as rel_postamats:
    postamats = json.load(rel_postamats)
with open('data/top50_cashboxes.json', 'r', encoding='utf-8') as rel_cashboxes:
    cashboxes = json.load(rel_cashboxes)

postamats_coords = list()
for post in postamats.values():
    postamats_coords.append([str(post['coordsN'])] + [str(post['coordsS'])] + ['20'] + [str(post['Postamat_daily'])])

cashboxes_coords = list()
for cash in cashboxes.values():
    cashboxes_coords.append([str(cash['coordsN'])] + [str(cash['coordsS'])] + ['02'] + [str(cash['cashbox_daily'])])

coords = list()
for c in data.values():
    coords.append(c)

coords = coords + postamats_coords + cashboxes_coords
coords = sorted(coords, key=lambda x: x[2], reverse=True)

toOutput = list()
for c in coords:
    flag = True
    for el in toOutput:
        if c[0] == el[0] and c[1] == el[1]:
            flag = False
            break
    if flag:
        toOutput.append(c)

with open('data/toMap.json', 'w') as output:
    json.dump(toOutput, output)
