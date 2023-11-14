import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd

x = '6bar'
y = '7bar'

df6 = pd.read_excel(r'C:\Users\alexa\Documents\Sensor\Files\mbt.xlsx', sheet_name=x, usecols='A:H')
df7 = pd.read_excel(r'C:\Users\alexa\Documents\Sensor\Files\mbt.xlsx', sheet_name=y, usecols='A:H')

z61 = df6['z1']*[-1]
t61 = df6['t1']
z62 = df6['z2']*[-1]
t62 = df6['t2']
z63 = df6['z3']*[-1]
t63 = df6['t3']

z71 = df7['z1']*[-1]
t71 = df7['t1']
z73 = df7['z3']*[-1]
t73 = df7['t3']
z74 = df7['z4']*[-1]
t74 = df7['t4']

fig, ax = plt.subplots()

### 6 BAR ###
# test #1
ax.plot(t61, z61, marker='.', color='mediumblue')
ax.text(70.3, 10.8, r'h$_{max}$ = 10,86 m', font='Times New Roman', fontsize=15, math_fontfamily='cm')
# test #2
ax.plot(t62, z62, marker='.', color='cornflowerblue')
ax.text(87.4, 7.7, r'h$_{max}$ = 7,8 m', font='Times New Roman', fontsize=15, math_fontfamily='cm')
# test #3
ax.plot(t63, z63, marker='.', color='blue')
ax.text(169, 8.3, r'h$_{max}$ = 8,32 m', font='Times New Roman', fontsize=15, math_fontfamily='cm')

### 7 BAR ###
# test #1
ax.plot(t71, z71, marker='.', color='limegreen')
ax.text(125.4, 5.5, r'h$_{max}$ = 5,24 m', font='Times New Roman', fontsize=15, math_fontfamily='cm')
#test #3
ax.plot(t73, z73, marker='.', color='forestgreen')
ax.text(75.3, 8.3, r'h$_{max}$ = 8,25 m', font='Times New Roman', fontsize=15, math_fontfamily='cm')
# test #4
ax.plot(t74, z74, marker='.', color='darkgreen')
ax.text(227, 9, r'h$_{max}$ = 9,2 m', font='Times New Roman', fontsize=15, math_fontfamily='cm')





ax.text(168, 11, r'Blauw = 6 Bar', font='Times New Roman', fontsize=15, math_fontfamily='cm')
ax.text(168, 10.5, r'Groen = 7 Bar', font='Times New Roman', fontsize=15, math_fontfamily='cm')
plt.xlabel('t (s)', font='Times New Roman', fontsize=17)
plt.ylabel('h (m)', font='Times New Roman', fontsize=17)
plt.title(r'6 en 7 Bar over tijd met h$_{max}$', font='Times New Roman', fontsize=25, math_fontfamily='cm')
plt.legend(['test #1','test #2','test #3', 'test #1','test #3','test #4'], loc='best')

plt.show()