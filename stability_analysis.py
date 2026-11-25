import numpy as np

# Function to convert magnitude and angle to complex number
def polar_to_complex(mag, ang_deg):
    return mag * np.exp(1j * np.deg2rad(ang_deg))

# Function to calculate stability parameters
def stability_factors(S11, S12, S21, S22):
    delta = S11 * S22 - S12 * S21
    K = (1 - abs(S11)**2 - abs(S22)**2 + abs(delta)**2) / (2 * abs(S12 * S21))
    return K, delta

# Function to calculate stability circles
def stability_circles(S11, S12, S21, S22, delta):
    C_s = np.conj(S11 - delta * np.conj(S22)) / (abs(S11)**2 - abs(delta)**2)
    R_s = abs(S12 * S21) / (abs(S11)**2 - abs(delta)**2)
    C_L = np.conj(S22 - delta * np.conj(S11)) / (abs(S22)**2 - abs(delta)**2)
    R_L = abs(S12 * S21) / (abs(S22)**2 - abs(delta)**2)
    return C_s, R_s, C_L, R_L

# Function to calculate Γs, ΓL and maximum gain
def max_gain(S11, S12, S21, S22, K, delta):
    if K <= 1 or abs(delta) >= 1:
        return None, None, None

    B1 = 1 + abs(S11)**2 - abs(S22)**2 - abs(delta)**2
    B2 = 1 + abs(S22)**2 - abs(S11)**2 - abs(delta)**2
    C1 = S11 - delta * np.conj(S22)
    C2 = S22 - delta * np.conj(S11)

    ΓS = (B1 - np.sqrt(B1**2 - 4 * abs(C1)**2)) / (2 * C1)
    ΓL = (B2 - np.sqrt(B2**2 - 4 * abs(C2)**2)) / (2 * C2)

    Gmax = abs(S21 / S12) * (K - np.sqrt(K**2 - 1))
    Gmax_dB = 20 * np.log10(Gmax)
    return ΓS, ΓL, Gmax_dB

# Given S-parameter data
data = [
    [2.50, 0.521, -92.0, 4.923, 96.8, 0.073, 45.0, 0.690, -41.8],
    [3.20, 0.406, -115.8, 4.231, 81.0, 0.078, 42.2, 0.614, -48.5],
    [4.50, 0.310, -159.4, 3.415, 57.3, 0.089, 40.8, 0.534, -60.3]
]

# Display results
for f, s11m, s11a, s21m, s21a, s12m, s12a, s22m, s22a in data:
    S11 = polar_to_complex(s11m, s11a)
    S21 = polar_to_complex(s21m, s21a)
    S12 = polar_to_complex(s12m, s12a)
    S22 = polar_to_complex(s22m, s22a)

    K, delta = stability_factors(S11, S12, S21, S22)
    C_s, R_s, C_L, R_L = stability_circles(S11, S12, S21, S22, delta)

    print(f"\nFrequency = {f} GHz")
    print(f"K = {K:.3f}, |Δ| = {abs(delta):.3f}")
    print(f"C_s = {C_s:.4f}, R_s = {R_s:.4f}")
    print(f"C_L = {C_L:.4f}, R_L = {R_L:.4f}")

    if K > 1 and abs(delta) < 1:
        ΓS, ΓL, Gmax_dB = max_gain(S11, S12, S21, S22, K, delta)
        print("→ Transistor is Unconditionally Stable")
        print(f"ΓS = {ΓS:.4f}, ΓL = {ΓL:.4f}")
        print(f"Maximum Gain = {Gmax_dB:.2f} dB")
    else:
        print("→ Transistor is Conditionally Stable")
