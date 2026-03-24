def g(x):
    return 1.0 / (1.0 + x**2)

x = 0.5
tol = 1e-10
max_iter = 1000
x_new = x

for i in range(max_iter):
    x_new = g(x)
    print(f"The {i} iteration value is : {x_new}")
    if abs(x_new - x) < tol:
        print(f"Converged at iteration {i+1}")
        break
    x = x_new

print(f"Fixed point x* = {x_new:.10f}")
print(f"Rounded to 2 decimal places = {round(x_new, 2)}")

# Verification: solve x^3 + x - 1 = 0
import numpy as np
roots = np.roots([1, 0, 1, -1])
real_roots = [r.real for r in roots if abs(r.imag) < 1e-10]
print(f"Root of x^3+x-1=0 in (0,1): {real_roots[0]:.10f}")
