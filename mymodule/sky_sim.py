#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:49:18 2023

@author: C. Martinez-Lombilla

A script to simulate a catalogue of simulated stars around Andromeda galaxy 
"""

import math
import random

# Determine Andromeda location in ra/dec degrees 
# from wikipedia
RA = '00:42:44.3' 
DEC = '41:16:09'  

# convert to decimal degrees
d, m, s = DEC.split(':')
DEC = int(d)+int(m)/60+float(s)/3600

h, m, s = RA.split(':')
RA = 15*(int(h)+int(m)/60+float(s)/3600)
RA = RA/math.cos(DEC*math.pi/180)

NSRC = 1_000_000

# make 1000 stars within 1 degree of Andromeda
ras = []
decs = []
for i in range(NSRC):
    ras.append(RA + random.uniform(-1,1))
    decs.append(DEC + random.uniform(-1,1))


# now write these to a csv file for use by my other program
with open('catalog.csv','w', encoding='utf-8') as f:  
    print("id,ra,dec", file=f)
    for i in range(NSRC):
        print(f"{0:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)