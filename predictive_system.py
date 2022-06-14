import numpy as np
import pickle

#loading the saved model
loaded_model = pickle.load(open("trained_model.sav", 'rb'))

input_data = (0,166,1,0,30,0,0,1,50,29)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('Patient is not diabetic')
else:
  print('Patient is diabetic')