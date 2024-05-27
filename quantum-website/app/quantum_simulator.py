import numpy as np
from qiskit import QuantumCircuit, transpile, Aer
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, circuit_drawer
from random import choice
from typing import List, Dict
import matplotlib.pyplot as plt
import tkinter as tk
from io import BytesIO
import base64
import numpy as np
from qiskit import QuantumCircuit, transpile, Aer
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, circuit_drawer
from random import choice
from typing import List, Dict
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from flask import request

# Function to add a random single-qubit gate
def add_random_single_qubit_gate(qc: QuantumCircuit, qubit: int) -> None:
    gates = ['x', 'y', 'z', 'h', 's', 't']
    gate = choice(gates)
    if gate == 'x':
        qc.x(qubit)
    elif gate == 'y':
        qc.y(qubit)
    elif gate == 'z':
        qc.z(qubit)
    elif gate == 'h':
        qc.h(qubit)
    elif gate == 's':
        qc.s(qubit)
    elif gate == 't':
        qc.t(qubit)

# Function to add a random two-qubit gate
def add_random_two_qubit_gate(qc: QuantumCircuit, qubit1: int, qubit2: int) -> None:
    gates = ['cx', 'cz', 'swap']
    gate = choice(gates)
    if gate == 'cx':
        qc.cx(qubit1, qubit2)
    elif gate == 'cz':
        qc.cz(qubit1, qubit2)
    elif gate == 'swap':
        qc.swap(qubit1, qubit2)

# Function to create a random quantum circuit
from flask import request

# Function to create a random quantum circuit
def create_random_quantum_circuit(num_qubits: int, single_qubit_gates: List[str], two_qubit_gates: List[str]) -> QuantumCircuit:
    qc = QuantumCircuit(num_qubits, num_qubits)
    for qubit in range(num_qubits):
        for gate in single_qubit_gates:
            if gate == 'x':
                qc.x(qubit)
            elif gate == 'y':
                qc.y(qubit)
            elif gate == 'z':
                qc.z(qubit)
            elif gate == 'h':
                qc.h(qubit)
            elif gate == 's':
                qc.s(qubit)
            elif gate == 't':
                qc.t(qubit)
    qubit_pairs = [(i, j) for i in range(num_qubits) for j in range(i+1, num_qubits)]
    for qubit1, qubit2 in qubit_pairs:
        for gate in two_qubit_gates:
            if gate == 'cx':
                qc.cx(qubit1, qubit2)
            elif gate == 'cz':
                qc.cz(qubit1, qubit2)
            elif gate == 'swap':
                qc.swap(qubit1, qubit2)
    qc.measure(range(num_qubits), range(num_qubits))
    return qc
# Function to simulate measurements
def simulate_measurements(qc: QuantumCircuit, shots: int = 1024) -> Dict[str, int]:
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=shots)
    result = job.result()
    return result.get_counts(compiled_circuit)

# Main function to create the circuit, and simulate measurements
def main():
    num_qubits = 3
    qc = create_random_quantum_circuit(num_qubits)
    print("Quantum Circuit:")
    circuit_image = circuit_drawer(qc, output='mpl', style='clifford')
    counts = simulate_measurements(qc)
    print("\nMeasurement counts:")
    print(counts)
    histogram = plot_histogram(counts)
    plt.close()  # Close the matplotlib figure

    return circuit_image, counts, histogram

# Unit tests for gate functions
def test_add_random_single_qubit_gate():
    qc = QuantumCircuit(1)
    add_random_single_qubit_gate(qc, 0)
    assert qc

def test_add_random_two_qubit_gate():
    qc = QuantumCircuit(2)
    add_random_two_qubit_gate(qc, 0, 1)
    assert qc

# # Run the tests and main function
# if __name__ == "__main__":
#     test_add_random_single_qubit_gate()
#     test_add_random_two_qubit_gate()
#     main()



# ... (the rest of your quantum simulator code goes here)

def generate_images(num_qubits, single_qubit_gates, two_qubit_gates):
    root = tk.Tk()
    root.withdraw()  # Hide the Tkinter window

    qc = create_random_quantum_circuit(num_qubits, single_qubit_gates, two_qubit_gates)
    print("Quantum Circuit:")
    circuit_image = circuit_drawer(qc, output='mpl', style='clifford')
    counts = simulate_measurements(qc)
    print("\nMeasurement counts:")
    print(counts)
    histogram = plot_histogram(counts)

    # Convert circuit image to base64
    circuit_image_buf = BytesIO()
    circuit_image.figure.savefig(circuit_image_buf, format='png')
    circuit_image_data = base64.b64encode(circuit_image_buf.getbuffer()).decode('utf-8')

    # Convert histogram image to base64
    histogram_buf = BytesIO()
    histogram.figure.savefig(histogram_buf, format='png')
    histogram_data = base64.b64encode(histogram_buf.getbuffer()).decode('utf-8')

    plt.close('all')  # Close all Matplotlib figures
    root.destroy()  # Destroy the Tkinter window

    return circuit_image_data, counts, histogram_data

if __name__ == "__main__":
    generate_images()
