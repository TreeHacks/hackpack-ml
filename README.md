# hackpack-ml

Make and deploy ML hacks in PyTorch.

### Features
This hackpack aims to make iterating on your models easy while also providing for quick integration into apps. 

We include:
 1. An introductory notebook in which we load our own dataset into PyTorch and build a simple neural network for regression on tabular data:
    `/models/dataset_nn/dataset_neural_nets.ipynb`
    
 2. An application-focused notebook in which we load and train a DenseNet model for image classification on MNIST and CIFAR10 datasets, 
    and then export the model into a Flask server as our own API:
    `/models/densenet_web/densenet.ipynb`
    
## Getting Started

This hackpack assumes some prior understanding of Python. Understanding of Deep Learning techniques is greatly beneficial but not required. If you are interested in learning, [Deep Learning by Goodfellow et al.](https://www.deeplearningbook.org/) is a good starting point.

### Google Colab

Both notebooks are also hosted on Google Colab, a free Jupyter notebook environment with GPU/TPU support. 
They are accessible at <a href='https://colab.research.google.com/drive/1JA1CDouBu2q8ivjWK8eMXaOJXR00-RaU'>dataset_neural_nets</a> and <a href='https://colab.research.google.com/drive/1KgxeCiC01kGk6b0hXiCQEKfphyDzoay5'>densenet_web</a> respectively. Feel free to open them in the playground environment or copy!
 
### Installing
If you wish to work on the notebooks locally, you can quickly spin up a environment 
```
!pip3 install torchvision
```
### License
MIT

# About HackPacks 🌲

HackPacks are built by the [TreeHacks](https://www.treehacks.com/) team to help hackers build great projects at our hackathon that happens every February at Stanford. We believe that everyone of every skill level can learn to make awesome things, and this is one way we help facilitate hacker culture. We open source our hackpacks (along with our internal tech) so everyone can learn from and use them! Feel free to use these at your own hackathons, workshops, and anything else that promotes building :) 

If you're interested in attending TreeHacks, you can apply on our [website](https://www.treehacks.com/) during the application period.

You can follow us here on [GitHub](https://github.com/treehacks) to see all the open source work we do (we love issues, contributions, and feedback of any kind!), and on [Facebook](https://facebook.com/treehacks), [Twitter](https://twitter.com/hackwithtrees), and [Instagram](https://instagram.com/hackwithtrees) to see general updates from TreeHacks. 
