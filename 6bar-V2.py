import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd

x = '6bar'

df = pd.read_excel(r'C:\Users\alexa\Documents\Sensor\Files\mbt.xlsx', sheet_name=x, usecols='A:H')

#zm = df['zm']
#z = df['z']
#t = df['t']

z1 = df['z1']*[-1]
t1 = df['t1']
z2 = df['z2']*[-1]
t2 = df['t2']
z3 = df['z3']*[-1]
t3 = df['t3']

fig, ax = plt.subplots()


ax.plot(t1, z1, marker='.', color='red')
#plt.xticks(np.arange(start=66, stop=72.5, step=0.5))
#ax.set_title("6 Bar test #1", font="Times New Roman", fontsize=20)
ax.text(70.3, 10.8, r'h$_{max}$ = 10,86 m', font='Times New Roman', fontsize=15, math_fontfamily='cm')

# x_tail = 68.4
# y_tail = 10.9
# x_head = 69.45
# y_head = 11
# arrow = mpatches.FancyArrowPatch((x_tail, y_tail), (x_head, y_head), mutation_scale=24, color='red')
# ax1.add_patch(arrow)
# ax1.annotate('Top', (68, 10.8), font="Times New Roman", fontsize=14, color='red')

ax.plot(t2, z2, marker='.')
#plt.xticks(np.arange(start=84, stop=87.5, step=0.5))
#ax.set_title("6 Bar test #2", font="Times New Roman", fontsize=20)
ax.text(87.4, 7.7, r'h$_{max}$ = 7,8 m', font='Times New Roman', fontsize=15, math_fontfamily='cm')

# x_tail = 84.85
# y_tail = 7.8
# x_head = 85.8
# y_head = 7.9
# arrow = mpatches.FancyArrowPatch((x_tail, y_tail), (x_head, y_head), mutation_scale=28)
# ax2.add_patch(arrow)
# ax2.annotate('Top', (84.6, 7.75), font="Times New Roman", fontsize=14, color='blue')

ax.plot(t3, z3, marker='.', color='orange')
#plt.xticks(np.arange(start=164, stop=168, step=0.5))
#ax.set_title("6 Bar test #3", font="Times New Roman", fontsize=20)
ax.text(159, 8.5, r'h$_{max}$ = 8,32 m', font='Times New Roman', fontsize=15, math_fontfamily='cm')

# x_tail = 164.85
# y_tail = 8.3
# x_head = 166
# y_head = 8.35
# arrow = mpatches.FancyArrowPatch((x_tail, y_tail), (x_head, y_head), mutation_scale=23, color='orange')
# ax3.add_patch(arrow)
# ax3.annotate('Top', (164.5, 8.2), font="Times New Roman", fontsize=14, color='orange')


#plt.savefig(f'C:/Users/alexa/Documents/Sensor/media/az-tests\{x}.png')

plt.xlabel('t (s)', font='Times New Roman', fontsize=17)
plt.ylabel('h (m)', font='Times New Roman', fontsize=17)
plt.title(r'6 Bar ($p$ = 600.000 Pa)', font='Times New Roman', fontsize=25, math_fontfamily='cm')
plt.legend(['test #1','test #2','test #3'], loc='upper right')

plt.show()
