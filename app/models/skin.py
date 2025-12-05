# app/models/skin.py
import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import io
import warnings
from collections import OrderedDict 


warnings.filterwarnings("ignore")

ID2LABEL = {0: 'akiec', 1: 'bcc', 2: 'bkl', 3: 'df', 4: 'mel', 5: 'nv', 6: 'vasc'}
IMG_SIZE = 224
MEAN = [0.485, 0.456, 0.406]
STD = [0.229, 0.224, 0.225]


preprocess = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=MEAN, std=STD),
])


def load_custom_resnet():
    print("--- Loading Skin Model (Final Structural Fix) ---")
    try:
        checkpoint = torch.load('models_store/skin_model.pt', map_location='cpu', weights_only=False)
        
        if 'model_state_dict' in checkpoint:
            state_dict = checkpoint['model_state_dict']
        else:
            state_dict = checkpoint

        clean_state_dict = {}
        for k, v in state_dict.items():
            clean_state_dict[k.replace("backbone.", "")] = v

        if 'fc.1.weight' in clean_state_dict:
            input_features = clean_state_dict['fc.1.weight'].shape[1] 
            hidden_features = clean_state_dict['fc.1.weight'].shape[0]
            num_classes = clean_state_dict['fc.5.weight'].shape[0]
            print(f"Detected Structure: In={input_features} -> Hidden={hidden_features} -> Out={num_classes}")
        else:
            raise Exception("Could not match layer keys (expected fc.1, fc.3, fc.5).")

        if input_features == 2048:
            model = models.resnet50(weights=None)
        elif input_features == 512:
            model = models.resnet18(weights=None)
        else:
             model = models.resnet50(weights=None)

  
        model.fc = nn.Sequential(OrderedDict([
            ('0', nn.Dropout(0.4)),                       
            ('1', nn.Linear(input_features, hidden_features)),
            ('2', nn.ReLU()),                             
            ('3', nn.BatchNorm1d(hidden_features)),       
            ('4', nn.Dropout(0.4)),                      
            ('5', nn.Linear(hidden_features, num_classes))    
        ]))
        
        model.load_state_dict(clean_state_dict)
        print("--- Success! Skin Model Fully Loaded ---")
        return model

    except Exception as e:
        print(f"!!! Critical Error loading Skin model: {e} !!!")
        return None


model = load_custom_resnet()
if model:
    model.eval()

def predict_skin(image_bytes):
    if model is None:
        return {'error': "Skin Model failed to load."}

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