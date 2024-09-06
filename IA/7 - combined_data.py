import pandas as pd
import os

# Assuming all average FFT CSV files are in this directory
input_directory = r'D:\Users\allan\Documents\Cours\Master\Master-GL\Stage Helsinki\IA\6 - average\LA'

# List to hold the data
data = []

# Labels for your data (ensure these are correctly matched with your files)
# For example: labels = ["nothing", "stroke", "tapping", "long_touch"]
labels = [...]  # Replace with your actual labels

for filename, label in zip(os.listdir(input_directory), labels):
    if filename.endswith('.csv'):
        file_path = os.path.join(input_directory, filename)
        # Load the data
        file_data = pd.read_csv(file_path, header=None)
        # Add label column
        file_data['label'] = label
        data.append(file_data)

# Combine all data into a single DataFrame
combined_data = pd.concat(data, ignore_index=True)

# Save the combined data
combined_data.to_csv(r'D:\Users\allan\Documents\Cours\Master\Master-GL\Stage Helsinki\IA\combined_data.csv', index=False)
