from app import app 
from flask import request, jsonify, render_template

from app.models.lung_cancer import predict_lung_cancer
from app.models.pneumonia_detection import predict_pneumonia
from app.models.brain_tumor import predict_brain_tumor
from app.models.pancreas import predict_pancreas
from app.models.tb import predict_tb
from app.models.dental import predict_dental 
from app.models.skin import predict_skin 
from app.models.infection import predict_infection 

@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/api/predict/lung', methods=['POST'])
def handle_lung_prediction(): 

    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    image_bytes = file.read()
    result = predict_lung_cancer(image_bytes)

    if 'error' in result:
        return jsonify(result), 500 
    
    return jsonify(result), 200

@app.route('/api/predict/pneumonia', methods=['POST'])
def handle_pneumonia_prediction():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    image_bytes = file.read()
    result = predict_pneumonia(image_bytes) 
    
    if 'error' in result:
        return jsonify(result), 500
    return jsonify(result), 200

@app.route('/api/predict/brain', methods=['POST'])
def handle_brain_tumor_prediction():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    image_bytes = file.read()
    result = predict_brain_tumor(image_bytes) 
    
    if 'error' in result:
        return jsonify(result), 500
    return jsonify(result), 200

@app.route('/api/predict/pancreas', methods=['POST'])
def handle_pancreas_prediction():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    image_bytes = file.read()
    result = predict_pancreas(image_bytes) 
    
    if 'error' in result:
        return jsonify(result), 500
    return jsonify(result), 200

@app.route('/api/predict/tb', methods=['POST'])
def handle_tb_prediction():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    image_bytes = file.read()
    result = predict_tb(image_bytes) 
    
    if 'error' in result:
        return jsonify(result), 500
    return jsonify(result), 200

@app.route('/api/predict/dental', methods=['POST'])
def handle_dental_prediction():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    image_bytes = file.read()
    result = predict_dental(image_bytes) 
    
    if 'error' in result:
        return jsonify(result), 500
    return jsonify(result), 200

@app.route('/api/predict/skin', methods=['POST'])
def handle_skin_prediction():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    image_bytes = file.read()
    result = predict_skin(image_bytes) 
    
    if 'error' in result:
        return jsonify(result), 500
    return jsonify(result), 200

@app.route('/api/predict/infection', methods=['POST'])
def handle_infection_prediction():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    image_bytes = file.read()
    result = predict_infection(image_bytes) 
    
    if 'error' in result:
        return jsonify(result), 500
    return jsonify(result), 200

