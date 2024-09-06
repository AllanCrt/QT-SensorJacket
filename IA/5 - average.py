import pandas as pd
import numpy as np
import os

def calculate_averages(data, segment_length=60, overlap=45, group_size=6):
    averages = []
    start = 0
    while start + segment_length <= len(data):
        segment = data.iloc[start:start + segment_length]
        grouped_averages = [segment.iloc[i:i + group_size].mean() for i in range(0, segment_length, group_size)]
        averages.append(grouped_averages)
        start += overlap
        print(f"Processed segment starting at index {start}")  # Progress update
    return averages

input_directory = r'C:\Users\allan\OneDrive\Bureau\IA\fft\LA'
output_directory = r'C:\Users\allan\OneDrive\Bureau\IA\average\LA'
os.makedirs(output_directory, exist_ok=True)

for filename in os.listdir(input_directory):
    if filename.endswith('.csv'):
        print(f"Processing file: {filename}")  # File processing update
        file_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, filename)

        data = pd.read_csv(file_path, header=None).squeeze()
        averages = calculate_averages(data)
        averages_df = pd.DataFrame(averages)
        averages_df.to_csv(output_path, index=False, header=False)
        print(f"Finished processing {filename}")  # Completion update

print("All files processed successfully.")
