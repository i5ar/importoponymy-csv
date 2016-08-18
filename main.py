# -*- coding: utf-8 -*-
import csv
from builtins import input
from six import iteritems

# Source
# path_gis = 'in-gis.csv'
# path_sic = 'in-sic.csv'
path_gis = input("Inserisci il nome del file CSV esportato dal GIS (completo di percorso ed estensione): ")
path_sic = input("Inserisci il nome del file CSV esportato dal SIC (completo di percorso ed estensione): ")
# Destination
# path_out = 'out.csv'
path_out = input("Inserisci il nome del file CSV di output (completo di percorso ed estensione): ")

with open(path_gis, 'r') as r:
    spreadsheet = csv.reader(r, delimiter=',')
    dic = {} # key: value
    for row in spreadsheet:
        # Append "key: value" to dictionary
        dic[row[1] +' '+ row[2]] = row[0]
r.closed

with open(path_sic, 'r') as h:
    spreadsheet = csv.reader(h, delimiter=',')
    lst = []
    for row in spreadsheet:
        # Append tuple ("area di circolazione", "numero", "esponente") to list
        lst.append((row[0] +' '+ row[1], row[2], row[3], row[4]))
h.closed

# Comparison "SIC: GIS" names
# names = {
#     'contrada santa maria': 'contrada s.maria',
# }
path_names = input("Inserisci il nome del file CSV delle associazioni dei toponimi (completo di percorso ed estensione): ")
with open(path_names, 'r') as n:
    spreadsheet = csv.reader(n, delimiter=',')
    names = {} # key: value
    for row in spreadsheet:
        # Append "key: value" to dictionary
        names[row[0]] = row[1]
n.closed

with open(path_out, 'w') as o:
    writer = csv.writer(o, delimiter=',', lineterminator='\n')
    for field in lst:
        if field[0] in dic.keys():
            # Get dictionary value from "area di circolazione" key
            area_id = dic[field[0]]
            # Write "area id", "area di circolazione", "numero", "esponente"
            writer.writerow([area_id, field[0], field[1], field[2], field[3]])
        # Handle comparison
        else:
            for (key, value) in iteritems(names):
                if (field[0] == value): # 'contrada s.maria'
                    area_id = dic[key] # dic['contrada santa maria']
                    writer.writerow([area_id, field[0], field[1], field[2], field[3]])

o.closed
