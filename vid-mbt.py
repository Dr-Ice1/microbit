import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel(r'C:\Users\alexa\Documents\Sensor\Files\mbt.xlsx', sheet_name='vid', usecols='A:E')

vid = df['video(m)']
sensor = df['sensor(m)']
druk = df['druk(bar)']
width = 0.1

fig, ax1= plt.subplots()

ax1.bar(druk+.05, sensor, color='darkcyan', width=width)
ax1.bar(druk-.05, vid, width=width, color='brown')
ax1.errorbar(6-.05, 19.1, yerr=5.4, color='orange', capsize=5)
ax1.errorbar(6+.05, 10.9, yerr=1.75, color='orange', capsize=5)
ax1.errorbar(7-.05, 12.9, yerr=3.85, color='orange', capsize=5)
ax1.errorbar(7+.05, 9.2, yerr=1.2, color='orange', capsize=5)

ax1.set_ylabel('Hoogte (m)')
ax1.set_xlabel('P (bar)')
ax1.set_xticks(np.arange(5,8,step=1))

ax1.legend(['Sensor Data', 'Videometing Data'], loc='upper left', ncols=3)


plt.show()