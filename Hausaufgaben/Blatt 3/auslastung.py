import psutil
import subprocess
import matplotlib.pyplot as plt
import numpy as np
import time
import sys

pid = int(sys.argv[1])
output_file = sys.argv[2]

def get_auslastung(pid, max_iterations=60*30, sleep_time=1, output_file='auslastung.png'):
    # Listen für die Auslastung
    cpu_usage = []
    gpu_usage = []
    ram_usage = []

    # Schleife zur Aufzeichnung der Auslastung
    for i in range(max_iterations):
        # CPU- und RAM-Auslastung abrufen
        process = psutil.Process(pid)
        cpu_percent = process.cpu_percent()
        mem_info = process.memory_info()
        mem_usage = mem_info.rss / 1024 / 1024  # in MB umrechnen

        # GPU-Auslastung abrufen
        cmd = "nvidia-smi --query-gpu=utilization.gpu --format=csv"
        output = subprocess.check_output(cmd, shell=True).decode()
        gpu_percent = float(output.split("\n")[1].split(",")[0].strip().rstrip("%"))
        
        # Auslastung zur Liste hinzufügen
        cpu_usage.append(cpu_percent)
        gpu_usage.append(gpu_percent)
        ram_usage.append(mem_usage)
        # Wenn das Training abgeschlossen ist, die Schleife beenden, falls das nicht stattfindet, bricht ab nach 3 minuten
        if i > 0 and cpu_usage[i] == 0 and gpu_usage[i] == 0 and ram_usage[i] == ram_usage[i-1]:
            print("Training abgeschlossen")
            break

        # Pause für 1 Sekunde einlegen
        time.sleep(sleep_time)

    # Plot erstellen
    fig, ax1 = plt.subplots()
    x = np.arange(len(cpu_usage))
    # CPU- und GPU-Prozentsätze auf der linken y-Achse zeichnen
    color = 'tab:red'
    ax1.set_xlabel('Zeitschritt (s)')
    ax1.set_ylabel('CPU/GPU %', color=color)
    ax1.plot(x, cpu_usage, color=color, label='CPU')
    ax1.plot(x, gpu_usage, color='tab:blue', label='GPU')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.legend(loc='upper left')

    # RAM-Nutzung auf der rechten y-Achse zeichnen
    ax2 = ax1.twinx()  # eine zweite y-Achse für RAM-Nutzung erstellen
    color = 'tab:green'
    ax2.set_ylabel('RAM (MB)', color=color)
    ax2.plot(x, ram_usage, color=color, label='RAM')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.legend(loc='upper right')

    # Titel hinzufügen und Diagramm anzeigen
    plt.title('CPU/GPU und RAM Nutzung')
    plt.savefig(output_file)

#get_auslastung(2099466, output_file='output/auslastung/baseline2.png')
get_auslastung(pid, output_file=output_file)