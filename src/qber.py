"""
Quantum Bit Error Rate (QBER) calculations.
"""
import numpy as np

def calculate_qber(alice_key: np.ndarray, bob_key: np.ndarray) -> float:
    """
    Calculate the Quantum Bit Error Rate (QBER) between Alice's and Bob's sifted keys.
    QBER = (Number of mismatched bits) / (Total number of bits in the sifted key)
    """
    if len(alice_key) == 0:
        return 0.0
    
    mismatches = np.sum(alice_key != bob_key)
    return mismatches / len(alice_key)

def detect_eavesdropper(qber: float, threshold: float = 0.11) -> bool:
    """
    Determine if an eavesdropper is present based on the QBER threshold.
    The theoretical threshold for security is typically 11% for standard BB84.
    If QBER > threshold, an eavesdropper is detected.
    """
    return qber > threshold
