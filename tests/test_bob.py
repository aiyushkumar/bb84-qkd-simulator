import pytest
import numpy as np
from qiskit import QuantumCircuit
from src.bob import Bob

def test_bob_initialization():
    bases = np.array([0, 1, 0, 1])
    bob = Bob(bases)
    assert np.array_equal(bob.bases, bases)
    assert bob.num_qubits == 4
    assert bob.measurements is None

def test_bob_measure():
    bases = np.array([0, 1])
    bob = Bob(bases)
    circuits = [QuantumCircuit(1, 1), QuantumCircuit(1, 1)]
    modified_circuits = bob.measure(circuits)
    
    assert len(modified_circuits) == 2
    assert modified_circuits[0].num_qubits == 1
    assert len(modified_circuits[0].data) > 0 # Measurements applied

def test_bob_set_measurements():
    bases = np.array([0, 1, 0, 1])
    bob = Bob(bases)
    bob.set_measurements("1010")
    assert np.array_equal(bob.measurements, np.array([1, 0, 1, 0]))
