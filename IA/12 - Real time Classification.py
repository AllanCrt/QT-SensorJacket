# Save the trained model
import joblib

joblib.dump(clf, r'C:\Users\allan\OneDrive\Bureau\IA\touch_classifier_svm.pkl')

# To load the model later:
# clf = joblib.load(r'C:\Users\allan\OneDrive\Bureau\IA\touch_classifier_svm.pkl')

# Example of using the model for real-time prediction
def classify_touch(fft_values):
    fft_values = np.array(fft_values).reshape(1, -1)
    prediction = clf.predict(fft_values)
    return prediction[0]

# Example usage:
# touch_type = classify_touch(new_fft_data)
