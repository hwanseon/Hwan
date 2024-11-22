
import os
import torch
from torchvision import transforms
from PIL import Image
import torch.nn.functional as F


DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

MODEL_PATH = "./Hwan_Models/project/BCF/model_all.pth"

if os.path.exists(MODEL_PATH):
    model = torch.load(MODEL_PATH)
    model.to(DEVICE)
    model.eval()
else:
    print(f"Error: 모델을 찾을 수 없음 {MODEL_PATH}")

# Image preprocessing function
def preprocess_image(file_item):
    img = Image.open(file_item)
    
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    img_tensor = transform(img).unsqueeze(0) 
    return img_tensor.to(DEVICE)
