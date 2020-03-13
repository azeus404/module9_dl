from numpy import loadtxt
from keras.models import model_from_json
from keras import optimizers

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("weights.h5")
print("Loaded model from disk")

loaded_model.summary()

# compile the keras model
loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# evaluate using test data
testdataset = loadtxt('xordata.txt', delimiter=',')
# split into input (X) and output (y) variables
xtest = testdataset[:,0:3]  # instances
ytest = testdataset[:,3]    # labels

_, accuracy = loaded_model.evaluate(xtest, ytest, verbose=0)
print('Accuracy: %.2f' % (accuracy*100))

# get result for first n samples of the test set
print("correct", "estimated")
for s in range(0, 8):
#    y_predicted = loaded_model.predict_classes(xtest[s:s+1])
    y_predicted = loaded_model.predict_classes(xtest[s:s+1])
    print(ytest[s:s+1], y_predicted)

