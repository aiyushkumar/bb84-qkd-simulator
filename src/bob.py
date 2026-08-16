"""
Bob's operations in the BB84 protocol.
"""
from qiskit import QuantumCircuit
import numpy as np

class Bob:
    def __init__(self, bases: np.ndarray):
        """
        Initialize Bob with his chosen measurement bases.
        bases: array of 0s (Z basis) and 1s (X basis)
        """
        self.bases = bases
        self.num_qubits = len(bases)
        self.measurements = None

    def measure(self, circuits: list) -> list:
        """
        Apply Bob's measurement bases to the list of quantum circuits.
        If basis is 1 (X basis), apply H gate before measuring.
        """
        for i in range(self.num_qubits):
            qc = circuits[i]
            if self.bases[i] == 1:
                qc.h(0)
            qc.measure(0, 0)
        return circuits

    def set_measurements(self, measurement_str: str):
        """
        Given a string of measurement results ('0101...'), 
        store it as an array of ints.
        The order of bits in the string corresponds to the order of circuits.
        """
        self.measurements = np.array([int(bit) for bit in measurement_str])
