import pytest
import numpy as np
from qiskit import QuantumCircuit
from src.eve import Eve

def test_eve_initialization():
    bases = np.array([1, 0, 1])
    eve = Eve(bases)
    assert np.array_equal(eve.bases, bases)
    assert eve.num_qubits == 3

def test_eve_intercept_and_measure():
    bases = np.array([1, 0])
    eve = Eve(bases)
    circuits = [QuantumCircuit(1, 1), QuantumCircuit(1, 1)]
    modified_circuits = eve.intercept_and_measure(circuits)
    assert len(modified_circuits) == 2
    assert len(modified_circuits[0].data) > 0

def test_eve_prepare_resent_states():
    bases = np.array([0, 1])
    eve = Eve(bases)
    with pytest.raises(ValueError):
        eve.prepare_resent_states() # Needs measurements first
        
    eve.set_measurements("10") # q0=1, q1=0
    circuits = eve.prepare_resent_states()
    assert len(circuits) == 2
    assert len(circuits[0].data) > 0
