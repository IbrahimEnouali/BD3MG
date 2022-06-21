import json
import matplotlib.pyplot as plt

measurand = "Total times"

with open(measurand + ".txt", "r") as f:
    data = json.load(f)
    x = []
    y = []

    single_processor_time = data["2"] # One master, one worker

    for cores in data:
        x.append(int(cores) - 1) # One master
        y.append(single_processor_time / data[cores])

    plt.plot(x, y, 'r+')
    plt.title("BD3MG Speed-up")
    plt.xlabel("Cores")
    plt.ylabel("Speed-up")
    plt.savefig("BD3MG Speed-up.png")