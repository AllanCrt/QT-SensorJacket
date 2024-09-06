from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Create a pipeline that standardizes the data then trains the SVM
clf = make_pipeline(StandardScaler(), svm.SVC(kernel='linear'))

# Train the model
clf.fit(X_train, y_train)
