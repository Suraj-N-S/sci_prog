import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy import signal
from scipy.fft import rfft, rfftfreq

# Parameters 
Vp  = 5.0          # square wave amplitude (V)
f0  = 50           # fundamental frequency (Hz)
T   = 1.0 / f0     # period = 20 ms
w0  = 2*np.pi*f0   # angular frequency
R1  = 10e3         # integrator input resistor (10 kOhm)
C   = 1e-6         # capacitor (1 uF)
H2  = 1.0          # Stage-2 gain (1kOhm / 1kOhm = 1)
N_h = 51           # number of odd harmonics

# Time vector
Fs  = 200000       # sampling frequency (Hz)
t   = np.arange(0, 4*T, 1/Fs)

# square wave 
Vin_exact = Vp * signal.square(2*np.pi*f0*t)

# Fourier series reconstruction 
# Input:  V_in(t) = sum  4Vp/(n*pi) * sin(n*w0*t)   [odd n]
# Output: V_out(t)= sum -4Vp*H1*H2/(n*pi) * cos(n*w0*t)
#         where |H1(jnw0)| = 1/(n*w0*R1*C),  phase H1 = +90
#         H2 = -1  =>  total phase = +90-180 = -90  =>  -cos
Vin_fs  = np.zeros_like(t)
Vout_fs = np.zeros_like(t)
for k in range(N_h):
    n      = 2*k + 1
    bn     = 4*Vp / (n*np.pi)
    H1_mag = 1.0  / (n*w0*R1*C)
    A_out  = H1_mag * H2 * bn
    Vin_fs  +=  bn    * np.sin(n*w0*t)        # input harmonics
    Vout_fs += -A_out * np.cos(n*w0*t)        # output: -cos (phase=-90)


#Figure
fig = plt.figure(figsize=(14, 11))
gs  = gridspec.GridSpec(2, 1, hspace=0.55, wspace=0.35)
t_ms = t * 1e3
mask = t > T
Vpp  = Vout_fs[mask].max() - Vout_fs[mask].min()

# input waveform
ax0 = fig.add_subplot(gs[0])
ax0.plot(t_ms, Vin_exact, 'royalblue', lw=1.5)
ax0.plot(t_ms, Vin_fs,    'orange',    lw=1.2, ls='--',
         label=f'Fourier series ({N_h} harmonics)')
ax0.set_title('Input Square Wave (±5 V, 50 Hz)', fontsize=10, fontweight='bold')
ax0.set_ylabel('Voltage (V)'); ax0.set_xlabel('Time (ms)')
ax0.legend(fontsize=8); ax0.grid(alpha=0.3)
ax0.set_xlim(0, 4*T*1e3)

# output waveform
ax1 = fig.add_subplot(gs[1])
ax1.plot(t_ms, Vout_fs, 'crimson', lw=1.8)
ax1.axhline(0, color='k', lw=0.5, ls='--')
ax1.set_title(f'Output Triangular Wave  (Vpp = 5 V, 50 Hz)',
              fontsize=10, fontweight='bold')
ax1.set_ylabel('Voltage (V)'); ax1.set_xlabel('Time (ms)')
ax1.grid(alpha=0.3); ax1.set_xlim(0, 4*T*1e3)


fig.suptitle(
    r'Problem 1.1.56 — Fourier Series Analysis   '
    r'($R_1=10\,\mathrm{k}\Omega,\ R=1\,\mathrm{k}\Omega,\ C=1\,\mu\mathrm{F},\ RC=1$)',
    fontsize=13, fontweight='bold')

plt.savefig('fourier_plot_1156.png', dpi=150, bbox_inches='tight')
plt.show()
print(f'Output Vpp = {Vpp:.4f} V  (target: 5.0000 V)')
print(f'Condition met: {abs(Vpp-5.0) < 0.05}')
