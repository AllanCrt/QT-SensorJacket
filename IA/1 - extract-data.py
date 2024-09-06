import pandas as pd
import os

# Define the directory paths
input_directory = r'C:\Users\allan\OneDrive\Bureau\IA\raw-data\LA'
output_directory = r'C:\Users\allan\OneDrive\Bureau\IA\extracted-data\LA'

# Make sure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Iterate over each file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, filename)

        # Read the CSV file
        data = pd.read_csv(file_path, header=None)

        # Select the fifth column
        fifth_column = data.iloc[:, 7]

        # Save the fifth column to a new CSV file
        fifth_column.to_csv(output_path, index=False, header=False)

print("Data extraction complete.")
