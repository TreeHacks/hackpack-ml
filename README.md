# hackpack-ml

Make and deploy ML hacks in PyTorch

### Features
This hackpack aims to make iterating on your models easy while also providing for quick integration into apps. 

We include:
 1. An introductory notebook in which we load our own dataset into PyTorch and build a simple neural network for regression on tabular data:
    `/models/dataset_nn/dataset_neural_nets.ipynb`
    
 2. An application-focused notebook in which we load and train a DenseNet model for image classification on MNIST and CIFAR10 datasets, 
    and then export the model into a Flask server as our own API:
    `/models/densenet_web/densenet.ipynb`
 
## Getting Started
### Installing
You can quickly spin up a torch environment with the following command:
```
!pip3 install torchvision
```
## Deployment
### Google Colab
(work in progress)
