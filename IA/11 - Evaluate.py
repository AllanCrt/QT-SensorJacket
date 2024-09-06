# Create a pipeline that standardizes the data then trains the SVM
clf = make_pipeline(StandardScaler(), svm.SVC(kernel='linear'))

# Train the model
clf.fit(X_train, y_train)