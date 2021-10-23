import numpy as np
import tensorflow as tf
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

import pickle
# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

IMG_SIZE = 28
x_train_arr = np.array(x_train).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
x_test_arr = np.array(x_test).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
          activation='relu', input_shape=(28, 28, 1)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

model.compile(loss="sparse_categorical_crossentropy",
              optimizer="adam", metrics=['accuracy'])
model.fit(x_train_arr, y_train, batch_size=1, epochs=5, validation_split=0)
tf.keras.models.save_model(model, 'my_model.hdf5')
# pickle.dump(model,open('modal.pkl','wb')

# modal=pickle.load(open('modal.pkl','rb'))
