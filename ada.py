
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from keras.models import Sequential
from keras.layers import Dense

iris_df = pd.read_csv('iris_dataset.csv')
label_encoder = LabelEncoder()
iris_df['target'] = label_encoder.fit_transform(iris_df['target'])
# print(iris_df.head())
X = iris_df.drop(columns=['target'])
y = iris_df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = Sequential()
model.add(Dense(8, input_dim=4, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='linear')) 

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mse'])  

model.fit(X_train_scaled, y_train, epochs=100, batch_size=10, verbose=0)

y_pred = model.predict(X_test_scaled)

mse = model.evaluate(X_test_scaled, y_test)[1]
print("Mean Squared Error (MSE) on test set:", mse)

new_sample = np.array([[5.1, 3.5, 1.4, 0.2]])  
new_sample_scaled = scaler.transform(new_sample)

predicted_value = model.predict(new_sample_scaled)
print("Predicted value for the new sample:", predicted_value)
