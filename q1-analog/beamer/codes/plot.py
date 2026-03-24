"""
plot_waveforms_1156.py  —  Problem 1.1.56 (GATE IN 2007)
Simulate and plot waveforms for the triangular wave generator.
Condition: RC = 1  (R = 1 kΩ, C = 1 µF)
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ── Parameters ────────────────────────────────────────────────
Vin_amp = 5.0    # Bipolar square wave amplitude (V)
f       = 50     # Hz
T       = 1 / f  # Period = 20 ms
R1      = 10e3   # Integrator input resistor (Ω) = 10 kΩ
C       = 1e-6   # Capacitor (F) = 1 µF
R2      = 1e3    # Stage-2 feedback resistor (Ω) = 1 kΩ
R_in2   = 1e3    # Stage-2 input resistor (Ω) = 1 kΩ
gain2   = R2 / R_in2  # = 1

dt = T / 2000
t  = np.arange(0, 4 * T, dt)

# ── Input: bipolar square wave ±5 V ───────────────────────────
Vin = Vin_amp * np.sign(np.sin(2 * np.pi * f * t))

# ── Stage 1: Inverting integrator (Euler) ─────────────────────
Vint = np.zeros(len(t))
for i in range(1, len(t)):
    Vint[i] = Vint[i - 1] - (Vin[i - 1] / (R1 * C)) * dt

# ── Stage 2: Inverting amplifier ──────────────────────────────
Vout = -gain2 * Vint

# ── Measure pp after settling ─────────────────────────────────
mask    = t > T
Vpp_out = Vout[mask].max() - Vout[mask].min()
Vpp_int = Vint[mask].max() - Vint[mask].min()

# ── Plot ──────────────────────────────────────────────────────
fig = plt.figure(figsize=(11, 8))
fig.suptitle(
    "Problem 1.1.56 — Triangular Wave Generator\n"
    r"$R_1 = 10\,\mathrm{k\Omega},\;\;R = 1\,\mathrm{k\Omega},\;\;"
    r"C = 1\,\mu\mathrm{F},\;\;R/C = 1$",
    fontsize=13, fontweight='bold'
)
gs   = gridspec.GridSpec(3, 1, hspace=0.55)
t_ms = t * 1e3

# ── Panel 1: Input ────────────────────────────────────────────
ax1 = fig.add_subplot(gs[0])
ax1.plot(t_ms, Vin, color='royalblue', lw=2.0)
ax1.set_title('Input — Square Wave (±5 V, 50 Hz)', fontsize=10)
ax1.set_ylabel('Voltage (V)')
ax1.set_ylim(-7, 7)
ax1.axhline(0, color='k', lw=0.6, ls='--')
ax1.grid(True, alpha=0.35)

# ── Panel 2: Integrator output ────────────────────────────────
ax2 = fig.add_subplot(gs[1])
ax2.plot(t_ms, Vint, color='seagreen', lw=2.0)
ax2.set_title(
    f'Stage 1 — Integrator Output (5 V)',
    fontsize=10
)
ax2.set_ylabel('Voltage (V)')
ax2.axhline(0, color='k', lw=0.6, ls='--')
ax2.grid(True, alpha=0.35)

# ── Panel 3: Final output ─────────────────────────────────────
ax3 = fig.add_subplot(gs[2])
ax3.plot(t_ms, Vout, color='crimson', lw=2.0)
ax3.set_title(
    f'Stage 2 — Output Triangular Wave (5 V, 50 Hz)',
    fontsize=10
)
ax3.set_ylabel('Voltage (V)')
ax3.set_xlabel('Time (ms)')
ax3.axhline(0, color='k', lw=0.6, ls='--')
ax3.grid(True, alpha=0.35)

# Annotate peak-to-peak arrow
y_max = Vout[mask].max()
y_min = Vout[mask].min()
x_ann = t_ms[mask][len(t_ms[mask])//3]
ax3.annotate('', xy=(x_ann, y_min), xytext=(x_ann, y_max),
             arrowprops=dict(arrowstyle='<->', color='darkred', lw=1.8))
ax3.text(x_ann + 1.5, (y_max + y_min) / 2,
         f'5 V', color='darkred', fontsize=9, va='center')

plt.savefig('waveforms.png', dpi=150, bbox_inches='tight')
plt.show()
print(f"\nOutput peak-to-peak  = {Vpp_out:.3f} V  (target: 5.000 V)")
print(f"Plot saved as 'waveforms_1156.png'")
