# -*- coding: utf-8 -*-
"""
Routines for reading and writing the necessary file in- and output.
"""
import numpy as np

def read_schrodinger_inp(folder='./iodata/finite_well_pot/'):
    """Reading input file schrodinger.inp

    Args:
        folder: folder in which schrodinger.inp is
    Returns:
        parameters of schrodinger.inp in a beautiful dictionary
    """
    para = {}
    fp = open(folder+'schrodinger.inp', 'r')
    string = fp.readline()
    para['mass'] = float(string.split()[0])
    string = fp.readline()
    para['xMin'] = float(string.split()[0])
    para['xMax'] = float(string.split()[1])
    para['nPoints'] = int(string.split()[2])
    string = fp.readline()
    para['first_eigenvalue'] = int(string.split()[0])
    para['last_eigenvalue'] = int(string.split()[1])
    string = fp.readline()
    para['interpolation_type'] = string.split()[0]
    string = fp.readline()
    para['interpolation_points_number'] = int(string.split()[0])
    para['interpolation_points_x'] = np.genfromtxt(folder+'schrodinger.inp', skip_header=5)[:, 0]
    para['interpolation_points_y'] = np.genfromtxt(folder+'schrodinger.inp', skip_header=5)[:, 1]
    return para


def write_pot_data(x, y, fname):
    data = np.array([x, y]).T
    np.savetxt(fname, data)
