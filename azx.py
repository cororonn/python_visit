import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

val_x_data = np.random.uniform(0, 1, (60000, 32, 32))
val_y_data = np.random.randint(0, 5, (60000))

print(val_x_data.shape, val_y_data.shape)

X_train, X_test, y_train, y_test = train_test_split(val_x_data, val_y_data, test_size=0.5)

train_data = tf.data.Dataset.from_tensor_slices((X_train, y_train))


def data_index(x, y):
    x = tf.reshape(x, [-1,])
    return x, y
train_data_map = train_data.map(data_index)

train_data_map.take(1)

for x, y in train_data_map.take(5):
    print(x.shape, y)

train_data_batch = train_data_map.batch(32)

for x, y in train_data_batch.take(5):
  print(x.shape, y.shape)


model = lambda x: np.random.randint(0, 5, (32,)) 

for x, y in train_data_batch:
    predicted = model(x)

print(model)
print(predicted)