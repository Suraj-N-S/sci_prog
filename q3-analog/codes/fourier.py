import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 20                 # number of harmonics
T = 4                  # period
w0 = 2 * np.pi / T     # fundamental frequency

# Time axis
t = np.linspace(-6, 6, 2000)

# Fourier series approximation
x_fs = np.ones_like(t) * (2 / T) * 2   # a0/2 = 0.5

# Add cosine terms
for n in range(1, N + 1):
    an = (2 / (n * np.pi)) * np.sin(n * np.pi / 2)
    x_fs += an * np.cos(n * w0 * t)

# Plot only Fourier series
plt.figure(figsize=(10, 5))
plt.plot(t, x_fs, label=f'Fourier Series (N={N})', linewidth=2)

plt.title('Fourier Series Approximation')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

# Save figure
plt.savefig('fourier_series.png', dpi=300)

plt.show()
