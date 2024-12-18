# Груз массой 0.2 кг подвешенный на пружине с жесткостью 20 Н/м лежит
# на подставке так что пружина не деформирована.
# Подставку убирают и груз начинает совершать колебания.
# Определить максимальную скорость колебаний груза и составить формулу для графика.

import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import make_interp_spline

def func(w, t):
    return A * math.sin(w * t)

def frange(start, stop, step):
    while start < stop:
        yield round(start, 1)
        start += step

k = 20 # коэф. натяжения нити
m = 0.2 # масса
A = 0.0981 # амплитуда
T = (2 * 3.14 * (m / k) ** 0.5) # период
w = 2 * 3.14 / T # частота

t_values = np.array(list(frange(0, 1.4, 0.1)))
x_values = np.array([func(w, t) for t in t_values])

t_smooth = np.linspace(t_values.min(), t_values.max(), 300)
spline = make_interp_spline(t_values, x_values, k=3)
x_smooth = spline(t_smooth)

scatter_values_x = []
for i in range(5):
    scatter_values_x.append(i * 0.25)
scatter_values_y = np.array([func(w, t) for t in scatter_values_x])

t_max_x = []
t_max_y = []
cnt = 0
for i in range(1, 9, 2):
    t = (-1)**cnt
    t_max_x.append(i*3.14/20)
    t_max_y.append(A*t)
    cnt +=1

t_sr_x = []
t_sr_y = []
for i in range(0, 5):
    t_sr_x.append(i*3.14/10)
    t_sr_y.append(0)
    
plt.figure(figsize=(10, 6))
ticks = [0, T/4, T/2, 3*T/4, T, 5*T/4, 3*T/2, 7*T/4, 2*T]
tick_labels = ['0', 'T/4', 'T/2', '3T/4', 'T', '5T/4', '3T/2', '7T/4', '2T']
plt.xticks(ticks, tick_labels)
plt.plot(t_smooth, x_smooth)
plt.scatter(t_sr_x, t_sr_y, color='red', zorder = 5)
plt.scatter(t_max_x, t_max_y, color='red', zorder = 5)
plt.xlabel('T, с')
plt.ylabel('A, м')
plt.title('График зависимости A от времени')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid()
plt.show()
