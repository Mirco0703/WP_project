# -*- coding: utf-8 -*-

import numpy as np
import iomodul
import sgl



def main():
    para=iomodul.read_schrodinger_inp()
    eigenvalues, eigenvectors=sgl.solve_hamiltonian(para)
    sgl.expectation_values(para,eigenvectors)
if __name__ == '__main__':
    main()
    