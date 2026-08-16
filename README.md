# BB84 Quantum Key Distribution Simulator

An educational but technically rigorous simulator of the **BB84 Quantum Key Distribution (QKD)** protocol, written in Python using [Qiskit](https://qiskit.org/) and [Streamlit](https://streamlit.io/).

This project models the quantum state preparation, transmission, measurement, and classical sifting process of BB84. It demonstrates the effects of a potential eavesdropper (Eve) executing an **intercept-resend attack**, statistically revealing her presence via the Quantum Bit Error Rate (QBER).

## Live Demo
Live Demo: To be deployed on Streamlit Community Cloud. 
The application entry point for deployment is `app.py`.

## Features
- **Alice**: Random bit generation, basis selection, and quantum state preparation.
- **Bob**: Random basis selection and measurement.
- **Eve**: Intercept-resend attack simulation.
- **Protocol Sifting**: Basis comparison and key generation.
- **QBER Analysis**: Calculation of the Quantum Bit Error Rate.
- **Interactive Dashboard**: A Streamlit web UI to control parameters (qubit count, Eve's presence, QBER thresholds) and visualize the quantum pipeline.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bb84-quantum-key-distribution.git
   cd bb84-quantum-key-distribution
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

## Usage

### Run the Dashboard
To launch the interactive simulator dashboard:
```bash
streamlit run app.py
```

### Run the Tests
To verify the core implementation and run the test suite:
```bash
pytest tests/
```

## Documentation
- [Theory](docs/theory.md): The mathematics and quantum principles behind BB84.
- [Architecture](docs/architecture.md): The software design and modular breakdown.
- [Experiments](docs/experiments.md): Statistical analysis of Eve's impact on QBER.

## Disclaimer
This is a **simulator** for educational and demonstration purposes. It does not provide real cryptographic security and runs on classical hardware simulating quantum circuits via `qiskit-aer`.

## License
[MIT License](LICENSE)
