###########################################

SGL Solver Version 1.0

by Mirco Hellwig and Jsohua Schmidt

##########################################

Solves the 1 dimensional stationary SGL on
an interpolated potential, and returns
energies, wavefunctions, expectation value
of the position operator and position
uncertainty.

##########################################

Input:

schrodinger.inp example:
    2.0	# mass
    -2.0 2.0 1999	# xMin xMax nPoint
    1 5	# first and last eigenvalue to print
    linear	# interpolation type
    2	# nr. of interpolation points and xy declarations
    -2.0 0.0
    2.0 0.0

Input file have to be in this form!!

#########################################

Usage:

* ./solve_sgl.py [-d DIRECTORY]
    solves the in DIRECTORY (default .)
    given problem

* ./visualizer.py [-d DIRECTORY] [-s SCALING] [-p PRINT]
    plots the solution obtained by
    solve_sgl.py in DIRECTORY, scales the
    wavefunctions by SCALING (default 1.0)
    and PRINTs it on 'screen' or in 'pdf'
    (default 'screen')

########################################

Returns:

* energies.dat: the in schrodinger.inp specified
                energy eigenvalues

* wavefuncs.dat: corresponding eigenvectors

* potential.dat: the interpolated potential,
                 3 different interpolation types
                 are currently supported:
                 * linear
                 * cspline (natural cubic splines)
                 * polynomial (polynomial fit)

* expvalues: linewise expectation values and
             uncertainty, corresponding to the
             eigenvaules/-vectors
