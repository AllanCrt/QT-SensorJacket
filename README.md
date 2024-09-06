# QT-SensorJacket

## Overview

The QT-SensorJacket project aims to create an interactive system where a QT robot can recognize and respond to various touch types (stroking, tapping, and long touch) on a sensor-equipped jacket. The project leverages data collected from pressure and triboelectric sensors, processes it using Fast Fourier Transform (FFT), and classifies the touch type using a Support Vector Machine (SVM) model.

## Project Structure for AI

### Directories

- **0 - raw data**: Contains the original data files collected from the sensors.
- **2 - extracted data**: Stores the extracted data (5th column) from the raw data files.
- **4 - fft**: Holds the FFT-transformed data.
- **6 - average**: Contains averaged FFT data.
- **8 - combined_data**: Includes combined and processed data ready for training.

### Files

1. **extract-data.py**: Script to extract the 5th column from raw data CSV files and save it to the extracted data directory.
2. **fft.py**: Transforms the extracted data using FFT and saves the results to the FFT directory.
3. **average.py**: Averages the FFT data in segments and saves the results to the average directory.
4. **combined_data.py**: Combines the averaged data into a single dataset for training.
5. **split.py**: Splits the combined dataset into training and testing sets.
6. **train.py**: Trains the SVM model using the training dataset.
7. **evaluate.py**: Evaluates the trained SVM model using the testing dataset.
8. **real_time_classification.py**: Performs real-time classification of touch types using the trained SVM model.


