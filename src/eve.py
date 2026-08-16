"""
Eve's operations in the BB84 protocol.
Eve performs an intercept-resend attack.
"""
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

class Eve:
    def __init__(self, bases: np.ndarray):
        """
        Initialize Eve with her chosen measurement bases.
        """
        self.bases = bases
        self.num_qubits = len(bases)
        self.measurements = None

    def intercept_and_measure(self, circuits: list) -> list:
        """
        Eve intercepts the qubits from Alice, measures them in her random bases.
        Returns the modified circuits with measurements.
        """
        # Eve applies her basis transformations
        for i in range(self.num_qubits):
            qc = circuits[i]
            if self.bases[i] == 1:
                qc.h(0)
            qc.measure(0, 0)
        
        return circuits

    def prepare_resent_states(self) -> list:
        """
        Prepare the resent quantum states based on Eve's measurements.
        This is exactly like Alice's prepare_states, but using Eve's measurements
        and Eve's bases.
        Returns a list of QuantumCircuits.
        """
        if self.measurements is None:
            raise ValueError("Eve must measure before resending states.")
            
        circuits = []
        
        for i in range(self.num_qubits):
            qc = QuantumCircuit(1, 1)
            # Encode bit (Eve's measurement)
            if self.measurements[i] == 1:
                qc.x(0)
            # Encode basis (Eve's basis)
            if self.bases[i] == 1:
                qc.h(0)
            circuits.append(qc)
                
        return circuits

    def set_measurements(self, measurement_str: str):
        """
        Store Eve's measurement results from Qiskit execution.
        """
        self.measurements = np.array([int(bit) for bit in measurement_str])
