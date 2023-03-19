import tensorflow as tf
# doesnt display info messages
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 

#                x1  x2
x = tf.constant([[2, 3]], dtype='float')
#                   w1     w2    w3     w4
W0 = tf.constant([[0.11, 0.21], [0.12, 0.08]])
#              x * wT      -> result is hidden layer
h1 = tf.matmul(x, tf.transpose(W0))
#                  w5    w6
W1 = tf.constant([[0.14, 0.15]])
#             h1 * w1T     -> result is output layer
y = tf.matmul(h1, tf.transpose(W1))
print(y, h1)