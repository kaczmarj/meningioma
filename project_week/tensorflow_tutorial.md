# Tensorflow

Google uses TPUs, not GPUs, to run Tensorflow. These are availablethorugh Google Cloud Services.
Top level is tf.learn (high-level API inspired by sklearn). Use TensorBoard to visualize information about your network.

A tensor is an individual data piece. The rank of the tensor is determined by the number of axes. This is different from the dimensions. Tensor can be of any rank.

Get onto your Graph, then you can run within a session. (`with tf.Session()`)

Constants are edges; edges go into node; output of node is another edge.

`tf.constant` defines an edge.

Training a neural network is an optimization; trying to minimize loss (error).

It might be helpful to scale your data between 0 and 1.

TIP: visualize your output (e.g., loss, predictions) while it runs. Look at PLAYGROUND.TENSORFLOW.ORG. And maybe tensorflow debugger (github).

The majority of machine learning at Google is done with linear regression. If you want to find trends in house prices across the globe, it would be good to "bin" the data instead of using latitude and longitude.

For segmentation, instead of mapping X, Y, it would be better to bin parts of the image. Compare linear regression + feature engineering to neural networks. Tensorflow provides linear regression framework.

Accuracy can be misleading for problems with disproportionate distributions of classes. Also look at false positive and true negatives.

In machine learning, you can use your data about 10 times, and after that, the risk of overfitting is high.

tf.contrib.learn.LinearClassifier does linear regression.

Use a confusion matrix, and look into ROC curve. You should plot the log(loss) over periods too.

To switch between classifiers, you just switch between LinearClassifier and DNNClassifier (and change the necessary parameters).

The more non-linear your data is, the more layers you need to represent your data.
