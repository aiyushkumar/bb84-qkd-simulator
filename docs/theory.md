# BB84 Protocol Theory

The BB84 protocol was the first quantum cryptography protocol, proposed by Charles Bennett and Gilles Brassard in 1984. It relies on the properties of quantum mechanics to securely distribute a cryptographic key between two parties, traditionally named Alice and Bob.

## Core Concepts

1. **No-Cloning Theorem**: In quantum mechanics, it is impossible to create an identical copy of an arbitrary unknown quantum state. If Eve intercepts a qubit, she cannot copy it and send the original to Bob.
2. **Measurement Disturbance**: Measuring a quantum system in a basis other than the one it was prepared in alters its state. If Eve measures Alice's qubits in the wrong basis, she irreversibly changes them.

## The Protocol

1. **State Preparation (Alice)**: Alice generates a random bit (0 or 1) and chooses a random basis: the computational Z basis ($|0\rangle, |1\rangle$) or the Hadamard X basis ($|+\rangle, |-\rangle$). She encodes the bit into a qubit and sends it to Bob.
2. **Measurement (Bob)**: Bob receives the qubit and randomly chooses a basis (Z or X) to measure it.
3. **Sifting**: Over a public, authenticated classical channel, Alice and Bob announce the bases they used for each qubit. They discard any bits where they used different bases.
4. **Key Generation**: The remaining bits, where their bases matched, form the *sifted key*.

## Eavesdropping (The Intercept-Resend Attack)

If an eavesdropper (Eve) intercepts the qubits, she must measure them to gain information. Since she does not know Alice's bases, she must guess.
- 50% of the time, Eve guesses the correct basis. She gets the correct bit and resends a state identical to Alice's. Bob notices nothing.
- 50% of the time, Eve guesses the wrong basis. Her measurement yields a random result (50% 0, 50% 1), and the state she resends to Bob is now in Eve's basis.
  - When Bob measures this state in the correct (Alice's) basis, he now has a 50% chance of getting the wrong result due to Eve's disturbance.
  
Thus, for every bit where Eve guesses wrong (50% of the time), she introduces a 50% error rate for Bob. The overall Quantum Bit Error Rate (QBER) introduced by Eve is $0.5 \times 0.5 = 0.25$ or 25%.

By comparing a subset of their sifted key over the public channel, Alice and Bob can estimate the QBER. If it is significantly greater than 0 (e.g., approaches 25%), they abort the protocol.
