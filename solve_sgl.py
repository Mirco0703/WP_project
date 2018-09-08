#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import iomodul
import sgl




def main():
    parser = argparse.ArgumentParser(description='Solving 1-d SGL')
    msg = 'Directory (default: .)'
    parser.add_argument('-d', '--directory', default='.', help=msg)
    args = parser.parse_args()
    para = iomodul.read_schrodinger_inp(args.directory)
    eigenvalues, eigenvectors = sgl.solve_hamiltonian(para)
    sgl.expectation_values(para, eigenvectors)

if __name__ == '__main__':
    main()
    