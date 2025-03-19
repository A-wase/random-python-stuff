import matplotlib.pyplot as plt

# data
load = [0, 0.981, 1.962, 2.843, 3.824, 4.905]  # Load in N
delta_v = [0, 0, 0.19, 1.40, 2.56, 4.06]  # Vertical deflection in mm
delta_h = [0, -0.22, -1.39, -1.41, -3.22, -5.1]  # Horizontal deflection in mm

# Plot Load vs Vertical Deflection
plt.figure(figsize=(8, 5))
plt.plot(load, delta_v, marker='o', linestyle='-', label='Vertical Deflection')
plt.xlabel('Load (N)')
plt.ylabel('Vertical Deflection (mm)')
plt.title('Load vs Vertical Deflection')
plt.legend()
plt.grid(True)
plt.show()

# Plot Load vs Horizontal Deflection
plt.figure(figsize=(8, 5))
plt.plot(load, delta_h, marker='s', linestyle='-', color='r', label='Horizontal Deflection')
plt.xlabel('Load (N)')
plt.ylabel('Horizontal Deflection (mm)')
plt.title('Load vs Horizontal Deflection')
plt.legend()
plt.grid(True)
plt.show()

# Combined Graph
plt.figure(figsize=(8, 5))
plt.plot(load, delta_v, marker='o', linestyle='-', label='Vertical Deflection')
plt.plot(load, delta_h, marker='s', linestyle='-', color='r', label='Horizontal Deflection')
plt.xlabel('Load (N)')
plt.ylabel('Deflection (mm)')
plt.title('Load vs Deflections')
plt.legend()
plt.grid(True)
plt.show()


import numpy as np
# Calculating gradients
gradient_v = np.gradient(delta_v, load)  # Vertical deflection gradient
gradient_h = np.gradient(delta_h, load)  # Horizontal deflection gradient

# Print the gradients at each point
print("Gradient of Vertical Deflection:", gradient_v)
print("Gradient of Horizontal Deflection:", gradient_h)
