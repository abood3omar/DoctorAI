# app/models/dental.py

import torch
import torchvision.transforms as transforms
from PIL import Image
import io
import timm

ID2LABEL = {0: 'Cavity', 1: 'Fillings', 2: 'Impacted Tooth', 3: 'Implant'}
IMG_SIZE = 224
MEAN = [0.485, 0.456, 0.406]
STD = [0.229, 0.224, 0.225]

preprocess = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=MEAN, std=STD),
])

try:
    model = torch.jit.load('models_store/dental_model.pt')
    model.eval()
    print("--- Dental Model loaded successfully ---")
except Exception as e:
    print(f"!!! Error loading Dental model: {e} !!!")

def predict_dental(image_bytes):
    try:
        image = Image.open(io.BytesIO(image_bytes))
        if image.mode != 'RGB':
            image = image.convert('RGB')
            
        tensor = preprocess(image).unsqueeze(0)

        with torch.no_grad():
            outputs = model(tensor)
            _, predicted_idx_tensor = torch.max(outputs, 1)
            predicted_idx = predicted_idx_tensor.item()

        label = ID2LABEL.get(predicted_idx, "Unknown Class")
        return {'prediction': label, 'class_id': predicted_idx}
    
    except Exception as e:
        return {'error': f"Error during prediction: {str(e)}"}