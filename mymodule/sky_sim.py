#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:49:18 2023

@author: C. Martinez-Lombilla
"""

# Determine Andromeda location in ra/dec degrees 
# ^- Missing module docstring (missing-module-docstring)

# from wikipedia
ra = '00:42:44.3' 
# ^- Constant name "ra" doesn't conform to UPPER_CASE naming style (invalid-name)
dec = '41:16:09'  
# ^- Constant name "dec" doesn't conform to UPPER_CASE naming style (invalid-name)

# convert to decimal degrees
from math import *  
# ^- Redefining built-in 'pow' (redefined-builtin)
# ^- Wildcard import math (wildcard-import)
# ^- Import "from math import *" should be placed at the top of the module (wrong-import-position)
# ^- W0614: Unused import(s) acos, acosh, asin, asinh, atan, atan2, atanh, ceil, comb, copysign, cosh, degrees, dist, e, erf, erfc, exp, expm1, fabs, factorial, floor, fmod, frexp, fsum, gamma, gcd, hypot, inf, isclose, isfinite, isinf, isnan, isqrt, ldexp, lgamma, log, log10, log1p, log2, modf, nan, perm, pow, prod, radians, remainder, sin, sinh, sqrt, tan, tanh, tau and trunc from wildcard import of math (unused-wildcard-import)

d, m, s = dec.split(':')
dec = int(d)+int(m)/60+float(s)/3600

h, m, s = ra.split(':')
ra = 15*(int(h)+int(m)/60+float(s)/3600)
ra = ra/cos(dec*pi/180)

nsrc = 1_000_000
# ^- Constant name "nsrc" doesn't conform to UPPER_CASE naming style (invalid-name)

# make 1000 stars within 1 degree of Andromeda
from random import *
# ^- Wildcard import math (wildcard-import)
# ^- Import "from math import *" should be placed at the top of the module (wrong-import-position)
# ^- Unused import(s) NV_MAGICCONST, TWOPI, LOG4, SG_MAGICCONST, BPF, RECIP_BPF, Random, SystemRandom, seed, random, triangular, randint, choice, randrange, sample, shuffle, choices, normalvariate, lognormvariate, expovariate, vonmisesvariate, gammavariate, gauss, betavariate, paretovariate, weibullvariate, getstate, setstate and getrandbits from wildcard import of random (unused-wildcard-import)

ras = []
decs = []
for i in range(nsrc):
    ras.append(ra + uniform(-1,1))
    decs.append(dec + uniform(-1,1))


# now write these to a csv file for use by my other program
f = open('catalog.csv','w')
# ^- Using open without explicitly specifying an encoding (unspecified-encoding)
# ^- Consider using 'with' for resource-allocating operations (consider-using-with)

print("id,ra,dec", file=f)
for i in range(nsrc):
    print("{0:07d}, {1:12f}, {2:12f}".forgit logmat(i, ras[i], decs[i]), file=f)
    # ^- Formatting a regular string which could be a f-string (consider-using-f-string)