#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = "Anders Johan Konnestad"
__project__ = "NATF100"

"""
Dette skriptet tegner histogrammer som grupperer fiskene inn i alder.

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
        gender = row[header.index("GENDER")]

        # opprett inndeling
        if not year in fisk_dict:
            fisk_dict[year] = {}
            
        if not species in fisk_dict[year]:
            fisk_dict[year][species] = {}
            fisk_dict[year][species]["Reidar"] = []
            fisk_dict[year][species]["Otolitt"] = []
            fisk_dict[year][species]["Skjell"] = []

        
        
        try:
            age = int(row[header.index("REIDAR_O")])
            fisk_dict[year][species]["Reidar"].append(age)
        except:
            try:
                age = int(row[header.index("AGE_O")])
                fisk_dict[year][species]["Otolitt"].append(age)
            except:
                try:
                    age = int(row[header.index("AGE_S")])
                    fisk_dict[year][species]["Skjell"].append(age)
                except:
                    continue
        

nr = 0
ages = [age for age in range(0,21)]
"""
bestem_colour = {"Reidar":"#0000ff",
                 "Otolitt":"#7777ff",
                 "Skjell":"#b6b6ff"}
"""


bestem_colour = {"Reidar":"2c",
                 "Otolitt":"80",
                 "Skjell":"ec"}

col_place = {"Røye":2,"Ørret":1}


alders_rekkefolge = ["Reidar",  "Otolitt", "Skjell"]

for year in fisk_dict:
    for species in fisk_dict[year]:
        plots = {}
        bunn = [ 0 for zero in range(0,21)]
        total_bestem = 0
        for bestem in alders_rekkefolge:
        
            print(bestem)
            
            colour_place = {"Røye":"#0000ff","Ørret":"#ff0000"}
            
            
            
            
            if len(fisk_dict[year][species][bestem]) != 0 or not bestem in fisk_dict[year][species]:
                print(fisk_dict[year][species][bestem])
                print(ages)
                print(bestem)
                
                ages_list = [ 0 for zero in range(0,21)]
                
                for val in fisk_dict[year][species][bestem]:
                    ages_list[val] += 1
                    
                col_string = "#"
                for i in range(0,3):
                    if not col_place[species] == i:
                        col_string += bestem_colour[bestem]
                    else:
                        col_string += "ff"
                print(col_string)
                
                label_bestm = str(bestem + " (n = " + str(sum(ages_list)) + ")")
                total_bestem += sum(ages_list)
                
                
                plots[bestem] = plt.bar(ages, ages_list,
                     color=col_string,
                     bottom = bunn,
                     edgecolor='black', width=1,
                     label = label_bestm)
                
                for nr, val in enumerate(ages_list):
                    bunn[nr] +=  val
                
                # add horizontal lines
                line_w = 1 # set linewidth
                for l in range(0,20,2):
                    plt.axhline(y=l, xmin=0.0, xmax=20, color="grey", linewidth=line_w,
                                linestyle='dashed', zorder=0)
                
                
        plt.title(str(species) + " " + str(year) + " (n =" + str(total_bestem) +")")
                
        plt.xlabel("Alder")
        plt.ylabel("Antall")
        
        plt.xlim(0, 21)
        plt.ylim(0, 12)

                
        plt.tick_params(axis='x', labelsize=6)

        
        plt.xticks(ages, ages)
        
        plot_this_func = []
        plot_this_name = []
        for p in alders_rekkefolge:
            if p in plots:
                plot_this_func.append(plots[p])
                plot_this_name.append(p)
        
        plt.legend(plot_this_func, plot_this_name)

        plt.legend()
        plt.savefig("figures/" + "aldrsfordeling_" + species + "_" + str(year) + ".eps")
        plt.clf()
        plt.cla()
        plt.close()
                
        nr += 1

print(fisk_dict)

