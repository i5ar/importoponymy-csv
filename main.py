#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import print_function

importoponymy_info = {
    "name": "Importoponymy CSV",
    "author": "iSar",
    "year": "2016",
    "version": (0, 0, 1),
    "python": (2, 7, 10),
    "wiki_url": "",
    "tracker_url": "https://github.com/i5ar/importoponymy-csv/",
    "description": "Line up big data with ease using CSV" }

from builtins import input
from six import iteritems
import os
import csv
from csv import Sniffer

isar_ascii_logo = '''\
              ::::::::  ::::::::        :::::::::
           :::::::::::  :::::::::::   :::::::::::
          ::::                  :::: ::::
          :::                    ::: :::
          :+++:                :+++: :+:
            :+++:            :+++:   :+:
 +#+          +###+        +###+     +#+
 +#+            +###+    +###+   #+  +#+
 ###              +##+  +##+     ##+ ###
 ###              +###  ###+     ### ###
 +###+           +###+  +###+  +###+ ###
   ##################    #########   ###
     ##############        #####     ###
'''

print(importoponymy_info['name'], '.'.join(map(str, importoponymy_info['version'])), end="\n")
print('Copyright (c)', importoponymy_info['year'], importoponymy_info['author'], end="\n\n")
print(isar_ascii_logo, end="\n")

# path_gis = 'gis.csv'
# path_sic = 'sic.csv'
# path_out = 'out.csv'
# path_dup = 'dup.csv'

path_gis = input("Inserisci il nome del file CSV esportato dal GIS [data/gis.csv]: ") or "data\\gis.csv"
path_sic = input("Inserisci il nome del file CSV esportato dal SIC [data/sic.csv]: ") or "data\\sic.csv"
path_out = input("Inserisci il nome del file CSV di output [out.csv]: ") or "out.csv"
path_dup = input("Inserisci il nome del file CSV dei toponomi duplicati (facoltativo): ") or None

def add_extension(path):
    '''Add extension if not provided'''
    basename = os.path.basename(os.path.normpath(path))
    if '.csv' in basename:
        return path
    else:
        return path + '.csv'

def list_address(sic_len, field, froad):
    '''List address based on the columns number'''
    address = []
    for i in range(sic_len):
        if i == 0:
            # Append "ID area"
            address.append(froad)
            # Append "DUG area"
            address.append(field[i])
        else:
            address.append(field[i])
    return address

with open(add_extension(path_gis), 'r') as file_gis:
    # https://docs.python.org/dev/library/csv.html
    has_header = Sniffer().has_header(file_gis.read(1024))
    file_gis.seek(0)
    spreadsheet = csv.reader(file_gis, delimiter=',')
    gis = {}
    for row in spreadsheet:
        if has_header:
            # Skip first line
            has_header = False
            # print("GIS has header.", end="")
            continue
        else:
            # Append "key: value" to dictionary
            gis[row[1] +' '+ row[2]] = row[0]
file_gis.closed

with open(add_extension(path_sic), 'r') as file_sic:
    has_header = Sniffer().has_header(file_sic.read(1024))
    file_sic.seek(0)
    spreadsheet = csv.reader(file_sic, delimiter=',')
    if has_header:
        sic = tuple(spreadsheet)[1:]
        # print("SIC has header.", end="")
    else:
        sic = tuple(spreadsheet)
    sic_len = len(sic[0])
file_sic.closed

# Names comparison
# dup = {'contrada santa maria': 'contrada s.maria'}
if path_dup:
    with open(add_extension(path_dup), 'r') as file_dup:
        spreadsheet = csv.reader(file_dup, delimiter=',')
        dup = {}
        for row in spreadsheet:
            dup[row[0]] = row[1]
    file_dup.closed

with open(add_extension(path_out), 'w') as o:
    writer = csv.writer(o, delimiter=',', lineterminator='\n')
    i = 0
    for field in sic:

        # Add header
        if i == 0:
            i += 1
            address = []
            for i in range(sic_len):
                if i == 0:
                    address.append('froad')
                    address.append('gname')
                elif i == 1:
                    address.append('rname')
                else:
                    address.append('')
            writer.writerow(address)
        else:

            if field[0]+' '+field[1] in gis.keys():
                # Get dictionary value from "area di circolazione" key
                froad = gis[field[0]+' '+field[1]]
                # Write "ID area", "DUG area" "nome area", "numero", "esponente"
                writer.writerow(list_address(sic_len, field, froad))
            # Handle comparison with names dictionary
            else:
                if path_dup:
                    for (key, value) in iteritems(dup):
                        if (field[0]+' '+field[1] == value): # 'salita a.bucco'
                            froad = gis[key] # gis['salita artie bucco']
                            writer.writerow(list_address(sic_len, field, froad))
o.closed
