import serial
import json
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

try:
    ser = serial.Serial('COM4', 9600, timeout=1)  # Remplacez 'COM4' par le port série approprié
    time.sleep(2)  # Temps pour que la connexion série soit établie
    print("Serial port opened successfully.")
except serial.SerialException as e:
    print(f"Failed to open serial port: {e}")
    exit()

def save_to_json(data):
    try:
        with open('data.json', 'a') as f:  # Utilisation du mode append pour ajouter les données
            f.write(data + '\n')  # Écrire une nouvelle ligne après chaque entrée
        print("Data saved to data.json")
    except Exception as e:
        print(f"Failed to save data to JSON: {e}")

# Initialiser les listes de données
data1 = []
data2 = []

# Initialiser le graphique
fig, ax = plt.subplots()
line1, = ax.plot([], [], label='Sensor 1')
line2, = ax.plot([], [], label='Sensor 2')
ax.legend()

# Configuration initiale des axes
ax.set_xlim(0, 500)
ax.set_ylim(0, 1024)

print("Server listening on serial port COM4")

useCase = 1; #1 - RA, 2 - RF, 3 - B, 4 - LA

def update_graph(frame):
    while ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        data = line.split(',')
        if len(data) == 8:
            try:
                # Parse the data explicitly
                sensorValue1, sensorValue2 = int(data[0]), int(data[1])
                sensorValue3, sensorValue4 = int(data[2]), int(data[3])
                sensorValue5, sensorValue6 = int(data[4]), int(data[5])
                sensorValue7, sensorValue8 = int(data[6]), int(data[7])
                
                # Save data entry
                data_entry = f"{sensorValue1}, {sensorValue2}, {sensorValue3}, {sensorValue4}, {sensorValue5}, {sensorValue6}, {sensorValue7}, {sensorValue8}"
                save_to_json(data_entry)

                # Ajouter les nouvelles données aux listes
                if (useCase == 1):
                    data1.append(sensorValue1)
                    data2.append(sensorValue5)
                elif (useCase == 2):
                    data1.append(sensorValue2)
                    data2.append(sensorValue6)
                elif (useCase == 3):
                    data1.append(sensorValue3)
                    data2.append(sensorValue7)
                elif (useCase == 4):
                    data1.append(sensorValue4)
                    data2.append(sensorValue8)

                

                # Limiter la taille des listes pour garder le graphique lisible
                if len(data1) > 500:
                    data1.pop(0)
                    data2.pop(0)

            except ValueError:
                print(f"Invalid data received: {line}")

    # Mettre à jour les données du graphique
    line1.set_ydata(data1)
    line1.set_xdata(range(len(data1)))
    line2.set_ydata(data2)
    line2.set_xdata(range(len(data2)))

    # Ajuster les limites de l'axe
    ax.relim()
    ax.autoscale_view()

ani = animation.FuncAnimation(fig, update_graph, interval=50)
plt.show()


try:
    while True:
        time.sleep(1)  # Maintenir le script en cours d'exécution
except KeyboardInterrupt:
    print("Server stopped by user")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    ser.close()
    print("Serial port closed")

