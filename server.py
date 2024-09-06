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
data1, data2, data3, data4, data5, data6, data7, data8 = [], [], [], [], [], [], [], []


# Initialiser le graphique
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()


line1, = ax1.plot([], [], label='RA - Right Arm, Pressure - P')
line2, = ax1.plot([], [], label='RA - Right Arm, Tribo - T')
line3, = ax2.plot([], [], label='RF - Right Front, Pressure - P')
line4, = ax2.plot([], [], label='RF - Right Front, Tribo - T')
line5, = ax3.plot([], [], label='B - Back, Pressure - P')
line6, = ax3.plot([], [], label='B - Back, Tribo - T')
line7, = ax4.plot([], [], label='LA - Left Arm, Pressure - P')
line8, = ax4.plot([], [], label='LA - Left Arm, Tribo - T')



# Configuration initiale des axes
for ax in [ax1, ax2, ax3, ax4]:
    ax.set_xlim(0, 500)
    ax.set_ylim(0, 1024)
    ax.legend()

print("Server listening on serial port COM4")

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
                data1.append(sensorValue1)
                data2.append(sensorValue2)
                data3.append(sensorValue3)
                data4.append(sensorValue4)
                data5.append(sensorValue5)
                data6.append(sensorValue6)
                data7.append(sensorValue7)
                data8.append(sensorValue8)

                # Limiter la taille des listes pour garder le graphique lisible
                if len(data1) > 500:
                    data1.pop(0)
                    data2.pop(0)
                    data3.pop(0)
                    data4.pop(0)
                    data5.pop(0)
                    data6.pop(0)
                    data7.pop(0)
                    data8.pop(0)

            except ValueError:
                print(f"Invalid data received: {line}")

    # Mettre à jour les données du graphique
    line1.set_ydata(data1)
    line1.set_xdata(range(len(data1)))
    line2.set_ydata(data2)
    line2.set_xdata(range(len(data2)))

    line3.set_ydata(data3)
    line3.set_xdata(range(len(data3)))
    line4.set_ydata(data4)
    line4.set_xdata(range(len(data4)))

    line5.set_ydata(data5)
    line5.set_xdata(range(len(data5)))
    line6.set_ydata(data6)
    line6.set_xdata(range(len(data6)))

    line7.set_ydata(data7)
    line7.set_xdata(range(len(data7)))
    line8.set_ydata(data8)
    line8.set_xdata(range(len(data8)))


    # Ajuster les limites de l'axe
    ax1.relim()
    ax1.autoscale_view()
    ax2.relim()
    ax2.autoscale_view()
    ax3.relim()
    ax3.autoscale_view()
    ax4.relim()
    ax4.autoscale_view()

    

ani1 = animation.FuncAnimation(fig1, update_graph, interval=50)
ani2 = animation.FuncAnimation(fig2, update_graph, interval=50)
ani3 = animation.FuncAnimation(fig3, update_graph, interval=50)
ani4 = animation.FuncAnimation(fig4, update_graph, interval=50)
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
