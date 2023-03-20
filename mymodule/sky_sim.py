#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:49:18 2023

@author: C. Martinez-Lombilla

A script to simulate a catalogue of simulated stars around Andromeda galaxy 
"""

# Determine Andromeda location in ra/dec degrees 
# from wikipedia
RA = '00:42:44.3' 
DEC = '41:16:09'  

# convert to decimal degrees
from math import cos, pi  

d, m, s = DEC.split(':')
DEC = int(d)+int(m)/60+float(s)/3600

h, m, s = RA.split(':')
RA = 15*(int(h)+int(m)/60+float(s)/3600)
RA = RA/cos(DEC*pi/180)

NSRC = 1_000_000

# make 1000 stars within 1 degree of Andromeda
from random import *
# ^- Wildcard import math (wildcard-import)
# ^- Import "from math import *" should be placed at the top of the module (wrong-import-position)
# ^- Unused import(s) NV_MAGICCONST, TWOPI, LOG4, SG_MAGICCONST, BPF, RECIP_BPF, Random, SystemRandom, seed, random, triangular, randint, choice, randrange, sample, shuffle, choices, normalvariate, lognormvariate, expovariate, vonmisesvariate, gammavariate, gauss, betavariate, paretovariate, weibullvariate, getstate, setstate and getrandbits from wildcard import of random (unused-wildcard-import)

ras = []
decs = []
for i in range(NSRC):
    ras.append(RA + uniform(-1,1))
    decs.append(DEC + uniform(-1,1))


# now write these to a csv file for use by my other program
f = open('catalog.csv','w')
# ^- Using open without explicitly specifying an encoding (unspecified-encoding)
# ^- Consider using 'with' for resource-allocating operations (consider-using-with)

print("id,ra,dec", file=f)
for i in range(NSRC):
    print("{0:07d}, {1:12f}, {2:12f}".format(i, ras[i], decs[i]), file=f)
    # ^- Formatting a regular string which could be a f-string (consider-using-f-string)
    
    
    
    
    
    