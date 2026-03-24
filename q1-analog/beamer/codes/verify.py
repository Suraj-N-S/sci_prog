
import numpy as np

# ── Given ─────────────────────────────────────────────────────
Vin_amp = 5.0       # Bipolar square wave amplitude (V), i.e. ±5 V
f       = 50        # Hz
T       = 1.0 / f   # Period = 20 ms
R1      = 10**4      # Integrator input resistor = 10 kΩ  (Ω)
R_in2   = 10**3       # Stage-2 input resistor    =  1 kΩ  (Ω)


# ── Analysis ──────────────────────────────────────────────────
# During the +5V half-cycle, integrator ramps DOWN by delta.
# During the −5V half-cycle, integrator ramps UP by delta.
# Net peak-to-peak at Stage-1 output = delta (one half-swing). 

r_c = (5*2*R1)/(Vin_amp*T) 

r_c = r_c / 10**6

print(f"The value of R/C = {r_c}")
