import scipy.stats
import numpy as np
from sympy import *


def rarity(cdfMatrix):
    if cdfMatrix <= 0.35:
        if cdfMatrix <= 0.05:
            print("SSR")
        elif 0.15 >= cdfMatrix > 0.05:
            print("SR")
        elif 0.35 >= cdfMatrix > 0.15:
            print("R")
    else:
        print("N")
