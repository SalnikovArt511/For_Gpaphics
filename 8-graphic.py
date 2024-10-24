import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt

with open('/home/b03-401/Desktop/Scripts/settings.txt', 'r') as f:
    avg_descritisation_frequency = float(f.read())

data = np.loadtxt('/home/b03-401/Desktop/Scripts/data.txt', dtype=np.float64)

fig, ax = plt.subplots()
Period = round(len(data) / avg_descritisation_frequency)
times = np.linspace(0, Period, len(data))
print(Period)
plt.grid(which='major', linestyle='-', linewidth=1)
plt.grid(which='minor', linestyle=':')
line, = ax.plot(times, data, linestyle='-', color='blue', label='V(t)', 
                markevery=[i for i in range(0, len(data), 20)], 
                marker="^", markerfacecolor='red', markersize=7, markeredgecolor='black') 
ax.set_xlabel('Время, с')
ax.set_ylabel('Напряжение, В')
ax.set_title('Процесс заряда и разряда конденсатора в RC-цепочке', wrap=True, loc='center')
ax.xaxis.set_minor_locator(mlt.ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(mlt.ticker.MultipleLocator(0.1))
ax.set_xlim([0, 10])
ax.set_ylim([0, 3])
ax.legend(handles = [line])

charging_time = data.argmax()/len(data) * Period
uncharging_time = Period - charging_time
ax.text(6.1, 2.1, f'Время заряда: {round(charging_time, 2)} с')
ax.text(6.1, 1.8, f'Время разряда: {round(uncharging_time, 2)} с')
fig.set_size_inches(8, 6)
fig.savefig('graphic.svg', dpi=400)

plt.show()
