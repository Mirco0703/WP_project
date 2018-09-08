# -*- coding: utf-8 -*-
"""
Routines for solving the 1-d time-independant schrodinger equation

    solve_hamiltonian(para):
        interpolates the potential, writes the hamiltonian and solves it,
        returning eigenvalues and -vectors
    expectation_values(para, eigenvalues)
        using the by solve_hamiltonian() calculated eigenvectors to
        calculate the expectation value of the position operator and the
        position uncertainty
"""
import numpy as np
import scipy.interpolate
import scipy.linalg

def _interpolate_potential(para):
    x_points = para['interpolation_points_x']
    y_points = para['interpolation_points_y']
    xaxis = np.linspace(para['xMin'], para['xMax'], para['nPoints'])
    if para['interpolation_type'] == 'linear':
        interpolation_fun = scipy.interpolate.interp1d(x_points, y_points)
        potential = interpolation_fun(xaxis)
    elif para['interpolation_type'] == 'cspline':
        interpolation_fun = scipy.interpolate.CubicSpline(x_points, y_points)
        potential = interpolation_fun(xaxis)
    elif para['interpolation_type'] == 'polynomial':
        print('not yet implemented')
    return potential

def _write_hamiltonian(para):
    potential = _interpolate_potential(para)
    delta = np.abs(para['xMax']-para['xMin'])/para['nPoints']
    para['Delta'] = delta
    aa = 1/(para['mass']*delta**2)
    hamiltonian_diag = aa+potential
    hamiltonian_offdiag = -aa/2*np.ones(para['nPoints']-1)
    return hamiltonian_diag, hamiltonian_offdiag

def _norm_eigenvectors(eigenvectors, para):
    for ii in range(np.size(eigenvectors[0])):
        eigenvector_norm = para['Delta']*sum(np.abs(eigenvectors[1:-1, ii])**2)
        eigenvectors[:, ii] = eigenvectors[:, ii]/np.sqrt(eigenvector_norm)
    return eigenvectors

def expectation_values(para, eigenvectors):
    """
    Calculating expectation values of position operator and position
    uncertainty

        Args:
            para:dictionary, written by iomodul.read_schrodinger_inp(),
                 containing all relevant parameters
            eigenvectors: eigenvectors of the hamiltonian, given by
                          solve_hamiltonian()

        Returns:
            expval: array with the expectation values of the position operator
                    for each eigenvector
            uncertainty: corresponding position uncertainty
    """
    expval = np.zeros(np.size(eigenvectors[0]))
    expval_squared = np.zeros(np.size(eigenvectors[0]))
    uncertainty = np.zeros(np.size(eigenvectors[0]))
    delta = para['Delta']
    x_i = np.linspace(para['xMin']+delta, para['xMax']-delta, para['nPoints']-2)
    for ii in range(np.size(eigenvectors[0])):
        expval[ii] = delta*np.sum(eigenvectors[1:-1, ii]**2*x_i)
        expval_squared[ii] = delta*np.sum(eigenvectors[1:-1, ii]**2*x_i**2)
        uncertainty[ii] = np.sqrt(expval_squared[ii]-expval[ii]**2)
    return expval, uncertainty

def solve_hamiltonian(para):
    """
    Solves the 1-d SGL on interpolated potential

        Args:
            para: dictionary, written by iomodul.read_schrodinger_inp(),
                  containing all relevant parameters

        Returns:
            eigenvalues:  Array with the selected eigenvalues of the hamiltonian
            eigenvectors: linewise the corresponding, normed eigenvectors
    """
    hamiltonian_diag, hamiltonian_offdiag = _write_hamiltonian(para)
    eigenvalues, eigenvectors = scipy.linalg.eigh_tridiagonal(hamiltonian_diag, hamiltonian_offdiag, False, 'v', (para['first_eigenvalue']-1, para['last_eigenvalue']))
    eigenvectors = _norm_eigenvectors(eigenvectors, para)
    return eigenvalues, eigenvectors
