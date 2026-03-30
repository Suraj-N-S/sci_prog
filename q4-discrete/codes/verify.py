import sympy as sp

x = sp.Symbol('x')
C = sp.Symbol('C')
k = sp.Symbol('k')

print("=" * 60)
print("  Problem 1.2.70  --  dy/dx = x^2 + 2y")
print("  Symbolic Verification using SymPy")
print("=" * 60)

# ── 1. General solution from integrating factor method ─────────
y_gen = C*sp.exp(2*x) - x**2/2 - x/2 - sp.Rational(1, 4)
dydx  = sp.diff(y_gen, x)
res   = sp.simplify(dydx - 2*y_gen - x**2)
print(f"\nGeneral solution: y = {y_gen}")
print(f"dy/dx - 2y - x^2 = {res}  (should be 0)")
print(f"Verified: {res == 0}")

# ── 2. Verify each option ──────────────────────────────────────
print("\n" + "-"*60)
print("Checking all four options by substitution:")
print("-"*60)

options = {
    '(a) y = (2/3)x^2 + 4x':
        sp.Rational(2,3)*x**2 + 4*x,
    '(b) y = sqrt(2/3 x^2 + 4x + k)':
        sp.sqrt(sp.Rational(2,3)*x**2 + 4*x + k),
    '(c) y = (2/3)x^3 - 4x + k':
        sp.Rational(2,3)*x**3 - 4*x + k,
    '(d) y = (2/3)x^3 + 4x + k':
        sp.Rational(2,3)*x**3 + 4*x + k,
}

for label, y_opt in options.items():
    try:
        dydx_opt = sp.diff(y_opt, x)
        res_opt  = sp.simplify(dydx_opt - 2*y_opt - x**2)
        satisfies = sp.simplify(res_opt) == 0
        print(f"\n  {label}")
        print(f"    dy/dx - 2y - x^2 = {res_opt}")
        print(f"    Satisfies ODE    : {satisfies}")
    except Exception as e:
        print(f"\n  {label}  --  Error: {e}")

# ── 3. SymPy dsolve confirmation ───────────────────────────────
print("\n" + "-"*60)
print("SymPy dsolve (direct ODE solver):")
y_func = sp.Function('y')
ode    = sp.Eq(y_func(x).diff(x) - 2*y_func(x), x**2)
sol    = sp.dsolve(ode, y_func(x))
print(f"  Solution: {sol}")

# ── 4. Laplace transform confirmation ─────────────────────────
print("\n" + "-"*60)
print("Laplace Transform partial fractions:")
s = sp.Symbol('s')
F = 2 / (s**3 * (s - 2))
pf = sp.apart(F, s)
print(f"  2 / [s^3(s-2)] = {pf}")

print("\n" + "="*60)
print("  CONCLUSION: General solution is")
print("  y = C*exp(2x) - x^2/2 - x/2 - 1/4")
print("  None of options (a)-(d) satisfy the ODE.")
print("="*60)
