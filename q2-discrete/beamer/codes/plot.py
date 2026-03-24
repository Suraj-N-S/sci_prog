import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return 1.0 / (1.0 + x**2)

x = 0.5
iterates = [x]
tol = 1e-10
max_iter = 50

for i in range(max_iter):
    x_new = g(x)
    iterates.append(x_new)
    if abs(x_new - x) < tol:
        print(f"Converged at iteration {i+1}")
        break
    x = x_new

x_star = iterates[-1]
print(f"Converged value: {x_star:.10f}")

n_vals = list(range(len(iterates)))

plt.figure(figsize=(9, 5))
plt.plot(n_vals, iterates, 'bo-', markersize=6, linewidth=1.5, label=r'$x_n$')
plt.axhline(y=x_star, color='r', linestyle='--', linewidth=1.5,
            label=f'$x^* \\approx {x_star:.4f}$')
plt.xlabel('Iteration $n$', fontsize=13)
plt.ylabel('$x_n$', fontsize=13)
plt.title(r'Convergence of $x_{n+1} = \dfrac{1}{1+x_n^2}$, $x_0 = 0.5$', fontsize=13)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.savefig('convergence_plot.png', dpi=150)
print("Plot saved as convergence_plot.png")
plt.show()
