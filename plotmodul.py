# -*- coding: utf-8 -*-

import iomodul
import matplotlib.pyplot as plt
import numpy as np

def plot_sgl_solution(directory='.', scaling=1.0):
    xaxis, potential = iomodul.read_potential(directory)
    eigenvalues = iomodul.read_eigenvalues(directory)
    eigenvectors = iomodul.read_eigenvectors(directory)[1]
    expval, uncertainty = iomodul.read_expectation_values(directory)
    
    plt.subplot(1, 2, 1)
    plt.plot(xaxis, potential, 'k')
    xmin = np.min(xaxis)*1.1
    xmax = np.max(xaxis)*1.1
    plt.hlines(eigenvalues, xmin, xmax, 'tab:grey')
    for ii in range(0,eigenvalues.size):
        plt.plot(xaxis, eigenvectors[:, ii]*scaling+ eigenvalues[ii], color=(ii%2, 0, 1-ii%2))
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
    plt.show()
    