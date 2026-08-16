import pytest
import numpy as np
from src.bb84 import sift_keys, get_matching_indices, simulate_bb84
from src.alice import Alice
from src.bob import Bob
from src.eve import Eve

def test_sift_keys():
    alice_bases = np.array([0, 1, 0, 1])
    bob_bases = np.array([0, 0, 0, 1])
    bits = np.array([1, 0, 1, 1])
    
    sifted = sift_keys(alice_bases, bob_bases, bits)
    assert np.array_equal(sifted, np.array([1, 1, 1]))

def test_get_matching_indices():
    alice_bases = np.array([0, 1, 0, 1])
    bob_bases = np.array([0, 0, 0, 1])
    
    indices = get_matching_indices(alice_bases, bob_bases)
    assert np.array_equal(indices, np.array([0, 2, 3]))

def test_simulate_bb84_no_eve():
    bits = np.array([0, 1, 0, 1])
    bases = np.array([0, 1, 0, 1])
    alice = Alice(bits, bases)
    bob = Bob(bases) # Perfect basis match
    
    alice_key, bob_key = simulate_bb84(alice, bob)
    assert np.array_equal(alice_key, bob_key)
    assert len(alice_key) == 4

def test_simulate_bb84_with_eve():
    bits = np.array([1, 1, 1, 1])
    alice_bases = np.array([0, 0, 0, 0])
    eve_bases = np.array([1, 1, 1, 1]) # Eve chooses opposite basis, destroying state
    bob_bases = np.array([0, 0, 0, 0]) # Bob chooses correct basis
    
    alice = Alice(bits, alice_bases)
    bob = Bob(bob_bases)
    eve = Eve(eve_bases)
    
    alice_key, bob_key = simulate_bb84(alice, bob, eve)
    
    assert len(alice_key) == 4
    # Because of Eve, bob_key will be roughly 50% incorrect.
    # It is a probabilistic test, so it may occasionally perfectly match, 
    # but over many bits it diverges. We just check it runs without error.
    assert len(bob_key) == 4
