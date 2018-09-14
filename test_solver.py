# -*- coding: utf-8 -*-

import pytest
import iomodul
import sgl
import numpy as np

TESTNAMES = ['infinite_well_pot', 'finite_well_pot', 'harmonic_pot', 'asym_pot',
             'double_pot_lin', 'double_pot_cspline']

@pytest.mark.parametrize("testname", TESTNAMES)
def test_potential(testname):
    """Simple testing function for the potential.
    Currently only checking for the y values."""
    print("\nTest potential")
    loc = './iodata/' + testname + '/'
    ref_pot = np.loadtxt(loc+'reference_potential.dat')[:, 1]
    para = iomodul.read_schrodinger_inp(loc)
    test_pot = sgl._interpolate_potential(para)
    assert np.all(ref_pot - test_pot < 1e-10)

@pytest.mark.parametrize("testname", TESTNAMES)
def test_energies(testname):
    """Simple testing function for the eigenvalues of
    the infinite well potential."""
    print('\nTest eigenvalues')
    loc = './iodata/' + testname + '/'
    ref_energies = np.loadtxt(loc+'reference_energies.dat')
    para = iomodul.read_schrodinger_inp(loc)
    test_energies = sgl.solve_hamiltonian(para)[0]
    _check_result(ref_energies, test_energies)  # probably not needed
    assert np.all(ref_energies - test_energies < 1e-2)


def _check_result(expected, obtained):
    """Checks results by printing expected and obtained one."""
    print('Expected:', expected)
    print('Obtained:', obtained)
