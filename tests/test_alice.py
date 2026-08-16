import pytest
import numpy as np
from qiskit import QuantumCircuit
from src.alice import Alice

def test_alice_initialization():
    bits = np.array([0, 1, 0, 1])
    bases = np.array([0, 0, 1, 1])
    alice = Alice(bits, bases)
    
    assert np.array_equal(alice.bits, bits)
    assert np.array_equal(alice.bases, bases)
    assert alice.num_qubits == 4

def test_alice_invalid_initialization():
    bits = np.array([0, 1, 0])
    bases = np.array([0, 0, 1, 1])
    with pytest.raises(ValueError):
        Alice(bits, bases)

def test_alice_prepare_states():
    bits = np.array([0, 1, 0, 1])
    bases = np.array([0, 0, 1, 1])
    alice = Alice(bits, bases)
    circuits = alice.prepare_states()
    
    assert len(circuits) == 4
    for qc in circuits:
        assert isinstance(qc, QuantumCircuit)
        assert qc.num_qubits == 1
    # The circuit should have gates applied.
    assert len(circuits[1].data) > 0
