## why se_resnext101_32x4d

ResNeXt-101 (64×4d): By making C=64 (i.e. 64 convolution paths within the ResNeXt block),
an even better improvement is already obtained with 20.4% top-1 and 5.3% top-5 error rates.
This means cardinality is essential to improve the classification accuracy

[link](https://towardsdatascience.com/review-resnext-1st-runner-up-of-ilsvrc-2016-image-classification-15d7f17b42ac)

## resnext vs resnet

A ResNeXt repeats a building block that aggregates a set of transformations with the same topology. 
Compared to a ResNet, it exposes a new dimension, cardinality (the size of the set of transformations) , 
as an essential factor in addition to the dimensions of depth and width.

[link](https://paperswithcode.com/method/resnext)

## what is resnet

ResNet, short for Residual Networks is a classic neural network used as a backbone for many computer vision tasks.
This model was the winner of ImageNet challenge in 2015. The fundamental breakthrough with ResNet was it allowed us
to train extremely deep neural networks with 150+layers successfully.

[link](https://towardsdatascience.com/understanding-and-coding-a-resnet-in-keras-446d7ff84d33)

## what is resnet

Residual Network (ResNet) is one of the famous deep learning models that was introduced by Shaoqing Ren,
Kaiming He, Jian Sun, and Xiangyu Zhang in their paper. The paper was named “Deep Residual Learning for 
Image Recognition” in 2015.

[link](https://www.analyticsvidhya.com/blog/2021/06/build-resnet-from-scratch-with-python/)

## layers in resnet

Each ResNet block is either two layers deep (used in small networks like ResNet 18, 34) or 
3 layers deep (ResNet 50, 101, 152).

[link](https://neurohive.io/en/popular-networks/resnet/)

## what is residual network

A residual neural network (ResNet)[1] is an artificial neural network (ANN). It is a gateless or open-gated 
variant of the HighwayNet,[2] the first working very deep feedforward neural network with hundreds of layers,
much deeper than previous neural networks. Skip connections or shortcuts are used to jump over some layers
(HighwayNets may also learn the skip weights themselves through an additional weight matrix for their gates). 
Typical ResNet models are implemented with double- or triple- layer skips that contain nonlinearities (ReLU)
and batch normalization in between. Models with several parallel skips are referred to as DenseNets.[3] 
In the context of residual neural networks, a non-residual network may be described as a plain network.

[link](https://en.wikipedia.org/wiki/Residual_neural_network)

## paper ref: Deep Residual Learning for Image Recognition

Deeper neural networks are more difficult to train. We present a residual learning framework to ease 
the training of networks that are substantially deeper than those used previously. 
We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, 
instead of learning unreferenced functions. We provide comprehensive empirical evidence showing that these 
residual networks are easier to optimize, and can gain accuracy from considerably increased depth. 
On the ImageNet dataset we evaluate residual nets with a depth of up to 152 layers---8x deeper than VGG nets 
but still having lower complexity. An ensemble of these residual nets achieves 3.57% error on the ImageNet 
test set. This result won the 1st place on the ILSVRC 2015 classification task. We also present analysis on 
CIFAR-10 with 100 and 1000 layers.

[link](https://arxiv.org/abs/1512.03385)




