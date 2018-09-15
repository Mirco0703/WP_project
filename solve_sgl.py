#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solving the 1D SGL on interpolated potential

@author: Mirco Hellwig, Joshua Schmidt
"""

import argparse
import iomodul
import sgl


def main():
    """
    Parses command line arguments (directory) and then solves the in
    directory+'schrodinger.inp' given problem, and writes all results in the
    same directory
    """
    parser = argparse.ArgumentParser(description=__doc__)
    msg = 'Directory (default: .)'
    parser.add_argument('-d', '--directory', default='.', help=msg)
    args = parser.parse_args()
    if args.directory[-1] != '/':    # users like us tend to forget the last /
        args.directory += '/'
    para = iomodul.read_schrodinger_inp(args.directory)
    eigenvectors = sgl.solve_hamiltonian(para)[1]
    sgl.expectation_values(para, eigenvectors)


if __name__ == '__main__':
    main()
