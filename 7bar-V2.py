import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd

x = '7bar'

df = pd.read_excel(r'C:\Users\alexa\Documents\Sensor\Files\mbt.xlsx', sheet_name=x, usecols='A:H')

#zm = df['zm']
#z = df['z']
#t = df['t']

z1 = df['z1']*[-1]
t1 = df['t1']
z3 = df['z3']*[-1]
t3 = df['t3']
z4 = df['z4']*[-1]
t4 = df['t4']

fig, ax = plt.subplots()


ax.plot(t1, z1, marker='.')
# ax.set_xticks(np.arange(start=125, stop=129, step=.5))
# ax.set_title("7 Bar test #1", font="Times New Roman", fontsize=20)
ax.text(125.4, 5.5, r'h$_{max}$ = 5,24 m', font='Times New Roman', fontsize=15, math_fontfamily='cm')
#x_tail = 68.4
#y_tail = 10.9
#x_head = 69.45
#y_head = 11
#arrow = mpatches.FancyArrowPatch((x_tail, y_tail), (x_head, y_head), mutation_scale=24, color='red')
#ax1.add_patch(arrow)
#ax1.annotate('Top', (68, 10.8), font="Times New Roman", fontsize=14, color='red')


ax.plot(t3, z3, marker='.', color='red')
# ax.set_xticks(np.arange(start=71, stop=75.7, step=0.6))
# ax.set_title("7 Bar test #3", font="Times New Roman", fontsize=20)
# ax.set_xlabel("t (s)", font="Times New Roman", fontsize=16)
# ax.set_ylabel("h (m)", font="Times New Roman", fontsize=16)
ax.text(75.3, 8.3, r'h$_{max}$ = 8,25 m', font='Times New Roman', fontsize=15, math_fontfamily='cm')
#x_tail = 84.85
#y_tail = 7.8
#x_head = 85.8
#y_head = 7.9
#arrow = mpatches.FancyArrowPatch((x_tail, y_tail), (x_head, y_head), mutation_scale=28)
#ax2.add_patch(arrow)
#ax2.annotate('Top', (84.6, 7.75), font="Times New Roman", fontsize=14, color='blue')


ax.plot(t4, z4, marker='.', color='orange')
# ax.set_xticks(np.arange(start=245, stop=249.5, step=.8))
# ax.set_title("7 Bar test #4", font="Times New Roman", fontsize=20)
# ax.set_xlabel("t (s)", font="Times New Roman", fontsize=16)
# ax.set_ylabel("h (m)", font="Times New Roman", fontsize=16)
ax.text(227, 9, r'h$_{max}$ = 9,2 m', font='Times New Roman', fontsize=15, math_fontfamily='cm')
#x_tail = 164.85
#y_tail = 8.3
#x_head = 166
#y_head = 8.35
#arrow = mpatches.FancyArrowPatch((x_tail, y_tail), (x_head, y_head), mutation_scale=23, color='orange')
#ax3.add_patch(arrow)
#ax3.annotate('Top', (164.5, 8.2), font="Times New Roman", fontsize=14, color='orange')

#



#plt.savefig(f'C:/Users/alexa/Documents/Sensor/media/az-tests\{x}.png')
ax.set_xlabel("t (s)", font="Times New Roman", fontsize=17)
ax.set_ylabel("h (m)", font="Times New Roman", fontsize=17)
plt.legend(['test #3', 'test #1', 'test #4'], loc='upper left')
plt.title(r'7 Bar ($p$ = 700.000 Pa)', font='Times New Roman', fontsize=25, math_fontfamily='cm')

plt.show()
