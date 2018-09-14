# -*- coding: utf-8 -*-
"""
Routines for reading and writing the necessary file in- and output.
"""
import numpy as np

def read_schrodinger_inp(directory='.'):
    """Reading input file schrodinger.inp

    Args:
        directory: directory in which schrodinger.inp is
    Returns:
        para: parameters of schrodinger.inp in a beautiful dictionary
    """
    para = {}
    para['directory'] = directory
    try:
        fp = open(directory+'schrodinger.inp', 'r')
    except OSError:
        print('Could not open file!')
        print('schrodinger.inp not found in given directory or no permission to read it given!')
        para = None
    else:
        para = {}
        para['directory'] = directory
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
    xaxis = np.reshape(xaxis, (xaxis.size, 1))
    data = np.hstack((xaxis, eigenvectors))
    np.savetxt(para['directory']+'wavefuncs.dat', data)

def write_expectation_values(expval, uncertainty, para):
    data = np.array([expval, uncertainty]).T
    np.savetxt(para['directory']+'expvalues.dat', data)

def read_potential(directory):
    data = np.loadtxt(directory+'potential.dat')
    xaxis = data[:, 0]
    potential = data[:, 1]
    return xaxis, potential

def read_eigenvalues(directory):
    eigenvalues = np.loadtxt(directory+'energies.dat')
    return eigenvalues

def read_eigenvectors(directory):
    data = np.loadtxt(directory+'wavefuncs.dat')
    xaxis = data[:, 0]
    eigenvectors = data[:, 1:]
    return xaxis, eigenvectors

def read_expectation_values(directory):
    data = np.loadtxt(directory+'expvalues.dat')
    expval = data[:, 0]
    uncertainty = data[:, 1]
    return expval, uncertainty
