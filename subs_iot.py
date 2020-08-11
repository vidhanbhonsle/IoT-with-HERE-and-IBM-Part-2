# Get and plot data from Watson IoT using Python
from random import uniform
from time import sleep

import matplotlib.pyplot as plt
#import DataPlot and RealtimePlot from the file plot_data.py
from plot_data import DataPlot, RealtimePlot

fig, axes = plt.subplots()
plt.title('Data from Watson IoT')

data = DataPlot()
dataPlotting= RealtimePlot(axes)
count=0

# plot data
while True:
    #global count
    tmp = uniform(20.0,30.0)
    hum = uniform(30,100)
    print(tmp)
    print(hum)
    count+=1
    data.add(count,tmp ,hum)
    dataPlotting.plot(data)
    plt.pause(0.001)
    sleep(5)
