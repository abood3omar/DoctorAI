import torch
import torchvision.transforms as transforms
from PIL import Image
import io
import timm


ID2LABEL = {0: 'Normal', 1: 'glioma_tumor', 2: 'meningioma_tumor', 3: 'pituitary_tumor'}
IMG_SIZE = 224
MEAN = [0.485, 0.456, 0.406]
STD = [0.229, 0.224, 0.225]


preprocess = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=MEAN, std=STD),
])


try:
    model = torch.jit.load('models_store/brain_tumor_model.pt')
    model.eval()
    print("--- Brain Tumor Model loaded successfully ---")
except Exception as e:
    print(f"!!! Error loading Brain Tumor model: {e} !!!")


def predict_brain_tumor(image_bytes):
    """
    تأخذ الصورة كـ bytes وترجع النتيجة كـ dictionary
    """
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