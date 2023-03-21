#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:49:18 2023

@author: C. Martinez-Lombilla

A script to simulate a catalogue of simulated stars around Andromeda galaxy 
"""

import math
import random
import argparse

NSRC = 1_000_000


def skysim_parser():
    """
    Configure the argparse for skysim

    Returns
    -------
    parser : argparse.ArgumentParser
        The parser for skysim.
    """
    parser = argparse.ArgumentParser(prog='sky_sim', prefix_chars='-')
    parser.add_argument('--ra', dest = 'ra', type=float, default=None,
                        help="Central ra (degrees) for the simulation location")
    parser.add_argument('--dec', dest = 'dec', type=float, default=None,
                        help="Central dec (degrees) for the simulation location")
    parser.add_argument('--out', dest='out', type=str, default='catalog.csv',
                        help='destination for the output catalog')
    return parser


def get_radec():
    '''
    Determine Andromeda location in ra/dec degrees

    Returns
    -------
    Tuple with ra and dec values

    '''
    
    # from wikipedia
    RA = '00:42:44.3'
    DEC = '41:16:09'

    # convert to decimal degrees
    d, m, s = DEC.split(':')
    dec = int(d)+int(m)/60+float(s)/3600

    h, m, s = RA.split(':')
    ra = 15*(int(h)+int(m)/60+float(s)/3600)
    ra = ra/math.cos(dec*math.pi/180)
    
    return (ra, dec)


def make_stars(ra, dec, NSRC):
    '''
    Make 1000000 stars within 1 degree of Andromeda

    Parameters
    ----------
    ra : float
        ra in degrees
    dec : float
        dec in degrees
    NSRC : int
        number of stars to simulate

    Returns
    -------
    tuple with the lists of ra and dec values

    '''

    ras = []
    decs = []
    for i in range(NSRC):
        ras.append(ra + random.uniform(-1,1))
        decs.append(dec + random.uniform(-1,1))
    return (ras, decs)




def main():
    parser = skysim_parser()
    options = parser.parse_args()
    # if ra/dec are not supplied the use a default value
    if None in [options.ra, options.dec]:
        ra, dec = get_radec()
    else:
        ra = options.ra
        dec = options.dec
    
    ra, dec = get_radec()
    ras, decs = make_stars(ra, dec, NSRC)
    
    # now write these to a csv file for use by my other program
    with open(options.out,'w', encoding='utf-8') as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)
    print(f"Wrote {options.out}")


if __name__ ==  '__main__':
    main()