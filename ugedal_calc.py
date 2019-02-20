#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = "Anders Johan Konnestad"
__project__ = "NATF100"

"""
This script calculates values for the Ugedal grading system.

"""

import argparse
import sys

delim = ","

###### CLI flag input
## Disse brukes for garnserieinformasjonen!

parser = argparse.ArgumentParser()
parser.add_argument("-g", "--garnserier", help="Antall garngarnserier", type=int, default=2)
parser.add_argument("-a", "--antall", help="Antall garn i en garnserie", type=int,  default=10)

parser.add_argument("-w", "--width", help="Garnets bredde i meter", type=float, default=25)
parser.add_argument("-d", "--depth", help="Garnets hoyde i meter", type=float, default=1.5)

args = parser.parse_args()
#####

#####
#Antall garnnetter = arninnstats
# garninnstats = antall garn x garnserier
garninnsats =  args.antall * args.garnserier

#garnareal for en garnserie
garnareal = (args.width * args.depth) * args.antall

#Omregningsfaktor, garnkonstant for garnserien
garnkonstant = 100 / garnareal

#####


#### Read datasett
fisk_dict = {}
for nr, line in enumerate(sys.stdin):
    if line == "\n":
        #remove empty lines
        continue
    
    row = line.replace("\n","").split(delim)
    
    
    if nr == 0:
        header = row
    else:
        year = int(row[header.index("YEAR")])
        species = row[header.index("SPECIES")]
        gender = row[header.index("GENDER")]
        
        try:
            stage = int(row[header.index("STAGE")])
        except:
            # verdien for kjonnstadie mangler
            stage = "N/A" # Not available
            continue
        
        
        # opprett inndeling
        if not year in fisk_dict:
            fisk_dict[year] = {}
            
        if not species in fisk_dict[year]:
            fisk_dict[year][species] = {}
            fisk_dict[year][species]["Antall"] = 0
            fisk_dict[year][species]["len_hunnfisk"] = []
            

        # Count this fish
        fisk_dict[year][species]["Antall"] += 1
        
        # antall kjonnsmoden hunnfisk
        if gender == "female":
            try:
                stage = int(row[header.index("STAGE")])
            except:
                # verdien for kjonnstadie mangler
                continue
            
            # velg kun kjonnsmoden (Stadie III eller hoyere)
            if stage >= 3:
                
                try:
                    lengde = float(row[header.index("LENGTH")])
                except:
                    #fiskens lengde mangler
                    continue
                
                fisk_dict[year][species]["len_hunnfisk"].append(lengde)


## Analyse data og print to stdout

header_list = []
header_list.append("YEAR")
header_list.append("SPECIES")
header_list.append("Bestandtetthet (antall fisk per 100m² garn)")
header_list.append("Gjennomsnittlengde av kjønnsmodne ($\geq$III) hunner (cm)")
print(delim.join(header_list))            

for year in fisk_dict:
    for species in fisk_dict[year]:
        
        hunnfisk_list = fisk_dict[year][species]["len_hunnfisk"]
        mean_hunnfisk_len = float(sum(hunnfisk_list)/len(hunnfisk_list))
        
        
        antall = fisk_dict[year][species]["Antall"]
        tetthet = float(( antall / args.garnserier) * garnkonstant)
        
        print(delim.join([str(year), species, str(tetthet), str(mean_hunnfisk_len)]))
        
