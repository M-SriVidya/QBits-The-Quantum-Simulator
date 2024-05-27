from flask import render_template, Response, Flask, session, request, redirect, url_for
import numpy as np
from app import app
from io import BytesIO
import base64

@app.route('/')
def index():
    return render_template('index.html')

###############################################################################################
from .vis import launch_simulator  
from .quantum_simulator import generate_images ,main
##########################################################################################


#####################################################################################################################
# @app.route('/simulate')
# def simulate():
#     return render_template('simulate.html')
# @app.route('/simulate', methods=['GET', 'POST'])
# def simulate():
#     circuit_image, counts, histogram = main()

#     # Convert circuit image to base64 for rendering
#     circuit_image_buf = BytesIO()
#     circuit_image.figure.savefig(circuit_image_buf, format='png')
#     circuit_image_data = base64.b64encode(circuit_image_buf.getbuffer()).decode('utf-8')

#     # Convert histogram image to base64 for rendering
#     histogram_buf = BytesIO()
#     histogram.figure.savefig(histogram_buf, format='png')
#     histogram_data = base64.b64encode(histogram_buf.getbuffer()).decode('utf-8')

#     return render_template('simulate.html', circuit_image=circuit_image_data, counts=counts, histogram=histogram_data)
# @app.route('/simulate', methods=['GET', 'POST'])
# def simulate():
#     circuit_image, counts, histogram = generate_images()
#     return render_template('simulate.html', circuit_image=circuit_image, counts=counts, histogram=histogram)
@app.route('/simulate', methods=['GET', 'POST'])
def simulate():
    if request.method == 'POST':
        num_qubits = int(request.form.get('num_qubits', 3))
        single_qubit_gates = request.form.get('single_qubit_gates', 'x,y,z,h,s,t').split(',')
        two_qubit_gates = request.form.get('two_qubit_gates', 'cx,cz,swap').split(',')
        circuit_image, counts, histogram = generate_images(num_qubits, single_qubit_gates, two_qubit_gates)
        return render_template('simulate.html', circuit_image=circuit_image, counts=counts, histogram=histogram)
    return render_template('simulate.html')


@app.route('/visualize-algorithms')
def visualize_algorithms():
    launch_simulator()  # Call the launch_simulator function
    # html_content = run_simulator()
    return render_template('visualize-algorithms.html')
    # return Response(html_content, mimetype='text/html')


@app.route('/build-circuit')
def build_circuit():
    return render_template('build-circuit.html')

@app.route('/quantum-games')
def quantum_games():
    return render_template('quantum-games.html')

@app.route('/getting-started')
def getting_started():
    return render_template('getting-started.html')


