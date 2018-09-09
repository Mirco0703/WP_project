# -*- coding: utf-8 -*-

import iomodul
import matplotlib.pyplot as plt

def plot_potential(directory):
    xaxis, potential = iomodul.read_potential(directory)
    plt.plot(xaxis, potential)
    plt.show()
    
