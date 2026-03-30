import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def f(x, y):
    return x**2 + 2*y

def exact(x, C):
    return C * np.exp(2*x) - x**2/2 - x/2 - 0.25

x0, y0 = 0.0, 0.0
C = y0 + 0.25

x_span = (0.0, 2.0)
x_eval = np.linspace(0.0, 2.0, 500)

sol   = solve_ivp(f, x_span, [y0], method='RK45',
                  t_eval=x_eval, rtol=1e-8, atol=1e-10)
y_ex  = exact(x_eval, C)

plt.figure(figsize=(8, 5))
plt.plot(x_eval, y_ex,   'royalblue', lw=2.2, label='Solution')
plt.plot(sol.t,  sol.y[0], 'r--',    lw=1.6, label='RK-4 plot')
plt.xlabel('x'); plt.ylabel('y(x)')
plt.title(r"$\frac{dy}{dx} = x^2 + 2y,\quad y(0)=0$"
          "\n"
          r"$y = Ce^{2x} - \frac{x^2}{2} - \frac{x}{2} - \frac{1}{4},\quad C = 0.25$",
          fontsize=11)
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('rk4_plot.png', dpi=150)
plt.show()
print(f"Max error: {np.max(np.abs(sol.y[0] - exact(sol.t, C))):.2e}")
