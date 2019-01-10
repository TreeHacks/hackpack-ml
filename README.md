# hackpack-ml

Make and deploy ML hacks in PyTorch.

Training and iterating on ML models during hackathons poses challenges due to the limited time of the event. 
We hope to make this process easier with a hackpack!

### Features

The goal of this hackpack is to make iterating on your models easy while also providing for quick integration into apps.

We include:
1. Jupyter notebooks for different types of tasks and prebuilt models:
    * Image classification (DenseNet)
    * Generative Adversarial Networks (DCGAN) *
    * Regression *
    * Variational Autoencoder *
    * Integrating datasets into PyTorch *
    
2. A Flask server per model to deploy as an API.

 \* = Work in progress
 
## Getting Started

This hackpack assumes some prior understanding of Python. Understanding of Deep Learning techniques is greatly beneficial but not required. If you are interested in learning, [Deep Learning by Goodfellow et al.](https://www.deeplearningbook.org/) is a good starting point.
### Installing
```
!pip3 install torchvision
```
## Deployment
### Google Colab
