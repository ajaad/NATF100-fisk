Løsningsforslag for fiskeoppgave i NATF100
==========================================

Denne pakken ble skrevet som løsningsforslag til fiskeoppgaven i NATF100 ved Norges miljø- og biovitenskapelige universitet (NMBU).

Resultatene fra prøvefisket (august 2017 og 2018) ligger i filen fisk_data.csv.
Tabellene ligger i "losningsforslag_og_kommentarer.pdf" sammen med generelle kommentarer til semesteroppgavene.


## Ugedals karaktersystem (koordinatsystem)

Dette er et karaktersystem for kvaliteten på fiskevann.
Med å bruke dette karaktersystemet vil man kunne sammenligne fiskevann opp mot hverandre.


karakter blir satt basert på gjennomsnittstørrelsen til kjønnsmoden hunnfisk (y-aksen) og fiskebestandens tetthet (x-aksen).

```bash
$ cat fisk_data.csv | python3 ugedal_calc.py -g 2 -a 10 -w 25 -d 1.5 2>&1 | tee ugedal_val.csv | python3 ugedal_plot.py -c Ørret,r,X,Røye,b,o -o figure.eps
```
### ugedal_calc

Dette skriptet vil gi en tabell med de nødvendige koordinatene for å sette karakter.

- -g = antall garnserier
- -a = antall garn per garnserie
- -w = garnets lengde
- -d = garnets høyde


### ugedal_plot

Dette skriptet vil bruke tabellen fra ugedal_calc.py til å produsere et plot.

- -c fiskeart1,vektorfarge,symbol,fiskeart2,vektorfarge,symbol
- -o outputfigur


## Scatterplot

```bash
$ cat fisk_data.csv | python3 scatter.py
```

Dette skriptet lager en lineær funksjon mellom lengde og alder,
samt produserer plot for hver art for hvert år.


## Alder (histogram)

```bash
$ cat fisk_data.csv | python3 antall.py
```

Dette skriptet tegner histogrammer som grupperer fiskene inn i alder.

## Fiskelengde og maskevidde (boxplot)

```bash
$ cat fisk_data.csv | python3 garn_lengde.py
```

Dette skriptet lager boxplot av fisken lengde gruppert etter maskevidden på garnet de ble fanget i.
Med dette kan vi se om fiskens lengde påvirker fangbarheten i forskjellige garn.

## Kjøttfarge (histogram)

```bash
$ cat fisk_data.csv | python3 meat_color.py
```

Dette skriptet grupperer fisken inn i kjønnstaider og lager et histogram hvor søylen blir farget etter fiskens kjøttfarge.


## Alt sammen

Alternativt kan alle utregninger gjøres ved å bruke execute.sh-scriptet.

```bash
$ bash execute.sh
```


### Kontakt

Disse skriptene er ikke superlette å lese, men jeg håper de likevell kan benyttes til å
regne ut løsningsforslag senere år.
Jeg håper også at de kan være til hjelp for dem som trenger det til andre oppdrag.


 Anders Johan Konnestad
 ankonnes@nmbu.no




