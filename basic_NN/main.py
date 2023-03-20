import tensorflow as tf
import numpy as np


model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# load mnist
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data(path='mlnumbers')

# reshape, normalize, and convert inputs to float32
x_train = (x_train / 255.).reshape([-1, 784]).astype(np.float32)
x_test = (x_test / 255.).reshape([-1, 784]).astype(np.float32)

# convert labels to one-hot vectors
y_train, y_test = tf.one_hot(y_train, 10), tf.one_hot(y_test, 10)

# prepare for training
train_data = tf.data.Dataset.from_tensor_slices((x_train, y_train))
train_data = train_data.shuffle(500).batch(32)

model.compile(optimizer='adam', loss='categorical_crossentropy')
model.fit(train_data)

def accuracy(y_pred, y_true):
    correct_prediction = tf.equal(tf.argmax(y_pred, -1), tf.argmax(y_true, -1))
    return tf.reduce_mean(tf.cast(correct_prediction, tf.float32), axis=-1)

pred = model(x_test)

print(f'Test accuracy: {accuracy(pred, y_test)}')
input("prompt: ")