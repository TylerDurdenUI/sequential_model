import tensorflow as tf
from tensorflow.keras.layers import Input, Embedding, Reshape, Multiply, Bidirectional, GRU, Dense, Flatten, Attention
from tensorflow.keras.models import Model

# Model hyperparameters
num_categories = 1000
embedding_dim = 128
seq_length = 50
gru_units = 128

# Input sequences
input_seq1 = Input(shape=(seq_length,), name='input_seq1')
input_seq2 = Input(shape=(seq_length,), name='input_seq2')

# Embedding layer for non-language categorical data
embedding = Embedding(num_categories, embedding_dim)

# Embed the first input sequence
embedded_seq1 = embedding(input_seq1)

# Reshape the second input sequence
reshaped_seq2 = Reshape((seq_length, 1))(input_seq2)

# Repeat reshaped_seq2 along the embedding_dim axis to match the shape of embedded_seq1
repeated_seq2 = tf.repeat(reshaped_seq2, repeats=embedding_dim, axis=-1)

# Element-wise multiplication to capture interactions
interaction = Multiply()([embedded_seq1, repeated_seq2])

# Bidirectional GRU layer
gru_output = Bidirectional(GRU(gru_units, return_sequences=True))(interaction)

# Attention layer
attention_layer = Attention()
attention_output = attention_layer([gru_output, gru_output])

# Flatten the attention layer output
attention_flat = Flatten()(attention_output)

# Classification layer
output = Dense(1, activation='sigmoid')(attention_flat)

# Build and compile the model
model = Model(inputs=[input_seq1, input_seq2], outputs=output)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()
