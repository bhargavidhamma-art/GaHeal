import matplotlib.pyplot as plt
time = [0, 1, 2, 3, 4, 5, 10, 20]
resistance = [1000000, 1000000, 500, 100, 5, 2, 1.5, 1.2]
plt.figure(figsize=(9,5))
plt.plot(time, resistance, marker='o', color='green', linewidth=2.5)
plt.yscale('log')
plt.title('GaHeal - Self Healing Test | Crack to Heal in 5 Sec')
plt.xlabel('Time (seconds)')
plt.ylabel('Resistance (Ohm)')
plt.grid(True, which="both")
plt.show()
