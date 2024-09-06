# Sensor Data Collection for Tactile Interaction Study

## Overview
This document explains the structure and meaning of the columns in the collected sensor data. The study involves recording sensor data from various body parts of the robot during different types of tactile interactions: stroking, touching, and tapping. Additionally, a baseline recording is taken with no interaction.

## Column Definitions
Each column in the dataset corresponds to an analog input pin on the Arduino, which is connected to a specific sensor. The sensors are placed on different body parts and measure different types of interaction (Pressure - P, Tribo - T).

### Column Mapping
A- **A0**: Sensor 1 (RA - Right Arm, Pressure - P)
B- **A1**: Sensor 2 (RF - Right Front, Pressure - P)
C- **A2**: Sensor 3 (B - Back, Pressure - P)
D- **A3**: Sensor 4 (LA - Left Arm, Pressure - P)
E- **A4**: Sensor 5 (RA - Right Arm, Tribo - T)
F- **A5**: Sensor 6 (RF - Right Front, Tribo - T)
G- **A6**: Sensor 7 (B - Back, Tribo - T)
H- **A7**: Sensor 8 (LA - Left Arm, Tribo - T)

### Types of Touch
The types of tactile interactions recorded are:
1. **Stroking**
2. **Touching**
3. **Tapping**

### Participants
Data is collected for two participants:
1. **Ramyah**
2. **Allan**

### Recording Sessions
For each type of touch and each participant, the data is recorded for 20 seconds. Additionally, a baseline recording is taken with no interaction. Therefore, the total sessions are:
- 4 areas × 3 types of touch × 2 participants = 24 sessions
- 1 baseline recording
