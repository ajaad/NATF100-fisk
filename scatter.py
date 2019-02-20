#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = "Anders Johan Konnestad"
__project__ = "NATF100"

"""
Scatterplot, lengde mot alder

"""

import sys
import matplotlib.pyplot as plt
import numpy as np

delim = ","


fisk_dict = {}
for nr, line in enumerate(sys.stdin):
    
    count = 0
    if line == "\n":
        #remove empty lines
        continue
    
    row = line.replace("\n","").split(delim)
    
    
    if nr == 0:
        header = row
    else:
        year = int(row[header.index("YEAR")])
        species = row[header.index("SPECIES")]
        


        
        # opprett inndeling
        if not year in fisk_dict:
            fisk_dict[year] = {}
            
        if not species in fisk_dict[year]:
            fisk_dict[year][species] = {}
            fisk_dict[year][species]["age_len"] = []
            fisk_dict[year][species]["antall"] = 0

        try:
            length = float(row[header.index("LENGTH")]) 
        except:
            continue
        
        try:

            
            age = int(row[header.index("REIDAR_O")])
            fisk_dict[year][species]["age_len"].append((age,length))
        except:
            try:
                age = int(row[header.index("AGE_O")])
                fisk_dict[year][species]["age_len"].append((age,length))
            except:
                try:
                    age = int(row[header.index("AGE_S")])
                    fisk_dict[year][species]["age_len"].append((age,length))
                except:
                    continue
        
fisk_farge = {"Røye":"#8080ff", "Ørret":"#80ff80"}
fisk_mark = {"Røye":"o", "Ørret":"X"}
        
nr = 0
for year in fisk_dict:
    for species in fisk_dict[year]:
        
        age_len = fisk_dict[year][species]["age_len"]
        
        age_list = [a[0] for a in age_len]
        len_list = [l[1] for l in age_len]
        

        
        z = np.polyfit(age_list, len_list, 1)
        
        p = np.poly1d(z)
        
        print(p(age_list))
        
        x_trend = [min(age_list),max(age_list)]
        y_trend = [min(p(age_list)),max(p(age_list))]
        
        print("y_trend: ", y_trend)
        print("x_trend: ", x_trend)

        x_delta = abs(min(age_list) - max(age_list))
        y_delta = abs(min(p(age_list)) - max(p(age_list)))
        
        stigning = (y_delta/x_delta)
        brytning = min(p(age_list)) - (min(age_list) * stigning)
        
        print("br",min(age_list),stigning,brytning)
        
        formelstr = str(round(stigning,2)) + "x + " + str(round(brytning,2))
        
        plt.plot(x_trend,y_trend,"--",
                 color = fisk_farge[species],
                 linewidth=1,
                 label = formelstr)

        sp_label = str(species + " (n = " + str(len(age_list)) + ")")
        
        plt.scatter(age_list,
                    len_list,
                    color = fisk_farge[species],
                    label = sp_label,
                    marker = fisk_mark[species]
                    )        
        
        plt.title(species + " - " + str(year))
        
        plt.xlabel("Alder")
        plt.ylabel("Lengde (cm)")
            
        plt.xlim(0, 20)
        plt.ylim(0, 50)
        
        line_w = 1 # set linewidth
        for l in range(0,50,10):
            plt.axhline(y=l, xmin=0.0, xmax=50, color="grey", linewidth=line_w,
                        linestyle='dashed', zorder=0)
            
        plt.xticks([5,10,15,20],[5,10,15,20])
        
        
        plt.legend()
        plt.savefig("figures/" + "scatter_" + species + "_" + str(year) + ".eps")
        plt.clf()
        plt.cla()
        plt.close()
        
        print("minste y:",min(p(age_list)))
