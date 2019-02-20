#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = "Anders Johan Konnestad"
__project__ = "NATF100"

"""
Dette skriptet grupperer fisken inn i kjønnstaider og lager et histogram
hvor søylen blir farget etter fiskens kjøttfarge.

"""

import sys
import matplotlib.pyplot as plt

delim = ","

colour = {"Ørret":"r","Røye":"b"}

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
        
        meat_col = row[header.index("COLOUR")]
        try:
            stage = int(row[header.index("STAGE")])
        except:
            continue
        
        # opprett inndeling
        if not year in fisk_dict:
            fisk_dict[year] = {}
            
        if not species in fisk_dict[year]:
            fisk_dict[year][species] = {}
            fisk_dict[year][species]["Col_list"] = []
            
            
        ## Velg riktig alder!!
        # Reidar otolitt > otolitt > skjell
        
        
        # Count this fish
        if not stage == "NA":
            fisk_dict[year][species]["Col_list"].append((stage,meat_col))

colour_label= {"R":"Rød", "LR": "Lyserød", "H":"Hvit"}

nr = 0
for year in fisk_dict:
    for species in fisk_dict[year]:
        
        total_antall = 0
        
        print(fisk_dict[year][species], "\n\n")
        
        totalt_antall = len(fisk_dict[year][species])
        
        hex_farger = {"R":"#ff0000", "LR":"#ffa5a5","H":"#ffecec"}
        
        X_akse = [0,1,2,3,4,5,6,7,8,9,10]
        bunn = [0 for i in X_akse]
        
 
        #color
        for colour in ["R","LR","H"]:
            
            
            stages = [0,0,0,0,0,0,0,0,0,0,0]
            
            for i in range(0,10):
                count_amount = 0
                for j in fisk_dict[year][species]["Col_list"]:
                    print(i,j[0])
                    if i == j[0] and colour == j[1]:
                        count_amount += 1
                
                stages[i] = count_amount
                
                
                
            print(stages)
            
            label_ant = colour_label[colour] + " (n = " + str(sum(stages)) + ")"
            
            total_antall += sum(stages)
            
            er_her = False
                
            for i in fisk_dict[year][species]["Col_list"]:
                if i[1] == colour:
                    er_her = True
            
            if er_her:
                plt.bar(X_akse, stages, color=hex_farger[colour],
                        bottom = bunn,
                        edgecolor='black', width=1,
                        label = label_ant
                        )
            
            for nr, val in enumerate(stages):
                bunn[nr] +=  val
            
            
            plt.xlim([0,8])
            plt.ylim(0, 14)
            
            plt.xticks([1,2,3,5,7],["I","II","III","V","VII"])
            

        
            plt.xlabel("Kjønnstadie")
            plt.ylabel("Antall")

            
        plt.title(str(species) + " " + str(year) + " (n = " + str(total_antall) + ")")
        
        line_w = 1 # set linewidth
        for l in range(0,20,2):
            plt.axhline(y=l, xmin=0.0, xmax=20, color="grey", linewidth=line_w,
                        linestyle='dashed', zorder=0)
            
        plt.legend()
        plt.savefig("figures/" + "kjottfarge_kjonnstadie_" + species + "_" + str(year) + ".eps")
        plt.clf()
        plt.cla()
        plt.close()
        
print(fisk_dict)
