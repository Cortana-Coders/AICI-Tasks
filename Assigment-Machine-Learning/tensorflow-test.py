# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

# Load IBM stock prices dataset
# Assuming the dataset is in a CSV file named 'IBM_Stock.csv' with a 'Close' column
ibm_stock = pd.read_csv('IBM_Stock.csv')
close_prices = ibm_stock['Close'].values

# Normalize the data
close_prices = close_prices.reshape(-1, 1)
scaler = StandardScaler()
close_prices = scaler.fit_transform(close_prices)

# Create sequences for RNN
def create_sequences(data, seq_length):
    sequences = []
    labels = []
    for i in range(len(data) - seq_length):
        sequences.append(data[i:i + seq_length])
        labels.append(data[i + seq_length])
    return np.array(sequences), np.array(labels)

seq_length = 10
X_seq, y_seq = create_sequences(close_prices, seq_length)

# Split the data
X_train_seq, X_test_seq, y_train_seq, y_test_seq = train_test_split(X_seq, y_seq, test_size=0.2, random_state=42)

# Create an RNN model
rnn_model = Sequential([
    SimpleRNN(50, activation='relu', input_shape=(seq_length, 1)),
    Dense(1)
])

# Compile the model
rnn_model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
rnn_model.fit(X_train_seq, y_train_seq, epochs=50, validation_data=(X_test_seq, y_test_seq))