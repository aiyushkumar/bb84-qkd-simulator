"""
Main orchestration of the BB84 protocol.
"""
from qiskit_aer import AerSimulator
from qiskit import transpile
import numpy as np
from src.alice import Alice
from src.bob import Bob
from src.eve import Eve

def execute_circuit(circuits: list) -> str:
    """
    Executes a list of single-qubit QuantumCircuits and returns the measurement bitstring.
    We use AerSimulator(method='aer_simulator') to simulate a single transmission.
    By executing independent single-qubit circuits, we avoid Qiskit's multi-qubit coupling map limits.
    """
    simulator = AerSimulator()
    compiled_circuits = transpile(circuits, simulator)
    
    # Run all circuits in one batch job for efficiency
    job = simulator.run(compiled_circuits, shots=1)
    result = job.result()
    
    # Concatenate the single bit from each circuit
    measured_str = ""
    for i in range(len(circuits)):
        counts = result.get_counts(i)
        # the key is like '0' or '1'
        measured_str += list(counts.keys())[0]
        
    return measured_str

def sift_keys(alice_bases: np.ndarray, bob_bases: np.ndarray, bits: np.ndarray) -> np.ndarray:
    """
    Compare Alice and Bob's bases. Keep only the bits where the bases match.
    """
    matching_bases = alice_bases == bob_bases
    return bits[matching_bases]

def get_matching_indices(alice_bases: np.ndarray, bob_bases: np.ndarray) -> np.ndarray:
    """
    Return the indices where Alice and Bob used the same bases.
    """
    return np.where(alice_bases == bob_bases)[0]

def simulate_bb84(alice: Alice, bob: Bob, eve: Eve = None):
    """
    Run the full BB84 simulation.
    Returns:
        alice_key: Sifted key for Alice
        bob_key: Sifted key for Bob
    """
    # 1. Alice prepares her qubits
    alice_qc = alice.prepare_states()
    
    if eve is not None:
        # 2a. Eve intercepts and measures
        eve_qc = eve.intercept_and_measure(alice_qc)
        eve_result = execute_circuit(eve_qc)
        eve.set_measurements(eve_result)
        
        # 2b. Eve prepares new states based on her measurements and sends to Bob
        transmitted_qc = eve.prepare_resent_states()
    else:
        # 2. No Eve, transmitted states are Alice's states
        transmitted_qc = alice_qc
        
    # 3. Bob measures the transmitted states
    bob_qc = bob.measure(transmitted_qc)
    bob_result = execute_circuit(bob_qc)
    bob.set_measurements(bob_result)
    
    # 4. Sifting
    matching_indices = get_matching_indices(alice.bases, bob.bases)
    
    alice_key = alice.bits[matching_indices]
    bob_key = bob.measurements[matching_indices]
    
    return alice_key, bob_key
