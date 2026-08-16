# Simulator Architecture

The BB84 simulator is built using a modular, object-oriented architecture in Python, leveraging Qiskit for quantum circuit simulation and Streamlit for the user interface.

## Modules

### `src/alice.py`
Defines the `Alice` class. Alice is responsible for generating random bits and bases, and preparing the `qiskit.QuantumCircuit` that encodes these bits into quantum states.

### `src/bob.py`
Defines the `Bob` class. Bob receives a quantum circuit, applies his random measurement bases, and records the classical bit string resulting from the measurement.

### `src/eve.py`
Defines the `Eve` class. Eve implements the intercept-resend attack. She measures Alice's circuit, records the results, and dynamically prepares a new circuit to send to Bob based on her measurements.

### `src/bb84.py`
The orchestration engine. It defines:
- `execute_circuit`: Transpiles and runs the quantum circuit on the `qiskit-aer` AerSimulator.
- `sift_keys`: Compares bases and filters out mismatched indices to produce the final key.
- `simulate_bb84`: Ties Alice, Bob, and Eve together in the correct sequence.

### `src/qber.py`
Calculates the Quantum Bit Error Rate (QBER) by comparing Alice and Bob's sifted keys, and determines if the threshold has been breached.

### `src/experiments.py`
Provides wrapper functions (`run_experiment`, `run_statistical_experiments`) to easily execute the simulation loop multiple times for data aggregation.

## User Interface (`app.py`)
A Streamlit dashboard that visualizes the classical arrays, executes the simulation, calculates QBER, and plots statistical distributions.
