#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = "Anders Johan Konnestad"
__project__ = "NATF100"

"""
This scipt asses values and insert them into a ugedal coordinate system.

"""

import sys
import argparse
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="Filnavn til output (figure.eps)", type=str, default="figure.eps")

parser.add_argument("-c", "--color", help="Fiskefarge (Ørret,r,Røye,b)", type=str, default="Ørret,#80ff80,X,Røye,#8080ff,o")

args = parser.parse_args()


color_list = args.color.split(",")

delim = ","

innsjo_navn = "Sandvatn"

fisk_dict = {}
year_list = []

for nr, line in enumerate(sys.stdin):
    if line == "\n":
        #remove empty lines
        continue
    
    row = line.replace("\n","").split(",")
    if nr == 0:
        header = row
    else:
        species = row[1]
        
        if not species in fisk_dict:
            fisk_dict[species] = {}
            fisk_dict[species]["X"] = []
            fisk_dict[species]["Y"] = []
        
        fisk_dict[species]["X"].append(float(row[2]))
        fisk_dict[species]["Y"].append(float(row[3]))
        
        year_list.append(int(row[0]))
        
    

ax = plt.axes()

# define graph extent
plt.xlim(0, 20)
plt.ylim(0, 50)

# set title and axis lables
title_name = innsjo_navn + " " + str(min(year_list)) + " - " + str(max(year_list))

plt.title("UGEDAL PLOT \n " + title_name)
plt.xlabel(header[2])
plt.ylabel(header[3])

line_w = 1 # set linewidth

# add horizontal lines
ax.axhline(y=25, xmin=0.0, xmax=20, color="grey", linewidth=line_w)
ax.axhline(y=35, xmin=0.0, xmax=20, color="grey", linewidth=line_w)

# add vertical lines
ax.axvline(x=5, ymin=0.0, ymax=50, color="grey", linewidth=line_w)
ax.axvline(x=15, ymin=0.0, ymax=50, color="grey", linewidth=line_w)


# bokstaver
bokstav_tup = [(2.5,43),(10,43),(17.5,43),
               (2.5,30),(10,30),(17.5,30),
               (2.5,12),(10,12),(17.5,12)]
alfabeta = "ABCDEFGHIJKLM"

for nr, tup in enumerate(bokstav_tup):
    plt.plot(tup[0],tup[1],marker="$" + alfabeta[nr] + "$",
    color="grey", linewidth=2, markersize=12)
    #fontweight="normal")

for species in fisk_dict:
    colour = color_list[color_list.index(species) + 1]
    mark = color_list[color_list.index(species) + 2]
    
    # plot halve vektorer
    for i in range(0, len(fisk_dict[species]["X"])):
        if (i - 1) >= 0:
            x_vect = (fisk_dict[species]["X"][i] - fisk_dict[species]["X"][i -1])/2
            y_vect = (fisk_dict[species]["Y"][i] - fisk_dict[species]["Y"][i - 1])/2
            
            ax.arrow(fisk_dict[species]["X"][i - 1],
                     fisk_dict[species]["Y"][i - 1],
                     x_vect, y_vect,
                     head_width=0.8, head_length=1.2, color=colour)
    
    plt.plot(fisk_dict[species]["X"],fisk_dict[species]["Y"],
             color=colour,
             label = species, marker = mark)

plt.legend()
plt.savefig(args.output)

