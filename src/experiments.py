"""
Experiment runners for demonstrating the effects of the intercept-resend attack.
"""
from src.utils import generate_random_bits, generate_random_bases
from src.alice import Alice
from src.bob import Bob
from src.eve import Eve
from src.bb84 import simulate_bb84
from src.qber import calculate_qber

def run_experiment(num_qubits: int, with_eve: bool, seed: int = None):
    """
    Run a single BB84 experiment with a specified number of qubits.
    Returns a dictionary of metrics.
    """
    alice_bits = generate_random_bits(num_qubits, seed=seed)
    alice_bases = generate_random_bases(num_qubits, seed=seed + 1 if seed is not None else None)
    bob_bases = generate_random_bases(num_qubits, seed=seed + 2 if seed is not None else None)
    
    alice = Alice(alice_bits, alice_bases)
    bob = Bob(bob_bases)
    
    if with_eve:
        eve_bases = generate_random_bases(num_qubits, seed=seed + 3 if seed is not None else None)
        eve = Eve(eve_bases)
    else:
        eve = None
        
    alice_key, bob_key = simulate_bb84(alice, bob, eve)
    
    qber = calculate_qber(alice_key, bob_key)
    
    return {
        "num_qubits": num_qubits,
        "sifted_key_length": len(alice_key),
        "qber": qber,
        "alice_bits": alice_bits,
        "alice_bases": alice_bases,
        "bob_bases": bob_bases,
        "bob_measurements": bob.measurements,
        "eve_bases": eve.bases if eve else None,
        "eve_measurements": eve.measurements if eve else None,
        "alice_key": alice_key,
        "bob_key": bob_key
    }

def run_statistical_experiments(num_qubits_per_experiment: int, num_experiments: int, with_eve: bool):
    """
    Run multiple experiments to gather statistical data on QBER.
    """
    results = []
    for i in range(num_experiments):
        result = run_experiment(num_qubits_per_experiment, with_eve, seed=None) # True random for multiple exp
        results.append(result['qber'])
    return results
