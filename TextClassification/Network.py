import numpy as np
import tensorflow as tf

#Functions to produce weights and bias variables, can change std deviation if we want
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=1)
    return tf.Variable(initial)

def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)