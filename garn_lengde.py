#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = "Anders Johan Konnestad"
__project__ = "NATF100"

"""
Dette skriptet lager boxplot av fisken lengde gruppert etter maskevidden på garnet de ble fanget i.
Med dette kan vi se om fiskens lengde påvirker fangbarheten i forskjellige garn.

"""

import sys
import matplotlib.pyplot as plt

delim = ","

colour = {"Ørret":"r","Røye":"b"}

fisk_dict = {}

mv_liste = []

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

        ww = str(row[header.index("WEBWIDTH")])
        length = float(row[header.index("LENGTH")])

        try:
            int_val = float(ww)
        except:
            int_val = "NA"
            continue
        
        
        if not species in fisk_dict:
            fisk_dict[species] = {}
        
        if not ww in fisk_dict[species]:
            fisk_dict[species][ww] = []
            
        if not float(ww) in mv_liste:
            mv_liste.append(float(ww))
        
        fisk_dict[species][ww].append(length)
        
for ww in sorted(mv_liste):
    print(ww)
    
mv_liste = [16.5, 19.5, 22.5, 24, 26, 29, 31, 35, 39, 45]

fisk_farge = {"Røye":"#8080ff", "Ørret":"#80ff80"}

        
for species in fisk_dict:
    data = [ [] for i in mv_liste]
    
    for ww in fisk_dict[species]:
        fisk_dict[species][ww]
        data[sorted(mv_liste).index(float(ww))].append(fisk_dict[species][ww])
        
    line_w = 1 # set linewidth
    for l in range(0,50,5):
        plt.axhline(y=l, xmin=0.0, xmax=20, color="grey", linewidth=line_w,
                    linestyle='dashed', zorder=0)
    
                
    plt.xlabel("Maskevidde (mm)")
    plt.ylabel("Lengde (cm)")
        
    plt.xlim(0, 10)
    plt.ylim(0, 50)
    
    medianprops = dict(linestyle='-', linewidth=1, color='black')
    
    total_antall = 0
    for i in data:
        try:
            total_antall += len(i[0])
        except:
            pass
    
    label_antall = species + " (n = " + str(total_antall) +")"
    
    plt.title(str(species) + " (n = " + str(total_antall) +")")
   
    box = plt.boxplot(data, patch_artist=True,
                      medianprops=medianprops,
                      )
        
    colors = [fisk_farge[species] for i in mv_liste]
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
    
    for i in box:
        print(i)
    
    x_list = []
    
    for nr, line in enumerate(box['whiskers']):
        x, y = line.get_xydata()[1]
        if not int(x) in x_list:
            x_list.append(x)
            
            try:
                print(data[int(x) - 1][0])
                label_name = "$(n = " + str(len(data[(int(x) - 1)][0])) + ")$"
                plt.text(x, y - 4, label_name, fontsize=8,
                         horizontalalignment='center')
            except:
                pass
        
    
    plt.xticks([i for i in range(1,11)], [i for i in sorted(mv_liste)])
    
    plt.legend()
    plt.savefig("figures/" + "alder-lengde_" + species + ".eps")
    plt.clf()
    plt.cla()
    plt.close()
   
