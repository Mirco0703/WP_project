# -*- coding: utf-8 -*-

import iomodul
import sgl
import numpy as np


def test_infinite_well_pot():
    """Simple testing function for the infinite well potential.
    Currently only checking for the y values."""
    print("\nTest infinite well potential")
    loc = './iodata/infinite_well_pot/'
    ref_pot = np.loadtxt(loc+'reference_potential.dat')[:, 1]
    para = iomodul.read_schrodinger_inp(loc)
    test_pot = sgl._interpolate_potential(para)
    assert np.all(ref_pot - test_pot < 1e-10)


def test_infinite_well_energies():
    """Simple testing function for the eigenvalues of
    the infinite well potential."""
    print('\nTest infinite well potential eigenvalues')
    loc = './iodata/infinite_well_pot/'
    ref_energies = np.loadtxt(loc+'reference_energies.dat')
    para = iomodul.read_schrodinger_inp(loc)
    test_energies = sgl.solve_hamiltonian(para)[0]
    _check_result(ref_energies, test_energies)  # probably not needed
    assert np.all(ref_energies - test_energies < 1e-10)


def _check_result(expected, obtained):
    """Checks results by printing expected and obtained one."""
    print('Expected:', expected)
    print('Obtained:', obtained)
