"""
Utility functions for the BB84 simulator.
"""

import numpy as np

def generate_random_bits(num_bits: int, seed: int = None) -> np.ndarray:
    """Generate an array of random bits (0s and 1s)."""
    if seed is not None:
        np.random.seed(seed)
    return np.random.randint(2, size=num_bits)

def generate_random_bases(num_bases: int, seed: int = None) -> np.ndarray:
    """
    Generate an array of random bases.
    0 represents the Z basis (computational).
    1 represents the X basis (Hadamard).
    """
    if seed is not None:
        np.random.seed(seed)
    return np.random.randint(2, size=num_bases)
