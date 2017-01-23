# NVIDIA Deep Learning Tutorial

TensorBoard is a UI tool to visualize training progress. Plots of loss, learning rate, accuracy; visualize computation graph.

Keras wraps Tensorflow or Theano. Code is easier to read.

Neural networks: feature extraction --> classification.

No information classifier can get high accuracy. If predicts everything to be 0 and only 2% of pixels are 1, then NN can achieve accuracy of >90%.

TFRecords data format is optimized for Tensorflow. Try not to use Numpy arrays (they will be slower).

Stochastic gradient descent: updating parameters in batches. The error curve will move around stochastically, and true curve would be the average of those vectors.

Epochs = number of times going completely through your data.


Convolution Neural Network
--------------------------

Usually perform better than traditional layered neural networks.
Look at network for 2012 ImageNet winner.
Convolution layers: previous example focused on each input pixel. What if features encompass multiple input pixels? Can use convolutions to capture larger receptive fields.

Convolutions and pooling are like looking through a telescope. Goes down to a feature vector, and feature vector is what gets classified. Re-inflate to get to original dimensionality. Deconvolution (transpose convolution) layer up-samples to bring smaller data back to its original size.


Fully Convolutional Networks (FCN)
----------------------------

The default FCN is a no-information classifier. Be sure to look at the model predictions. This will always be an issue if your classes are not balanced.
To fix this, use a cost function. Choice of cost function can make a big difference.

What is a Dice metric?? The higher the better.
