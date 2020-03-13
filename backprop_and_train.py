from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from keras.callbacks import EarlyStopping
from numpy import loadtxt

# load the dataset
dataset = loadtxt('anddata.txt', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:3] # first 3 columns are input
Y = dataset[:,3]   # last column is category


# define the keras model
model = Sequential()
model.add(Dense(4, input_dim=3, activation='relu')) # input layer with 3 inputs and 12 hidden nodes
model.add(Dense(1, activation='sigmoid')) # output layer with one node, takes input from hidden layer
opt = SGD(lr=0.02, momentum=0.9)

model.summary()

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
#model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit (=train) the keras model on the dataset
print("training ...")
es = EarlyStopping(monitor='loss', patience=30, min_delta=0.00001, mode='auto', verbose=1)
model.fit(X, Y, epochs=1000, batch_size=1, verbose=1)
#model.fit(X, Y, epochs=1000, batch_size=1, verbose=1, callbacks=[es])
print("Done training")

#serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("weights.h5")
print("Saved model to disk")

# binary save
#model.save("trainedmodel.h5")
#print("Saved model to disk")

# evaluate the trained model
testdataset = loadtxt('xordata.txt', delimiter=',')
# split into input (X) and output (y) variables (labels)
xtest = testdataset[:,0:3]
ytest = testdataset[:,3]

_, accuracy = model.evaluate(xtest, ytest, verbose=0)
print('Accuracy: %.2f' % (accuracy*100))
