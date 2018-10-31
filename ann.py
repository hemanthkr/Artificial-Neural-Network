 # Create Model

model = Sequential()
model.add(Dense(40, activation='relu', input_dim=12288))
model.add(Dropout(0.1))
model.add(Dense(25, activation='relu'))
# model.add(Dropout(0.1))
model.add(Dense(1, activation='sigmoid'))

# Compile model

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Fit the model

model.fit(x_trn, y_trn, epochs=100, batch_size=10)

# Evaluate the model

scores = model.evaluate(x_trn, y_trn)
print("\ntraining %s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

scores1 = model.evaluate(x_tst, y_tst)
print("\ntesting %s: %.2f%%" % (model.metrics_names[1], scores1[1]*100))
