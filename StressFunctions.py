"""
This will serve as a collection of all functions regarding material stress and strain
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def principal_stress(sig_11=0, sig_22=0, sig_33=0, t_12=0, t_13=0, t_23=0):
    stress_tensor = np.array([
        [sig_11, t_12, t_13],
        [t_12, sig_22, t_23],
        [t_13, t_23, sig_33],
        ])
    # print(np.linalg.eigvals(stress_tensor))
    return np.linalg.eigvals(stress_tensor)

def create_mohr(p1: float, p2: float):
    p_avg = np.average([p1, p2])
    radius = max(p1,p2)-p_avg
    circle = plt.Circle((p_avg,0), radius=radius, color='r', fill=False)
    return circle

def mohr():

    p = principal_stress(18, 23, -14, 0, 32, 6)

    pad = 10
    y_bounds: float = max(p)-np.average([min(p), max(p)]) + pad
    circle1 = create_mohr(p[0], p[1])
    circle2 = create_mohr(p[0], p[2])
    circle3 = create_mohr(p[1], p[2])
    fig, ax = plt.subplots(1)
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.add_patch(circle3)
    plt.xlim(min(p)-pad, max(p)+pad)
    plt.ylim(-y_bounds, y_bounds)
    plt.show()

if __name__ == '__main__':
    mohr()