# -*- coding: utf-8 -*-
from __future__ import print_function
from builtins import input
from six import iteritems
import csv

print("Quando ti verra' chiesto di inserire i nomi dei files \
\nricorda di inserire anche l'estensione oltre che il percorso.", end="\n")

# path_gis = 'gis.csv'
# path_sic = 'sic.csv'
# path_out = 'out.csv'
# path_dup = 'dup.csv'

path_gis = input("Inserisci il nome del file CSV esportato dal GIS [data/gis.csv]: ") or "data\\gis.csv"
path_sic = input("Inserisci il nome del file CSV esportato dal SIC [data/sic.csv]: ") or "data\\sic.csv"
path_out = input("Inserisci il nome del file CSV di output [out.csv]: ") or "out.csv"
path_dup = input("Inserisci il nome del file CSV dei toponomi duplicati (facoltativo): ") or None

def list_address(sic_len, field, froad):
    '''Define the address list based on the columns number'''
    address = []
    for i in range(sic_len):
        if i == 0:
            address.append(froad)
            address.append(field[i])
        else:
            address.append(field[i])
    return address

with open(path_gis, 'r') as r:
    spreadsheet = csv.reader(r, delimiter=',')
    gis = {}
    for row in spreadsheet:
        # Append "key: value" to dictionary
        gis[row[1] +' '+ row[2]] = row[0]
r.closed

with open(path_sic, 'r') as h:
    spreadsheet = csv.reader(h, delimiter=',')
    sic = tuple(spreadsheet)
    sic_len = len(sic[0])
h.closed

# Names comparison
# nam = {'contrada santa maria': 'contrada s.maria'}
if path_dup:
    with open(path_dup, 'r') as n:
        spreadsheet = csv.reader(n, delimiter=',')
        nam = {}
        for row in spreadsheet:
            nam[row[0]] = row[1]
    n.closed

with open(path_out, 'w') as o:
    writer = csv.writer(o, delimiter=',', lineterminator='\n')
    for field in sic:
        if field[0]+' '+field[1] in gis.keys():
            # Get dictionary value from "area di circolazione" key
            froad = gis[field[0]+' '+field[1]]
            # Write "area id", "area di circolazione", "numero", "esponente"
            writer.writerow(list_address(sic_len, field, froad))
        # Handle comparison with names dictionary
        else:
            if path_dup:
                for (key, value) in iteritems(nam):
                    if (field[0]+' '+field[1] == value): # 'contrada s.maria'
                        froad = gis[key] # gis['contrada santa maria']
                        writer.writerow(list_address(sic_len, field, froad))
o.closed
