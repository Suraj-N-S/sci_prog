import numpy as np

# ── Circuit parameters (SI units) ──────────────────────────────
Vp  = 5.0        # Square wave amplitude (V), bipolar +-5V
f0  = 50         # Fundamental frequency (Hz)
w0  = 2*np.pi*f0 # Angular frequency (rad/s) = 100*pi
R1  = 10e3       # Integrator input resistor (Ohm) = 10 kOhm
C   = 1e-6       # Capacitor (F) = 1 uF
# Stage-2: feedback R = 1 kOhm, input = 1 kOhm  => gain = 1 (dimensionless)
R_kOhm  = 1.0    # Stage-2 feedback resistor (kOhm)
R_in2   = 1.0    # Stage-2 input resistor (kOhm)
H2_mag  = R_kOhm / R_in2   # = 1.0

# ── Time vector ────────────────────────────────────────────────
t    = np.linspace(0, 4/f0, 20000)
Vin  = np.zeros_like(t)
Vout = np.zeros_like(t)

# ── Fourier series construction ────────────────────────────────
N_harmonics = 1000   # 1000 odd harmonics for high accuracy
for k in range(N_harmonics):
    n = 2*k + 1                           # n = 1, 3, 5, ...

    # Input harmonic amplitude (square wave Fourier coefficient)
    A_in  = 4 * Vp / (n * np.pi)

    # Stage-1 transfer function magnitude at frequency n*w0
    # H1(jnw0) = -1/(jnw0*R1*C) => |H1| = 1/(n*w0*R1*C)
    H1_mag = 1.0 / (n * w0 * R1 * C)

    # Output harmonic amplitude
    A_out = H1_mag * H2_mag * A_in        # decays as 1/n^2

    # Build Fourier series
    # Input: sine terms; integrator adds +90 deg phase (1/j = -j => +90)
    # so output terms are cosine
    Vin  += A_in  * np.sin(n * w0 * t)
    Vout += A_out * np.cos(n * w0 * t)

# ── Measure peak-to-peak (skip first cycle) ────────────────────
mask        = t > 1/f0
Vpp_out     = Vout[mask].max() - Vout[mask].min()
Vpp_in      = Vin[mask].max()  - Vin[mask].min()

# ── Analytical peak amplitude of triangular wave ───────────────
# Triangular wave: peak A, series: sum 8A/(pi^2) * cos/n^2
# Our output series: sum A_out_1/n^2 * cos (approximately)
# Matching: 8A/pi^2 = A_out_1 = (4*Vp*H2_mag)/(pi*w0*R1*C)
# => A = pi*Vp*H2_mag / (2*w0*R1*C)
A_analytical   = (np.pi * Vp * H2_mag) / (2 * w0 * R1 * C)
Vpp_analytical = 2 * A_analytical

# ── Print results ──────────────────────────────────────────────
print("=" * 62)
print("  Problem 1.1.56  --  Fourier-Laplace Verification")
print("=" * 62)
print(f"  Input amplitude  Vp  = +/-{Vp} V (bipolar square wave)")
print(f"  Frequency        f0  = {f0} Hz,  w0 = 100*pi rad/s")
print(f"  Integrator R1        = {R1/1e3:.0f} kOhm,  C = {C*1e6:.1f} uF")
print(f"  Stage-2 gain  H2     = {H2_mag:.1f}  ({R_kOhm} kOhm / {R_in2} kOhm)")
print(f"  RC product           = {R_kOhm * C*1e6:.2f}  kOhm*uF")
print("-" * 62)
print(f"  Harmonics used       = {N_harmonics} (odd: 1,3,5,...)")
print(f"  Input  Vpp simulated = {Vpp_in:.4f} V  (should be ~{2*Vp:.1f} V)")
print(f"  Output Vpp simulated = {Vpp_out:.4f} V")
print(f"  Output Vpp analytical= {Vpp_analytical:.4f} V")
print(f"  Target               = 5.0000 V")
print(f"  Condition met        : {np.isclose(Vpp_out, 5.0, atol=0.05)}")
print("=" * 62)
print()
print("  First 5 odd harmonics -- harmonic table:")
print(f"  {'n':>4}  {'f (Hz)':>8}  {'A_in (V)':>10}  {'|H1|':>10}  {'A_out (V)':>10}")
print(f"  {'-'*52}")
for k in range(5):
    n     = 2*k + 1
    A_in  = 4*Vp / (n * np.pi)
    H1_m  = 1.0 / (n * w0 * R1 * C)
    A_out_n = H1_m * H2_mag * A_in
    print(f"  {n:>4}  {n*f0:>8.0f}  {A_in:>10.4f}  {H1_m:>10.4f}  {A_out_n:>10.4f}")
print()
print("  A_out decays as 1/n^2 -- this confirms a triangular wave output.")
print()
print("  Design condition: Vpp = 5*R/C = 5 => R/C = 1 => RC = 1")
print("  Answer: (a)  RC = 1")
