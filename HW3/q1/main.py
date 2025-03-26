m_p = 1.007276  # amu
m_n = 1.008665  # amu
m_e = 0.00054858  # amu

# Part (a) --> Binding Energy of 8-Oxygen-16, 10-Neon-20, 28-Nickel-56
print("Part (a)")
M = [15.9949146, 19.9924402, 55.9421363]  # amu
N = Z = [8, 10, 28]
E_b = [
    1 / (N[i] + Z[i]) * (N[i] * m_n + Z[i] * (m_p + m_e) - M[i]) * 931.5
    for i in range(3)
]  # MeV/nucleon
print([f"{e:.2f} MeV/nucleon" for e in E_b])

# Part (b) --> Amount of 28-Nickel-56 required for 10^51 erg of energy
print("Part (b)")
E = 1e51  # erg
dE = E_b[2] - (2 * E_b[1] + E_b[0]) / 3  # MeV/nucleon
print(f"\\Delta E = {dE:.2f} MeV/nucleon")

AdE = dE * (N[2] + Z[2])
print(f"A_{{Ni}}\\Delta E = {AdE:.2f} MeV")
AdE *= 1.602e-6  # MeV to erg
print(f"A_{{Ni}}\\Delta E = {AdE:.2e} erg")

n = E / AdE
print(f"n = {n:.2e} Ni nuclei")

g = n * 56 * 1.66e-24  # g
print(f"or {g:.2e} g of Ni")

s = g / 2e33  # solar masses
print(f"or {s:.2f} M_\\odot of Ni")
