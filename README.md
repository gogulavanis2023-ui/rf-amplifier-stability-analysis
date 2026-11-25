# RF Transistor Amplifier Stability and Maximum-Gain Analysis

A Python tool that takes measured transistor S-parameters at several frequencies and works through the standard microwave amplifier design checks:

- **Rollett stability factor** `K` and `|Δ|` (K-Δ test for unconditional stability)
- **Source and load stability circles** (centres `C_s`, `C_L` and radii `R_s`, `R_L`)
- For unconditionally stable cases: **simultaneous conjugate-match reflection coefficients** Γ_S and Γ_L, and the **maximum available gain** G_max in dB

## Input data
The S-parameters are hard-coded as magnitude/angle at 2.5, 3.2 and 4.5 GHz:
`[f_GHz, |S11|, ∠S11, |S21|, ∠S21, |S12|, ∠S12, |S22|, ∠S22]`. Edit the `data` list to analyse another device.

## Run
```bash
pip install numpy
python stability_analysis.py
```
For each frequency it prints K, |Δ|, both stability circles, and either the conjugate-match Γ_S/Γ_L with G_max (unconditionally stable) or a "conditionally stable" warning.

## Equations used
- Δ = S11·S22 − S12·S21, K = (1 − |S11|² − |S22|² + |Δ|²) / (2|S12·S21|)
- C_S = (S11 − Δ·S22\*)\* / (|S11|² − |Δ|²), R_S = |S12·S21| / ||S11|² − |Δ|²| (and similarly for the load)
- G_max = |S21/S12| · (K − √(K² − 1))

## Future improvements
Read Touchstone `.s2p` files, plot the circles on a Smith chart (scikit-rf / matplotlib), and add constant-gain and noise-figure circles.

## Technologies
`Python` `NumPy` `RF / microwave engineering` `S-parameters` `Amplifier design`
