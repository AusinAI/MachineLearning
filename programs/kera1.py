from keras.models import Sequential
from keras.layers import Dense, Activation
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
