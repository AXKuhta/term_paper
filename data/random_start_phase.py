import matplotlib.pyplot as plt
import numpy as np

x = np.arange(400) / 1000 / 1000 / 1000
y = np.sin(np.pi*2*x * 10*1000*1000)
y[:100] = 0

z = np.sin(np.pi*2*x * 10*1000*1000 + 1.7*np.pi)
z[:100] = 0

fig, axes = plt.subplots(1, 2, figsize=[6, 2])
l, r = axes

l.plot(y, color="black", linewidth=1)
r.plot(z, color="black", linewidth=1)
l.set_axis_off()
r.set_axis_off()

plt.savefig("random_start_phase.pdf")
