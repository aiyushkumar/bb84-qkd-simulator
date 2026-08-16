import pytest
import numpy as np
from src.qber import calculate_qber, detect_eavesdropper

def test_calculate_qber_no_errors():
    alice_key = np.array([1, 0, 1, 1])
    bob_key = np.array([1, 0, 1, 1])
    qber = calculate_qber(alice_key, bob_key)
    assert qber == 0.0

def test_calculate_qber_with_errors():
    alice_key = np.array([1, 0, 1, 1])
    bob_key = np.array([1, 1, 1, 0])
    qber = calculate_qber(alice_key, bob_key)
    assert qber == 0.5 # 2 out of 4 mismatch

def test_calculate_qber_empty():
    alice_key = np.array([])
    bob_key = np.array([])
    qber = calculate_qber(alice_key, bob_key)
    assert qber == 0.0

def test_detect_eavesdropper():
    assert detect_eavesdropper(0.0) == False
    assert detect_eavesdropper(0.05, threshold=0.11) == False
    assert detect_eavesdropper(0.25, threshold=0.11) == True
