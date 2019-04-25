#!/usr/bin/env python3

import sys, os, math
from sys import stdin
from math import factorial, sqrt, exp, pi

def print_help():
    print("USAGE")
    print("\t./206neutrinos n a h sd\n")
    print("DESCRIPTION")
    print("\tn number of values")
    print("\ta arithmetic mean")
    print("\th harmonic mean")
    print("\tsd standard deviation")

def error_handling():
    tab = []
    i = 1
    try:
        while (i < len(sys.argv)):
            tab.append(int(sys.argv[i]))
            if (tab[i-1] < 0):
                sys.exit(84)
            i += 1
    except:
        print_help()
        exit(84)
    return tab

def check_input(input):
    if input == "END":
        exit(0)
    try:
        ma = float(input)
        if ma < 0:
            exit(84)
    except:
        exit(84)
    return ma

#nb_val, a, h, sd
def my_neutrinos(tab):
    while (True):
        input_value = input("Enter next value: ")
        ma = check_input(input_value)
        print(ma)
        total = tab[1] * tab[0]
        temp = (tab[3] * tab[3] + tab[1] * tab[1]) * tab[0]
        print(temp)
        tab[0] = tab[0] + 1
        tab[1] = (total + ma) / tab[0]
#        sd = sqrt(((temp + pow(ma, 2)) / nb_val) - pow(a, 2))
#        kvadratisk = sqrt((temp + pow(ma, 2)) / nb_val)
#        h = nb_val / ((1 / ma) + ((nb_val - 1) / h))
#        print ("\tantal malinder :\t%d" % nb_val)
#        print ("\tstandardafvilgelse :\t%.2f" % sd)
#        print ("\taritmetisk gennemsnit :\t%.2f" % a)
#        print ("\tkvadratisk gennemsnit :\t%.2f" % kvadratisk)
#        print ("\tharmonisk gennemsnit :\t%.2f\n" % h)

def main():
    if (len(sys.argv) == 5):
        arg = error_handling()
        my_neutrinos(arg)
        print(arg)
    else:
        exit(84)
main()
