# -*- coding: utf-8 -*-

import numpy as np
import scipy.interpolate
import scipy.linalg
import scipy.integrate

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
    para['Delta']=Delta
    a=1/(para['mass']*Delta**2)
    hamiltonian_diag=a+potential
    hamiltonian_offdiag=-a/2*np.ones(para['nPoints']-1)
    return hamiltonian_diag,hamiltonian_offdiag

def _norm_eigenvectors(eigenvectors,para):
    for ii in range(np.size(eigenvectors[0])):
        eigenvector_norm = para['Delta']*sum(np.abs(eigenvectors[:,ii])**2)
        print(eigenvector_norm)
        eigenvectors[:,ii] = eigenvectors[:,ii]/np.sqrt(eigenvector_norm)
    return eigenvectors

def expectation_values(para,eigenvectors):
    expval_position_operator=np.zeros(np.size(eigenvectors[0]))
    for ii in range(np.size(eigenvectors[0])):
        expval_position_operator[ii]=para['Delta']*np.sum(eigenvectors[:,ii]**2*np.linspace(para['xMin'],para['xMax'],para['nPoints']))
    print(expval_position_operator)
    return expval_position_operator

def solve_hamiltonian(para):
    print(para['first_eigenvalue'])
    print(para['last_eigenvalue'])
    hamiltonian_diag, hamiltonian_offdiag =_write_hamiltonian(para)
    eigenvalues, eigenvectors=scipy.linalg.eigh_tridiagonal(hamiltonian_diag, hamiltonian_offdiag,False,'v',(para['first_eigenvalue']-1,para['last_eigenvalue']))
    eigenvectors = _norm_eigenvectors(eigenvectors,para)
    eigenvectors = _norm_eigenvectors(eigenvectors,para)
    
    return eigenvalues, eigenvectors