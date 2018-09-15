# -*- coding: utf-8 -*-
"""
Routines for reading and writing the necessary file in- and output.

@author: Mirco Hellwig, Joshua Schmidt
"""

import numpy as np


def read_schrodinger_inp(directory='.'):
    """Reading input file schrodinger.inp

    Args:
        directory: directory in which schrodinger.inp is
    Returns:
        para: parameters of schrodinger.inp in a beautiful dictionary
    """
    try:
        fp = open(directory+'schrodinger.inp', 'r')
    except OSError:
        print('Could not open file!')
        print('No schrodinger.inp in directory or no permission to read it!')
        raise SystemExit
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
    para['interpolation_points_x'] = np.genfromtxt(directory+'schrodinger.inp',
                                                   skip_header=5)[:, 0]
    para['interpolation_points_y'] = np.genfromtxt(directory+'schrodinger.inp',
                                                   skip_header=5)[:, 1]
    return para


def write_potential(xaxis, potential, directory):
    """
    Writing potential in potential.dat

        Args:
            xaxis: x values
            potential: potential V(x)
            directory: directory for saving
    """
    data = np.array([xaxis, potential]).T
    np.savetxt(directory+'potential.dat', data)


def write_eigenvalues(eigenvalues, directory):
    """
    Writing eigenvalues in energies.dat

        Args:
            eigenvalues: energie eigenvalues to write
            directory: directory for saving
    """
    np.savetxt(directory+'energies.dat', eigenvalues.T)


def write_eigenvectors(eigenvectors, xaxis, directory):
    """
    Writing eigenvectors in wavefuncs.dat

        Args:
            eigenvectgors: eigenvectors to write
            directory: directory for saving
    """
    xaxis = np.reshape(xaxis, (xaxis.size, 1))
    data = np.hstack((xaxis, eigenvectors))
    np.savetxt(directory+'wavefuncs.dat', data)


def write_expectation_values(expval, uncertainty, directory):
    """
    Wrtiting expectation value und uncertainty in expvalues.dat

        Args:
            expval: expectation value of position operator
            uncertainty: position uncertainty
            directory: directory for saving
    """
    data = np.array([expval, uncertainty]).T
    np.savetxt(directory+'expvalues.dat', data)


def read_potential(directory):
    """
    Reads potential in directory + 'potential.dat'

        Args:
            directory: directory with file to be read

        Returns:
            xaxis: x values
            potential: potential V(x)
    """
    data = np.loadtxt(directory+'potential.dat')
    xaxis = data[:, 0]
    potential = data[:, 1]
    return xaxis, potential


def read_eigenvalues(directory):
    """
    Reads energies in directory + 'energies.dat'

        Args:
            directory: directory with file to be read

        Returns:
            eigenvalues: read energies
    """
    eigenvalues = np.loadtxt(directory+'energies.dat')
    return eigenvalues


def read_eigenvectors(directory):
    """
    Reads eigenvectors in directory + 'wavefuncs.dat'

        Args:
            directory: directory with file to be read

        Returns:
            xaxis: x values
            eigenvectors: matrix with all eigenvectors
    """
    data = np.loadtxt(directory+'wavefuncs.dat')
    xaxis = data[:, 0]
    eigenvectors = data[:, 1:]
    return xaxis, eigenvectors


def read_expectation_values(directory):
    """
    Reads expectation values and uncertainty in directory + 'expvalues.dat'

        Args:
            directory: directory with file to be read

        Returns:
            expval: expectation value of position operator
            uncertainty: position uncertainty
    """
    data = np.loadtxt(directory+'expvalues.dat')
    expval = data[:, 0]
    uncertainty = data[:, 1]
    return expval, uncertainty
