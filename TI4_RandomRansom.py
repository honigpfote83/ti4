#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import random as rd


# In[2]:


#Daten aus Rassenübersicht einlesen
df = pd.read_csv("F:/Users/Alain/Documents/ti4_rassenuebersicht.csv", sep=";")
#Technologie-Typologien einlesen
tech = pd.read_csv("F:/Users/Alain/Documents/ti4_techs.csv", sep=";")


# In[3]:


#Starteinheiten ermitteln & formattieren
starteinheiten = df[['Fraktion', 'Schlachtschiff', 'Zerstörer', 'Kreuzer', 'Träger', 'Jäger', 'Infanterie', 'Kriegssonne', 'Raumwerft', 'PVS']]
starteinheiten.set_index('Fraktion')


# In[4]:


#Anzahl Spieler ermitteln
nSpieler = int(input('Anzahl Spieler: '))+1


# In[5]:


#Spielernamen ermitteln
spieler =[]
for x in range(1, nSpieler):
    s = input(str(x) + ". Spieler: ")
    spieler.append(s)
spieler    


# In[6]:


#Für jeden Spieler einen Würfel werfen
würfel = pd.DataFrame({'Spieler': spieler, 'Würfelergebnis': rd.sample(range(0, 17), nSpieler-1)})


# In[7]:


#Fraktion gemäss Würfelwurf zuteilen
ergebnis = würfel.merge(df, left_on="Würfelergebnis", right_index=True, how="left")


# In[8]:


output = ergebnis[['Spieler','Fraktion', 'Heimatsystem (Nr.)', 'Heimatplaneten', 'Starttechnologien']]
output.set_index('Fraktion', inplace=True)


# In[11]:


f = output.merge(starteinheiten.astype(object), how='left', on='Fraktion').T
f = f.reindex(['Spieler', 'Fraktion', 'Heimatsystem (Nr.)', 'Heimatplaneten', 'Starttechnologien','Schlachtschiff','Zerstörer','Kreuzer','Träger','Jäger','Infanterie','Raumwerft','PVS'])
f.dropna(how='all', inplace=True)
f.fillna('-', inplace=True)


# In[12]:


for y in range(1, nSpieler):
    print(f.iloc[:,y-1])
    print("\n\n")

