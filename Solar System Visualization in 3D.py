# Solar System Visualization in 3D

import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
semi_major_axis = [0.39, 0.72, 1.0, 1.52, 5.2, 9.58, 19.22, 30.05] # in AU (Astronomical Units)
orbit_period = [0.24, 0.62, 1.0, 1.88, 11.86, 29.46, 84.01, 164.8] # in years

plt.style.use("dark_background")

fig = plt.figure(figsize=(8, 8)) # Creates figure and axis, figure size is 8x8

ax = fig.add_subplot(111, projection="3d")

ax.scatter(0, 0, color="yellow", s=100, label="Sun") # Plots Sun at center

# Plot orbits of planets
for i, planet in enumerate(planet_names):
    orbit_radius = semi_major_axis[i]
    orbit_theta = np.linspace(0, 2 * math.pi, 100)
    x = orbit_radius * np.cos(orbit_theta)
    y = orbit_radius * np.sin(orbit_theta)
    z = np.zeros_like(x)
    ax.plot(x, y, z, label=planet)

ax.set_xlabel("Distance (AU)")
ax.set_ylabel("Distance (AU)")
ax.set_zlabel("Distance (AU)")
ax.set_title("Solar System")

ax.legend()

plt.grid(True)
plt.show()