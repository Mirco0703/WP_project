#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 12:51:42 2018

@author: mirco
"""

import argparse
import plotmodul
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(description='Plotting solution of 1-d SGL')
    msg = 'Directory (default: .)'
    parser.add_argument('-d', '--directory', default='.', help=msg)
    msg = 'Scaling of eigenvectors (default: 1.0)'
    parser.add_argument('-s', '--scaling', default=1.0, help=msg)
    args = parser.parse_args()
    plotmodul.plot_sgl_solution(args.directory, float(args.scaling))
    plt.show()

if __name__ == '__main__':
    main()
