"""
Simple Flask server to return predictions from trained densenet_web model
"""

from flask import Flask, request, redirect, flash
import torch
from torchvision.transforms.functional import to_tensor
from PIL import Image

from model import densenet121

app = Flask(__name__)
cp = torch.load('models/densenet_web/checkpoint/best_model.pth.tar')
net = densenet121()
net.load_state_dict(cp['net'])
net.eval()


def classify_image(x):
    """
    :param x: image
    :return: class prediction from densenet_web model
    """
    outputs = net(x)
    _, predicted = outputs.max(1)
    return predicted


@app.route('/predict', methods=['POST'])
def predict():
    """
    :return: prediction for image from POST request.
    """
    if request.method == 'POST':
        if 'img' not in request.files:
            flash('No image in request')
            return redirect(request.url)

        # preprocess image
        img = request.files['img']
        img = Image.open(img).convert("RGB")
        x = to_tensor(img)

        prediction = classify_image(x.unsqueeze(0))
        return str(int(prediction[0].data))
