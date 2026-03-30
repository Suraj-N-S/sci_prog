import numpy as np
import matplotlib.pyplot as plt

# ── Analytical FT only ───────────────────────────────────────────
def X_analytical(w):
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(np.abs(w) < 1e-9, 2.0, 2*np.sin(w)/w)

w    = np.linspace(-5*np.pi, 5*np.pi, 8000)
Xw   = X_analytical(w)

# ── Figure ───────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 1, figsize=(11, 8))
fig.suptitle(
    r'Signal $x(t)$ and its Fourier Transform $X(j\omega)$',
    fontsize=14, fontweight='bold')

# Top: x(t) -- single rect pulse, no fill colour
t_disp  = np.linspace(-4, 4, 4000)
xt_disp = np.where(np.abs(t_disp) <= 1.0, 1.0, 0.0)

axes[0].plot(t_disp, xt_disp, 'b-', linewidth=2.5, label=r'$x(t)$')
axes[0].set_title('Signal $x(t)$', fontsize=13, fontweight='bold')
axes[0].set_xlabel('$t$', fontsize=12)
axes[0].set_ylabel('$x(t)$', fontsize=12)
axes[0].set_xlim(-4, 4)
axes[0].set_ylim(-0.25, 1.45)
axes[0].axhline(0, color='k', linewidth=0.8)
axes[0].set_xticks(range(-4, 5))
axes[0].legend(fontsize=12)
axes[0].grid(True, linestyle='--', alpha=0.6)

# Bottom: X(jw) -- clean single curve, no colour, zeros marked
axes[1].plot(w, Xw, 'b-', linewidth=2.0,
             label=r'$X(j\omega) = \dfrac{2\sin(\omega)}{\omega}$')
# Mark zeros at omega = n*pi (excluding 0)
n_vals = np.arange(-5, 6)
zero_points = n_vals * np.pi
zero_points = zero_points[n_vals != 0]  # exclude w = 0

axes[1].plot(zero_points, np.zeros_like(zero_points), 'ro', markersize=5, label='Zeros')
axes[1].plot(zero_points, np.zeros_like(zero_points), 'ro', markersize=5, label='Zeros')
axes[1].axhline(0, color='k', linewidth=0.8)
axes[1].axvline(0, color='k', linewidth=0.5, linestyle=':')

tick_vals   = [n*np.pi for n in range(-5, 6)]
tick_labels = [r'$-5\pi$', r'$-4\pi$', r'$-3\pi$', r'$-2\pi$',
               r'$-\pi$',  r'$0$',     r'$\pi$',   r'$2\pi$',
               r'$3\pi$',  r'$4\pi$',  r'$5\pi$']
axes[1].set_xticks(tick_vals)
axes[1].set_xticklabels(tick_labels, fontsize=10)
axes[1].set_xlim(-5*np.pi, 5*np.pi)
axes[1].set_title(
    r'Fourier Transform $X(j\omega) = \dfrac{2\sin(\omega)}{\omega}$',
    fontsize=13, fontweight='bold')
axes[1].set_xlabel(r'$\omega$  (rad/s)', fontsize=12)
axes[1].set_ylabel(r'$X(j\omega)$', fontsize=12)
axes[1].legend(fontsize=11, loc='upper right')
axes[1].grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.savefig('fourier_transform_plot.png', dpi=150, bbox_inches='tight')
print("Saved fourier_transform_plot.png")
