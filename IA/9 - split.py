from sklearn.model_selection import train_test_split
import pandas as pd

# Load the combined dataset
data = pd.read_csv(r'D:\Users\allan\Documents\Cours\Master\Master-GL\Stage Helsinki\IA\combined_data.csv')

# Separate features and labels
X = data.drop('label', axis=1)
y = data['label']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


