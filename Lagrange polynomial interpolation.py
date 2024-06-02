import matplotlib.pyplot as plt
import numpy as np
def lagrange_interpolation(points, x):
    """
    Menghitung nilai interpolasi Lagrange pada titik x.
    
    Parameters:
    points (list of tuple): Daftar titik (x, y).
    x (float): Nilai x yang ingin diinterpolasi.
    
    Returns:
    float: Nilai interpolasi pada titik x.
    """
    # variabel untuk menyimpan hasil akhir dari interpolasi
    total = 0.0
    # variabel untuk menyimpan jumlah titik dalam points
    n = len(points)
    # looping I, untuk tiap titik xi, yi dalam points
    for i in range(n):
        # menyimpan nilai x dan y dari titik ke-i
        xi, yi = points[i]
        # menyimpan nilai yi untuk nanti dikalikan
        term = yi

        # looping II, untuk tiap titik xj, yj dalam daftar points, kecuali jika i dan j sama
        for j in range(n):
            if i != j:
                # mendapatkan nilai x dari titik j ke dalam variabel xj
                xj, _ = points[j]
                term *= (x - xj) / (xi - xj)
        print(f"a{i}L{i} = {term:.5f}")
        total += term
    
    return total, i, n

# Contoh penggunaan fungsi lagrange_interpolation
points = [(1, 1.5709), (4, 1.5727), (6, 1.5751)]
x = 3.5
interpolated_value, i, n = lagrange_interpolation(points, x)
print(f"P{i}({x}) = {interpolated_value:.5f}")
print(f"Jadi nilai interpolasi pada x = {x} yaitu {interpolated_value:.5f}")

