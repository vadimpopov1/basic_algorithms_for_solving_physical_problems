# Дифференциальное уравнение затухающих колебаний в LCR-контуре имеет вид d^2q/dt^2 + 4 * 10^4 * dq/dt + 10 ^ 10 q = 0 Кл/с^2
# Определить индуктивность и споротивление включеных в контур катушки индуктивности и резистора, ё
# собственную частоту колебаний в контуре, частоту и период затухающих колебаний.
# время релаксации, добротность контура, если емкость конденсатора равна 100 мФ

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

beta = 2e4
omega = 9.98e4
q0 = 1

T = 2 * np.pi / omega
t = np.linspace(0, 2.1 * T, 1000)

q = q0 * np.exp(-beta * t) * np.cos(omega * t)

maxima_indices = argrelextrema(q, np.greater)[0]
maxima_values = q[maxima_indices]
minima_indices = argrelextrema(q, np.less)[0]
minima_values = q[minima_indices]

zero_crossings_indices = np.where(np.diff(np.sign(q)))[0]
zero_crossings_t = t[zero_crossings_indices]
zero_crossings_q = q[zero_crossings_indices]

plt.figure(figsize=(10, 6))
plt.plot(t, q, label=r'$q(t) = e^{-\beta t} cos(omega t)$')
plt.scatter(t[maxima_indices], maxima_values, color='red', label='Максимумы', zorder=5)
plt.scatter(t[minima_indices], minima_values, color='red', label='Минимумы', zorder=5)
plt.scatter(zero_crossings_t, zero_crossings_q, color='red', label='Пересечения с осью $t$', zorder=5)
plt.scatter(0, 1, color='red', zorder=5)
ticks = [0, T/4, T/2, 3*T/4, T, 5*T/4, 3*T/2, 7*T/4, 2*T]
tick_labels = ['0', 'T/4', 'T/2', '3T/4', 'T', '5T/4', '3T/2', '7T/4', '2T']
plt.xticks(ticks, tick_labels)
plt.title('Затухающие колебания в LCR-контуре')
plt.xlabel('t, с')
plt.ylabel('q, Кл')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True)
plt.legend()
plt.show()