# Nama    : Femas Arianda Rizki
# NIM     : 21120122130080
# Kelas   : Metode Numerik - B

# Kode Sumber
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
        total += term
    
    return total

# Kode Testing, contoh penyelesaian problem
points = [(5, 10), (10, 30), (15, 25), (20, 40), (25, 18), (30, 20), (35, 22), (40, 15)]
x = 33
interpolated_value = lagrange_interpolation(points, x)
print(f"P({x}) = {interpolated_value:.5f}")
print(f"Jadi nilai interpolasi pada x = {x} yaitu {interpolated_value:.5f}")

#  Plot Grafik hasil interpolasi dengan 5 <= x <= 40
x_values = np.arange(5, 40.1, 0.1)
y_values = [lagrange_interpolation(points, x) for x in x_values]

plt.plot(x_values, y_values, "r")
plt.grid()
plt.xlim(0, 42)

plt.show()