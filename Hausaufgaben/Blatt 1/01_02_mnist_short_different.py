from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.regularizers import l2

# Laden der MNIST-Daten
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Vorbereitung der Daten
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
x_train = x_train.reshape((60000,28*28))
x_test = x_test.reshape((10000,28*28))

# Definition des neuronalen Netzes
# 2 Hidden-Layer mit jeweils 256 Neuronen --> 10 Output-Neuronen (0-9)
model = Sequential([
    Dense(256, activation="relu", kernel_regularizer=l2(0.001), input_shape=(28*28,)),
    Dense(256, activation="relu"),
    Dense(10, activation="softmax")
])

# Kompilieren des Modells
model.compile(
    loss="sparse_categorical_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)

# Training des Modells
history = model.fit(
    x_train,
    y_train,
    batch_size=128,
    epochs=10,
    validation_data=(x_test, y_test)
)

# Auswertung des Modells
test_loss, test_acc = model.evaluate(x_test, y_test)
print("Test accuracy:", test_acc)