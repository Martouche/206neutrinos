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
def my_calcul(tab, ma):
    total = tab[1] * tab[0]
    temp = (tab[3] * tab[3] + tab[1] * tab[1]) * tab[0]
    tab[0] = tab[0] + 1
    tab[1] = (total + ma) / tab[0]
    tab[3] = sqrt(((temp + pow(ma, 2)) / tab[0]) - pow(tab[1], 2))
    mean_square = sqrt((temp + pow(ma, 2)) / tab[0])
    tab.append(mean_square)
    tab[2] = tab[0] / ((1 / ma) + ((tab[0] - 1) / tab[2]))
    return tab

def print_funct(tab, mean_square):
    print ("\tNumber of values:\t%d" % tab[0])
    print ("\tStandard deviation:\t%.2f" % tab[3])
    print ("\tArithmetic mean:\t%.2f" % tab[1])
    print ("\tRoot mean square:\t%.2f" % mean_square)
    print ("\tHarmonic mean:\t%.2f\n" % tab[2])

def my_neutrinos(tab):
    while (True):
        input_value = input("Enter next value: ")
        ma = check_input(input_value)
        temp = (tab[3] * tab[3] + tab[1] * tab[1]) * tab[0]
        my_calcul(tab, ma)
        mean_square = sqrt((temp + pow(ma, 2)) / tab[0])
        print_funct(tab, mean_square)


def main():
    if (len(sys.argv) == 5):
        arg = error_handling()
        my_neutrinos(arg)
        print(arg)
    else:
        exit(84)
main()
