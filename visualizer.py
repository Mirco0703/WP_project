#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plots the results of 1D-SGL, and prints it either in file or on screen

@author: Mirco Hellwig, Joshua Schmidt
"""

import argparse
import plotmodul


def main():
    """
    Parses command line arguments (directory, scaling, print to screen/pdf),
    plots with those parameters and prints it
    """
    parser = argparse.ArgumentParser(description=__doc__)
    msg = 'Directory (default: .)'
    parser.add_argument('-d', '--directory', default='.', help=msg)
    msg = 'Scaling of eigenvectors (default: 1.0)'
    parser.add_argument('-s', '--scaling', default=1.0, help=msg)
    msg = 'Print to "screen" or "pdf" (default: ''screen'')'
    parser.add_argument('-p', '--printto', default='screen', help=msg)
    args = parser.parse_args()
    if args.directory[-1] != '/':    # users like us tend to forget the last /
        args.directory += '/'
    fig_handle = plotmodul.plot_sgl_solution(args.directory,
                                             float(args.scaling))
    plotmodul.print_plot(args.printto, args.directory, fig_handle)


if __name__ == '__main__':
    main()
