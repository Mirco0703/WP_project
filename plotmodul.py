# -*- coding: utf-8 -*-

import iomodul
import matplotlib.pyplot as plt
import numpy as np

def plot_sgl_solution(directory='.', scaling=1.0, xmin=-2.0, xmax=2.0):
    xaxis, potential = iomodul.read_potential(directory)
    eigenvalues = iomodul.read_eigenvalues(directory)
    xaxis, eigenvectors = iomodul.read_eigenvectors(directory)
    expval, uncertainty = iomodul.read_expectation_values(directory)   
    plt.subplot(1, 2, 1)
    plt.plot(xaxis, potential, 'k')
    plt.hlines(eigenvalues, xmin, xmax, 'tab:grey')
    for ii in range(0,eigenvalues.size):
        plt.plot(xaxis, eigenvectors[:, ii]*scaling+ eigenvalues[ii], color=(ii%2, 0, 1-ii%2))
    plt.plot(expval, eigenvalues, 'gx')
    
    plt.subplot(1, 2, 2)   
    plt.hlines(eigenvalues, 0, np.max(uncertainty)*1.2, 'tab:grey')
    plt.plot(uncertainty, eigenvalues, 'm+')
    plt.show()
    