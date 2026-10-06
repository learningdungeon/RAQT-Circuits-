"""Protocol 1 (ANON): anonymous transmission of a classical bit."""

import numpy as np
from netsquid.qubits import qubitapi as qapi
from netsquid.qubits import operators as ops


def run_protocol1(d, noise_prob=0.0):
    ghz4 = np.zeros(16)
    ghz4[0] = ghz4[15] = 1 / np.sqrt(2)
    qubits = qapi.create_qubits(4)
    qapi.assign_qstate(qubits, ghz4)

    if noise_prob > 0:
        for q in qubits:
            qapi.depolarize(q, noise_prob)

    if d == 1:
        qapi.operate(qubits[2], ops.Z)

    for q in qubits:
        qapi.operate(q, ops.H)

    results = [qapi.measure(q)[0] for q in qubits]
    return sum(results) % 2


if __name__ == "__main__":
    print(run_protocol1(d=1))
