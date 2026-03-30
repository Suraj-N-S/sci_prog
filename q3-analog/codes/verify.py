import numpy as np
from scipy.integrate import quad
from sympy import symbols, integrate, exp, I, sin, pi, oo, And, Piecewise
from sympy import simplify, lambdify, re

print("=" * 55)
print("sympy -- symbolic Fourier Transform")
print("=" * 55)

t_s, w_s = symbols('t omega', real=True)

# Define x(t) symbolically
x_sym = Piecewise((1, And(t_s >= -1, t_s <= 1)), (0, True))

# Compute FT symbolically
Xw_sym = integrate(x_sym * exp(-I * w_s * t_s), (t_s, -oo, oo))
Xw_sym = simplify(Xw_sym)
print(f"\n  X(j*omega) = {Xw_sym}")

print("\n  Evaluating at option frequencies:")
for label, val in [("w = pi",    pi),
                   ("w = 2*pi",  2*pi),
                   ("w = 0.5pi", pi/2),
                   ("w = 1.5pi", 3*pi/2),
                   ("w = 0",     0)]:
    result = Xw_sym.subs(w_s, val)
    print(f"    {label:12s} -> X = {simplify(result)}")

print("\n" + "=" * 55)
print("scipy.integrate.quad -- numerical integration")
print("=" * 55)

def X_quad(w):
    """Compute X(jw) via direct numerical integration of x(t)e^{-jwt}"""
    if abs(w) < 1e-10:
        val, _ = quad(lambda t: 1.0, -1, 1)
        return val
    real_part, _ = quad(lambda t: np.cos(w * t), -1, 1)
    imag_part, _ = quad(lambda t: -np.sin(w * t), -1, 1)
    return complex(real_part, imag_part)

print("\n  Checking all four options:")
options = {
    "a) pi, 2pi"       : [np.pi,       2*np.pi],
    "b) 0.5pi, 1.5pi"  : [0.5*np.pi,   1.5*np.pi],
    "c) 0, pi"         : [0,            np.pi],
    "d) 2pi, 2.5pi"    : [2*np.pi,      2.5*np.pi],
}
for opt, freqs in options.items():
    vals = [abs(X_quad(w)) for w in freqs]
    is_zero = all(v < 1e-9 for v in vals)
    print(f"  {opt}: |X|={vals[0]:.6f}, {vals[1]:.6f}  -> zeros={is_zero}")

print("\n  Answer: option a) is the only pair where both |X(jw)| = 0")
