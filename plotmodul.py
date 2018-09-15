# -*- coding: utf-8 -*-
"""
Module for plotting the solution of 1D-SGL obtained by solve_sgl.py

@author: Mirco Hellwig, Joshua Schmidt
"""

import numpy as np
import matplotlib.pyplot as plt
import iomodul


def plot_sgl_solution(directory='.', scaling=1.0):
    """
    Plots the potential, eignvalues, wavefunctions, uncertainty and
    expecatation value of position operator

        Args:
            directory: directory with results of solve_sgl.py
            scaling: y-scaling for the wavefunction for beautiful plots

        Returns:
            fig_handle: handle for the figure, can be used for plt.show() or
                        savefig.fig_handle()
    """
    xaxis, potential = iomodul.read_potential(directory)
    eigenvalues = iomodul.read_eigenvalues(directory)
    eigenvectors = iomodul.read_eigenvectors(directory)[1]
    expval, uncertainty = iomodul.read_expectation_values(directory)
    fig_handle = plt.figure()
    plt.subplot(1, 2, 1)
    plt.plot(xaxis, potential, 'k')
    xmin = np.min(xaxis)*1.1
    xmax = np.max(xaxis)*1.1
    plt.hlines(eigenvalues, xmin, xmax, 'tab:grey')
    for ii in range(0, eigenvalues.size):
        plt.plot(xaxis, eigenvectors[:, ii] * scaling + eigenvalues[ii],
                 color=(ii % 2, 0, 1-ii % 2))
    plt.plot(expval, eigenvalues, 'gx')
    plt.xlim(xmin, xmax)
    plt.ylim(np.min(potential)-0.2, (np.max(eigenvalues)+scaling)*1.05)
    plt.title(r'Potential, eigenstates, $\langle x \rangle$')
    plt.xlabel('x [Bohr]')
    plt.ylabel('Energy [Hartree]')
    plt.subplot(1, 2, 2)
    xmin = 0
    xmax = np.max(uncertainty)*1.1
    plt.hlines(eigenvalues, xmin, xmax, 'tab:grey')
    plt.plot(uncertainty, eigenvalues, 'm+')
    plt.xlim(xmin, xmax)
    plt.ylim(np.min(potential)-0.1, (np.max(eigenvalues)+scaling)*1.05)
    plt.title(r'$\sigma_x$')
    plt.xlabel('[Bohr]')
    plt.gca().axes.get_yaxis().set_visible(False)
    return fig_handle


def print_plot(location='screen', directory='.', fig_handle=None):
    """
    Prints any given plot either to the screen (default) or in a .pdf file

        Args:
            location: 'screen' or 'pdf'
            directory: for the .pdf file
            fig_handle: handle of figure to print
    """
    if location == 'screen':
        plt.show()
    elif location == 'pdf':
        fig_handle.savefig(directory+'plot.pdf', bbox_inches='tight')
