import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ODE: dy/dx = x^2 + 2y
def f(x, y):
    return x**2 + 2*y

# Exact general solution: y = C*exp(2x) - x^2/2 - x/2 - 1/4
# With y(0) = 0 => C = 0.25
def exact(x):
    return 0.25 * np.exp(2*x) - x**2/2 - x/2 - 0.25

x_eval = np.linspace(0.0, 2.0, 500)

# RK-4 solution (y(0) = 0)
sol = solve_ivp(f, (0.0, 2.0), [0.0], method='RK45',
                t_eval=x_eval, rtol=1e-8, atol=1e-10)

# Option functions (k=0 chosen for plotting)
k = 0
opt_a = (2/3)*x_eval**2 + 4*x_eval
opt_b = np.sqrt(np.abs((2/3)*x_eval**2 + 4*x_eval + k))
opt_c = (2/3)*x_eval**3 - 4*x_eval + k
opt_d = (2/3)*x_eval**3 + 4*x_eval + k

plt.figure(figsize=(9, 6))

plt.plot(x_eval, exact(x_eval),  'k',   lw=2.5, label=r'Solution: $y=Ce^{2x}-\frac{x^2}{2}-\frac{x}{2}-\frac{1}{4}$')
plt.plot(sol.t,  sol.y[0],       'k--', lw=1.4, label='RK-4 numerical ($y(0)=0$)')
plt.plot(x_eval, opt_a, 'royalblue',  lw=1.8, ls='-.',  label=r'(a) $y=\frac{2}{3}x^2+4x$')
plt.plot(x_eval, opt_b, 'seagreen',   lw=1.8, ls='-.',  label=r'(b) $y=\sqrt{\frac{2}{3}x^2+4x+k}$')
plt.plot(x_eval, opt_c, 'orange',     lw=1.8, ls='-.',  label=r'(c) $y=\frac{2}{3}x^3-4x+k$')
plt.plot(x_eval, opt_d, 'crimson',    lw=1.8, ls='-.',  label=r'(d) $y=\frac{2}{3}x^3+4x+k$')

plt.xlabel('x', fontsize=12)
plt.ylabel('y(x)', fontsize=12)
plt.title(r'Problem 1.2.70 -- $\frac{dy}{dx} = x^2 + 2y$'
          '\nAll options vs correct solution (RK-4, $y(0)=0$, $k=0$)',
          fontsize=11)
plt.legend(fontsize=8.5, loc='upper left')
plt.ylim(-10, 30)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('rk4_options.png', dpi=150)
plt.show()
