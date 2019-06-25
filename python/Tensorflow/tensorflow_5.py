import tensorflow as tf
import numpy as np

### creat data ###

x_data = np.random.rand(100).astype(np.float32)
#np.random.rand(4,2) 2D 4 rows and 2 colums
#the type of most data in tensorflow is float32 
y_data = x_data*0.1 + 0.3
#the weight of predict data should close to 0.1 and biases should close to 0.3

### creat tensorflow structure start ###

Weight = tf.Variable(tf.random.uniform([1],-1.0,1.0))
#this random uniform is 1D, is the same as the array, from -1.0 to 1.0
biases = tf.Variable(tf.zeros([1])) 

y = Weight*x_data + biases
#this y is predict data, next we should enhance accuracy
loss = tf.reduce_mean(tf.square(y-y_data))
#at first the loss will be very huge
optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
#we use the optimizer to reduce the loss
#GradientDescentOptimizer is a type of optimizer
#0.5 is the learning rate, normally, it is a number less than 1 

init = tf.compat.v1.global_variables_initializer()
#

### create tensorflow structure end ###

sess = tf.compat.v1.Session()
#the session just like a point, to point the location in the tf structure
sess.run(init) #very important
#so we point on the inital to start this struture

for step in range(201):
   sess.run(train)
   if step % 20 == 0:
       print(step, sess.run(Weight),sess.run(biases))
