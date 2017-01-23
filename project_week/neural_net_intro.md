# Neural Network Intro

Loss function
-------------
Normalize the probabilities and take negative log. Result is in range of 0, inf. We want to minimize this value.

In first initiation of training, value of loss function should be 1 / c, where c is the number of classes.


Gradient descent
----------------
Go down the gradient to find minimum of loss function.


Full-batch vs mini-batch gradient descent
-----------------------------------------
full-batch:
  compute the gradient on the full batch of samples for each update.
mini-batch: (stochastic gradient descent, SGD)
  compute gradient on a small mini-batch of samples (e.g., 64)
  much faster computationally
online (mini-batch size=1):
  noisy, no computational advantage over mini-batch.

But SGD can reach minimum in an inefficient way. There are more efficient methods.

Momentum update
---------------
Physical analogy: ball rolling down the loss function; gradient is like the force at each moment, and the ball has momentum.

Nesterov Momentum
-----------------
first take momentum step, then take gradient step. Actual step is sum of those two steps.

Adagrad
-------
Keep a cache for each parameter. Normalizes the gradients differently for each parameter.

RMSPROP
-------
Makes Adagrad cache leaky so the loss function doesn't freeze before getting to minimum.


# Non-linearities

Sigmoid function is popular for introducing non-linearity. Squashes numbers between 0 and 1. This can saturate neurons, which is bad because saturated neurons kill gradients. It is also not zero-centered, and it uses exp() which is expensive.

tanh is zero-centered but still not great.

ReLU computes f(x) = max(0, x). Does not saturate, very computationally efficient, converges faster in practice than sigmoid and tanh, but it is not zero-centered. Dead ReLU (if gradient is < 0).

Leakly ReLU computes f(x) = max(0.01x, x). Does not die!
Parametric ReLU computes f(x) = max(ax, x), where a is learned.


# Weight initialization

If initialize all neurons with 0, the neurons will be identical (and they won't learn). There has to be some randomness.


# Regularization

Make network much more complex than data regime. Regularization prevents overfit. Start with small data regime.

Regularization techniques:
Data augmentation: translation; rotation; rescaling; flipping.
Weight decay: L1 regularization, L2 regularization.
Dropout: randomly turn off some of the neurons.

If learning rate is too low, very slow convergence. If it is too high, there is no convergence. It should be somewhere in the middle.

TIP: decay the learning rate as you go forward on your training.


# Babysitting the network

Plot the loss over chunk # (different line for each epoch).
