
# Denne kommandoen plotter ugedalplottet, samt eksporterer alle verdiene til en tabell
cat fisk_data.csv | python3 ugedal_calc.py -g 2 -a 10 -w 25 -d 1.5 2>&1 | tee -a ugedal_val.csv | python3 ugedal_plot.py -c Ørret,r,X,Røye,b,o -o figure.eps


cat fisk_data.csv | python3 scatter.py

cat fisk_data.csv | python3 antall.py

cat fisk_data.csv | python3 garn_lengde.py

cat fisk_data.csv | python3 meat_color.py
