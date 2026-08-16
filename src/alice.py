"""
Alice's operations in the BB84 protocol.
"""
from qiskit import QuantumCircuit
import numpy as np

class Alice:
    def __init__(self, bits: np.ndarray, bases: np.ndarray):
        """
        Initialize Alice with her generated bits and chosen bases.
        bits: array of 0s and 1s
        bases: array of 0s (Z basis) and 1s (X basis)
        """
        if len(bits) != len(bases):
            raise ValueError("Length of bits and bases must be equal.")
        self.bits = bits
        self.bases = bases
        self.num_qubits = len(bits)

    def prepare_states(self) -> list:
        """
        Prepare a list of quantum circuits representing Alice's states.
        For each qubit i:
        - If bit is 1, apply X gate (flips to |1>).
        - If basis is 1 (X basis), apply H gate (transforms to |+> or |->).
        Returns a list of QuantumCircuits.
        """
        circuits = []
        
        for i in range(self.num_qubits):
            qc = QuantumCircuit(1, 1)
            # Encode bit
            if self.bits[i] == 1:
                qc.x(0)
            # Encode basis
            if self.bases[i] == 1:
                qc.h(0)
            circuits.append(qc)
                
        return circuits
