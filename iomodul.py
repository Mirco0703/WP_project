# -*- coding: utf-8 -*-
"""
Routines for reading and writing the necessary file in- and output.
"""
import numpy as np

def read_schrodinger_inp(directory='./iodata/infinite_well_pot/'):
    """Reading input file schrodinger.inp

    Args:
        directory: directory in which schrodinger.inp is
    Returns:
        para: parameters of schrodinger.inp in a beautiful dictionary
    """
    para = {}
    para['directory'] = directory
    fp = open(directory+'schrodinger.inp', 'r')
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
    para['interpolation_points_x'] = np.genfromtxt(directory+'schrodinger.inp', skip_header=5)[:, 0]
    para['interpolation_points_y'] = np.genfromtxt(directory+'schrodinger.inp', skip_header=5)[:, 1]
    return para


def write_potential(xpot, potential, para):
    data = np.array([xpot, potential]).T
    np.savetxt(para['directory']+'potential.dat', data)
    
def write_eigenvalues(eigenvalues, para):
    np.savetxt(para['directory']+'energies.dat', eigenvalues.T)
    
def write_eigenvectors(eigenvectors, xaxis, para):
    data = np.array([eigenvectors])
    print(data.shape)
    np.savetxt(para['directory']+'wavefuncs.dat', data)
