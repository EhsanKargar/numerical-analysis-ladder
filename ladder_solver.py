import numpy as np
import matplotlib.pyplot as plt

# Input parameters
w1 = 9   # feet
w2 = 7   # feet
a_deg = 123
a = np.radians(a_deg)  # convert angle a to radians

# Define range of angle c (in radians)
c_vals = np.linspace(np.radians(1), np.pi - a - 0.01, 300)
L_vals = []

# Compute L(c) for each angle c
for c in c_vals:
    sin_c = np.sin(c)
    sin_ac = np.sin(a + c)
    if sin_c == 0 or sin_ac == 0:
        L_vals.append(np.inf)
    else:
        L = w1 / sin_ac + w2 / sin_c
        L_vals.append(L)

# Find the minimum ladder length and corresponding angle
min_index = np.argmin(L_vals)
c_opt = c_vals[min_index]         # in radians
L_min = L_vals[min_index]

# Plotting
img = plt.imread('ladder_mine.png')
plt.imshow(img)
plt.figure(figsize=(8, 5))
plt.plot(c_vals, L_vals, label='Ladder Length $L(c)$', color='blue')
plt.axvline(c_opt, color='red', linestyle='--', label=f'Optimal angle c ≈ {c_opt:.4f} rad')
plt.scatter(c_opt, L_min, color='red')
plt.xlabel('Angle c (radian)')
plt.ylabel('Ladder Length (feet)')
plt.title('Variation of Ladder Length with Respect to Angle c (radians)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

