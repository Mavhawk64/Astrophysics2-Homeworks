#!/usr/bin/env python3
# Courtesy of Ned Wright (www.astro.ucla.edu/~wright)
# Updated for Python 3

import sys
from math import *

try:
    if sys.argv[1] == "-h":
        print(
            """Cosmology calculator ala Ned Wright (www.astro.ucla.edu/~wright)
input values = redshift, Ho, Omega_m, Omega_vac
output values = age at z, distance in Mpc, kpc/arcsec, apparent to abs mag conversion

Options:   -h for this message
           -v for verbose response"""
        )
        sys.exit()

    verbose = 1 if sys.argv[1] == "-v" else 0
    length = len(sys.argv) - 1 if verbose else len(sys.argv)

    # Input handling
    if length == 2:
        z = float(sys.argv[1 + verbose])
        if z > 100:
            z /= 299790.0
        H0 = 75.0
        WM = 0.3
        WV = 1.0 - WM - 0.4165 / (H0 * H0)
    elif length == 3:
        z = float(sys.argv[1 + verbose])
        H0 = float(sys.argv[2 + verbose])
        WM = 0.3
        WV = 1.0 - WM - 0.4165 / (H0 * H0)
    elif length == 4:
        z = float(sys.argv[1 + verbose])
        H0 = float(sys.argv[2 + verbose])
        WM = float(sys.argv[3 + verbose])
        WV = 0.0
    elif length == 5:
        z = float(sys.argv[1 + verbose])
        H0 = float(sys.argv[2 + verbose])
        WM = float(sys.argv[3 + verbose])
        WV = float(sys.argv[4 + verbose])
    else:
        print("need some values or too many values")
        sys.exit(1)

    # Constants
    WR = 0.0
    WK = 0.0
    c = 299792.458
    Tyr = 977.8
    DTT = 0.5
    DTT_Gyr = 0.0
    age = 0.5
    age_Gyr = 0.0
    zage = 0.1
    zage_Gyr = 0.0
    DCMR = 0.0
    DCMR_Mpc = 0.0
    DCMR_Gyr = 0.0
    DA = 0.0
    DA_Mpc = 0.0
    DA_Gyr = 0.0
    kpc_DA = 0.0
    DL = 0.0
    DL_Mpc = 0.0
    DL_Gyr = 0.0
    V_Gpc = 0.0
    a = 1.0
    az = 1.0 / (1 + z)

    h = H0 / 100.0
    WR = 4.165e-5 / (h * h)
    WK = 1.0 - WM - WR - WV
    age = 0.0
    n = 1000

    for i in range(n):
        a = az * (i + 0.5) / n
        adot = sqrt(WK + (WM / a) + (WR / (a * a)) + (WV * a * a))
        age += 1.0 / adot

    zage = az * age / n
    zage_Gyr = (Tyr / H0) * zage
    DTT = 0.0
    DCMR = 0.0

    for i in range(n):
        a = az + (1 - az) * (i + 0.5) / n
        adot = sqrt(WK + (WM / a) + (WR / (a * a)) + (WV * a * a))
        DTT += 1.0 / adot
        DCMR += 1.0 / (a * adot)

    DTT = (1.0 - az) * DTT / n
    DCMR = (1.0 - az) * DCMR / n
    age = DTT + zage
    age_Gyr = age * (Tyr / H0)
    DTT_Gyr = (Tyr / H0) * DTT
    DCMR_Gyr = (Tyr / H0) * DCMR
    DCMR_Mpc = (c / H0) * DCMR

    ratio = 1.0
    x = sqrt(abs(WK)) * DCMR
    if x > 0.1:
        if WK > 0:
            ratio = 0.5 * (exp(x) - exp(-x)) / x
        else:
            ratio = sin(x) / x
    else:
        y = x * x
        if WK < 0:
            y = -y
        ratio = 1.0 + y / 6.0 + y * y / 120.0

    DCMT = ratio * DCMR
    DA = az * DCMT
    DA_Mpc = (c / H0) * DA
    kpc_DA = DA_Mpc / 206.264806
    DA_Gyr = (Tyr / H0) * DA
    DL = DA / (az * az)
    DL_Mpc = (c / H0) * DL
    DL_Gyr = (Tyr / H0) * DL

    x = sqrt(abs(WK)) * DCMR
    if x > 0.1:
        if WK > 0:
            ratio = (0.125 * (exp(2.0 * x) - exp(-2.0 * x)) - x / 2.0) / (
                x * x * x / 3.0
            )
        else:
            ratio = (x / 2.0 - sin(2.0 * x) / 4.0) / (x * x * x / 3.0)
    else:
        y = x * x
        if WK < 0:
            y = -y
        ratio = 1.0 + y / 5.0 + (2.0 / 105.0) * y * y

    VCM = ratio * DCMR * DCMR * DCMR / 3.0
    V_Gpc = 4.0 * pi * ((0.001 * c / H0) ** 3) * VCM

    if verbose == 1:
        print(
            f"For H_o = {H0:.1f}, Omega_M = {WM:.2f}, Omega_vac = {WV:.2f}, z = {z:.3f}"
        )
        print(f"It is now {age_Gyr:.1f} Gyr since the Big Bang.")
        print(f"The age at redshift z was {zage_Gyr:.1f} Gyr.")
        print(f"The light travel time was {DTT_Gyr:.1f} Gyr.")
        print(
            f"The comoving radial distance is {DCMR_Mpc:.1f} Mpc or {DCMR_Gyr:.1f} Gly."
        )
        print(f"The comoving volume within redshift z is {V_Gpc:.1f} Gpc^3.")
        print(f"The angular size distance D_A is {DA_Mpc:.1f} Mpc or {DA_Gyr:.1f} Gly.")
        print(f'This gives a scale of {kpc_DA:.2f} kpc/".')
        print(f"The luminosity distance D_L is {DL_Mpc:.1f} Mpc or {DL_Gyr:.1f} Gly.")
        print(f"The distance modulus, m-M, is {5 * log10(DL_Mpc * 1e6) - 5:.2f}")
    else:
        print(
            f"{zage_Gyr:.2f} {DCMR_Mpc:.2f} {kpc_DA:.2f} {5 * log10(DL_Mpc * 1e6) - 5:.2f}"
        )

except IndexError:
    print("need some values or too many values")
    sys.exit(1)
except ValueError:
    print("nonsense value or option")
    sys.exit(1)
