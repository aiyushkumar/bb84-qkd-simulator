# Statistical Experiments and the Eve Attack

This simulator allows you to run large-scale automated experiments to demonstrate the statistical properties of the BB84 protocol under an intercept-resend attack.

## Experiment: No Eavesdropper

When running the simulation without Eve, Alice encodes her bits and Bob measures them.
For the bits where they coincidentally chose the same basis, Bob's measurement will perfectly align with Alice's preparation (assuming ideal quantum channels with no noise).

**Expected Outcome**:
- QBER (Quantum Bit Error Rate) should be exactly $0.0\%$.
- Any deviation from 0 in this simulator would indicate a bug, as we do not simulate environmental noise.

## Experiment: With Eavesdropper (Intercept-Resend)

Eve intercepts the qubits from Alice, measures them, and resends them to Bob. Since she cannot clone the states (No-Cloning Theorem), she must measure them in a randomly chosen basis.

If Eve's basis differs from Alice's (50% probability), Eve measures a random value and prepares a new state in her basis. When Bob measures this state in Alice's basis (to form the sifted key), he has a 50% probability of getting the wrong bit.

Therefore, the probability of an error in the sifted key is:
$P(\text{Eve wrong basis}) \times P(\text{Bob gets wrong result}) = 0.5 \times 0.5 = 0.25$

**Expected Outcome**:
- Over a large number of qubits, the QBER will converge to $25\%$.
- In the `experiments.py` module, you can run hundreds of trials. A histogram will clearly show the QBER distribution centering around $0.25$.

This 25% error rate is easily detectable by Alice and Bob if they compare a subset of their sifted keys over the public channel. If the error rate exceeds a certain threshold (typically around 11% for basic BB84), they conclude an eavesdropper is present and discard the key.
