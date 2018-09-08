# -*- coding: utf-8 -*-

import numpy as np
import scipy

def _interpolate_potential(para):
    potential = np.interp(np.linspace(para['xMin'], para['xMax'], para['nPoints']), para['interpolation_points_x'], para['interpolation_points_y'])
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
    test=scipy.linalg.eigh_tridiagonal(hamiltonian_diag, hamiltonian_offdiag)
    return test