# -*- coding: utf-8 -*-

import numpy as np
import scipy.interpolate
import scipy.linalg

def _interpolate_potential(para):
    if para['interpolation_type']=='linear':
        interpolation_fun = scipy.interpolate.interp1d(para['interpolation_points_x'], para['interpolation_points_y'])
        xaxis=np.linspace(para['xMin'],para['xMax'],para['nPoints'])
        potential=interpolation_fun(xaxis)
    elif para['interpolation_type']=='cspline':
        interpolation_fun = scipy.interpolate.CubicSpline(para['interpolation_points_x'], para['interpolation_points_y'])
        xaxis=np.linspace(para['xMin'],para['xMax'],para['nPoints'])
        potential=interpolation_fun(xaxis)
    elif para['interpolation_type']=='polynomial':
        print('not yet implemented')
    return potential

def _write_hamiltonian(para):
    potential=_interpolate_potential(para)
    Delta=np.abs(para['xMax']-para['xMin'])/para['nPoints']
    a=1/(para['mass']*Delta**2)
    hamiltonian_diag=a+potential
    hamiltonian_offdiag=-a/2*np.ones(para['nPoints']-1)
    return hamiltonian_diag,hamiltonian_offdiag

def solve_hamiltonian(para):
    [hamiltonian_diag, hamiltonian_offdiag] =_write_hamiltonian(para)
    eigenvalues, eigenvectors=scipy.linalg.eigh_tridiagonal(hamiltonian_diag, hamiltonian_offdiag,False,'v',(para['first_eigenvalue'],para['last_eigenvalue']))
    return eigenvalues, eigenvectors