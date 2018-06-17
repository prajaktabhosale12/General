# -*- coding: utf-8 -*-
"""
Created on Thu May 18 12:09:06 2017

@author: prjkt
"""
import universe

def main():
    try:
        u = universe.Universe.random_state()
        u.run()
    except Exception as e:
        print("Not able to run the simulation...", e)

if __name__ == "__main__":
    main()
    