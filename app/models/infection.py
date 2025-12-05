# app/models/infection.py
import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import io
import warnings
from collections import OrderedDict 


warnings.filterwarnings("ignore")

ID2LABEL = {0: 'infected', 1: 'noninfected'}
IMG_SIZE = 224
MEAN = [0.485, 0.456, 0.406]
STD = [0.229, 0.224, 0.225]

preprocess = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=MEAN, std=STD),
])


def load_custom_infection_model():
    print("--- Loading Infection Model (Custom ResNet50) ---")
    try:
        checkpoint = torch.load('models_store/infection_model.pt', map_location='cpu', weights_only=False)
        
        if 'model_state_dict' in checkpoint:
            state_dict = checkpoint['model_state_dict']
        else:
            state_dict = checkpoint

        new_state_dict = {}
        for k, v in state_dict.items():
            if k.startswith("backbone."):
                new_state_dict[k.replace("backbone.", "")] = v
            elif k.startswith("classifier."):
                new_state_dict[k.replace("classifier.", "fc.")] = v
            else:
                new_state_dict[k] = v

   
        model = models.resnet50(weights=None)
        
        model.fc = nn.Sequential(OrderedDict([
            ('0', nn.Dropout(0.4)),                     
            ('1', nn.Linear(2048, 512)),                
            ('2', nn.ReLU()),                          
            ('3', nn.BatchNorm1d(512)),                  
            ('4', nn.Dropout(0.4)),                     
            ('5', nn.Linear(512, 256)),                  
            ('6', nn.ReLU()),                           
            ('7', nn.BatchNorm1d(256)),                  
            ('8', nn.Dropout(0.4)),                     
            ('9', nn.Linear(256, 2))                
        ]))

     
        model.load_state_dict(new_state_dict)
        print("--- Success! Infection Model Fully Loaded ---")
        return model

    except Exception as e:
        print(f"!!! Critical Error loading Infection model: {e} !!!")
        return None


model = load_custom_infection_model()
if model:
    model.eval()

def predict_infection(image_bytes):
    if model is None:
        return {'error': "Infection Model failed to load."}

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