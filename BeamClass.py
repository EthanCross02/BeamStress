"""
This file will be used to define the behavior of all beams. It will continue to be updated I am sure

At some point, the use of a material database would dramatically expand the functionality of the code
"""
from typing import Tuple

class Beam:
    def __init__(self, length: float, youngs_modulus: float, bulk_modulus: float, material: str=None, cross_section: Tuple[float, float]=None):
        if material is not None:
            self.material = material
        if cross_section is None:
            self.base = 5.0
            self.height = self.base
        else:
            self.base = cross_section[0]
            self.height = cross_section[1]

        self.length = length
        self.E = youngs_modulus     #name changed to engineering convention to help with typing efficiency
        self.G = bulk_modulus
