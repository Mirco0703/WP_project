# -*- coding: utf-8 -*-
"""
Functions for pytest, testing potential and energies for the 6 given examples

Reference files are in same folders as schrodinger.inp, energies for the infinite
potential well and the harmonic oczillator are analytically calculated, rest
checked numerical results, potential is analytic exakt for both wells, and the
oszillator, others are checked numerical results

@author: Mirco Hellwig, Joshua Schmidt
"""

import numpy as np
import pytest
import iomodul
import sgl


TESTNAMES = ['infinite_well_pot', 'finite_well_pot', 'harmonic_pot',
             'asym_pot', 'double_pot_lin', 'double_pot_cspline']


@pytest.mark.parametrize("testname", TESTNAMES)
def test_potential(testname):
    """Simple testing function for the potential V(x), the x are NOT checked.

        Args:
            testname: directory with schrodinger.inp and the reference files
    """
    print("\nTest potential")
    loc = './iodata/' + testname + '/'
    ref_pot = np.loadtxt(loc+'reference_potential.dat')[:, 1]
    para = iomodul.read_schrodinger_inp(loc)
    test_pot = sgl.interpolate_potential(para)
    assert np.all(ref_pot - test_pot < 1e-10)


@pytest.mark.parametrize("testname", TESTNAMES)
def test_eigenvalues(testname):
    """Simple testing function for the eigenvalues/energies, prints them if
    test failed

        Args:
            testname: directory with schrodinger.inp and the reference files
    """
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
