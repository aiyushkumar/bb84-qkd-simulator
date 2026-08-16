# BB84 Quantum Key Distribution Simulator

An educational but technically rigorous simulator of the **BB84 Quantum Key Distribution (QKD)** protocol, written in Python using [Qiskit](https://qiskit.org/) and [Streamlit](https://streamlit.io/).

This project models the quantum state preparation, transmission, measurement, and classical sifting process of BB84. It demonstrates the effects of a potential eavesdropper (Eve) executing an **intercept-resend attack**, statistically revealing her presence via the Quantum Bit Error Rate (QBER).

## 🚀 Live Demo

👉 *[Launch BB84 QKD Simulator](https://bb84-qkd.streamlit.app)*

Try the interactive BB84 Quantum Key Distribution simulator directly in your browser. No installation required.

## 🌟 Features
- **Alice**: Random bit generation, basis selection, and quantum state preparation.
- **Bob**: Random basis selection and measurement.
- **Eve**: Intercept-resend attack simulation.
- **Protocol Sifting**: Basis comparison and key generation.
- **QBER Analysis**: Calculation of the Quantum Bit Error Rate.
- **Interactive Dashboard**: A Streamlit web UI to control parameters (qubit count, Eve's presence, QBER thresholds) and visualize the quantum pipeline.

## 🧠 How BB84 Works
The BB84 protocol ensures secure key exchange using the principles of quantum mechanics:
1. **Quantum State Preparation**: Alice encodes classical bits into quantum states (qubits) using one of two randomly chosen conjugate bases (e.g., Rectilinear or Diagonal).
2. **Transmission**: Alice sends these qubits to Bob over a quantum channel.
3. **Measurement**: Bob measures each incoming qubit using his own randomly chosen bases.
4. **Basis Reconciliation (Sifting)**: Alice and Bob publicly share the bases they used (but NOT the results). They keep only the bits where their bases matched, forming the "sifted key."

### Eve's Intercept-Resend Attack & QBER
If an eavesdropper (Eve) tries to measure the qubits in transit, quantum mechanics dictates she must guess a measurement basis. If she guesses wrong, she collapses and alters the qubit's state. When she resends the altered qubit to Bob, it introduces errors. Alice and Bob can detect this intrusion by comparing a subset of their sifted keys to calculate the **Quantum Bit Error Rate (QBER)**. A QBER significantly above 0% (approaching ~25% for a full intercept-resend attack) indicates Eve's presence, prompting Alice and Bob to discard the key.

## 🛠️ Technology Stack
- **Python 3.12**
- **Qiskit & Qiskit Aer**: For accurate quantum circuit simulation and statevector processing.
- **Streamlit**: For the interactive web application interface.
- **NumPy & Pandas**: For high-performance array operations and data structuring.
- **Matplotlib**: For statistical plotting and visualization.
- **Pytest**: For automated unit testing of quantum components.

## 📁 Project Structure
```text
bb84-quantum-key-distribution/
├── app.py                  # Main Streamlit application entry point
├── requirements.txt        # Python dependencies
├── src/                    # Core quantum implementation
│   ├── alice.py            # Alice's state preparation
│   ├── bob.py              # Bob's measurement logic
│   ├── eve.py              # Eve's intercept-resend attack
│   ├── bb84.py             # Protocol orchestration & simulation
│   ├── qber.py             # Error rate calculation
│   ├── experiments.py      # Statistical scaling experiments
│   └── utils.py            # Formatting helpers
├── tests/                  # Pytest automated test suite
└── docs/                   # Extended theoretical documentation
```

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aiyushkumar/bb84-qkd-simulator.git
   cd bb84-qkd-simulator
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Run the Dashboard Locally
To launch the interactive simulator dashboard on your own machine:
```bash
streamlit run app.py
```

### Run the Tests
To verify the core quantum implementation and run the automated test suite:
```bash
pytest tests/
```

## ⚠️ Limitations & Disclaimer
This project is an **educational simulator** designed for learning, demonstrations, and statistical analysis. It does not provide real cryptographic security and runs on classical hardware simulating quantum circuits via `qiskit-aer`. It is NOT a production-grade QKD system.

## 📜 License
[MIT License](LICENSE)
