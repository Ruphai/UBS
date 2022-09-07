#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scipy.optimize import brentq
from scipy.interpolate import interp1d

def eer(fpr, tpr):
    return brentq(lambda x : 1. - x - interp1d(fpr, tpr)(x), 0., 1.)
