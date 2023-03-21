#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 12:00:02 2023

@author: C. Martinez-Lombilla
"""


'''

La manera de hacer funciones para testear codigos:
    
    
def test_that_a_thing_works():
    # do things
    if not thing_works:
        raise AssertionError("Description of what failed")
    return
'''

from numpy import testing


def test_module_import():
    try:
        import mymodule.sky_sim
    except Exception as e:
        raise AssertionError("Failed to import mymodule")
    return



def test_get_radec():
    from mymodule import sky_sim
    answer = (14.215420962967535, 41.26916666666666)
    result = sky_sim.get_radec()
    
    testing.assert_allclose(answer, result, rtol=1e-8)
    return