import numpy as np
import pandas as pd
import os

# Define the input and output directories
input_directory = r'C:\Users\allan\OneDrive\Bureau\IA\extracted-data\LA'
output_directory = r'C:\Users\allan\OneDrive\Bureau\IA\fft\LA'

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Process each file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, filename)

        # Load data from CSV
        data = pd.read_csv(file_path, header=None)
        data = data.squeeze()  # Convert DataFrame to Series if necessary

        # Apply FFT
        fft_result = np.fft.fft(data.values)

        # Get magnitudes of the frequencies
        magnitudes = np.abs(fft_result)

        # Save the magnitudes to a new CSV file
        np.savetxt(output_path, magnitudes, delimiter=',')

print("FFT processing complete for all files.")
