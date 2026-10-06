"""GHZ-4 state preparation. Run on IBM Quantum or Aer."""

from qiskit import QuantumCircuit

qc = QuantumCircuit(4, 4)
qc.h(0)
qc.cx(0, 1)
qc.cx(0, 2)
qc.cx(0, 3)
qc.measure([0, 1, 2, 3], [0, 1, 2, 3])

print(qc)
# Expected: 0000 and 1111 only
