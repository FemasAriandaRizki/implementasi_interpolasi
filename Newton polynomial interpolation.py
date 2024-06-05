# Nama    : Femas Arianda Rizki
# NIM     : 21120122130080
# Kelas   : Metode Numerik - B

# Kode Sumber
import numpy as np
import matplotlib.pyplot as plt

def newton_interpolation(points, x):
    """
    Menghitung nilai interpolasi Newton pada titik x.
    
    Parameters:
    points (list of tuple): Daftar titik (x, y).
    x (float): Nilai x yang ingin diinterpolasi.
    
    Returns:
    float: Nilai interpolasi pada titik x.
    """
    n = len(points)
    # Membuat tabel selisih terbagi
    divided_diff = np.zeros((n, n))
    # Memasukkan nilai y ke kolom pertama dari tabel selisih terbagi
    for i in range(n):
        divided_diff[i][0] = points[i][1]

    # Menghitung selisih terbagi
    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i][j] = (divided_diff[i+1][j-1] - divided_diff[i][j-1]) / (points[i+j][0] - points[i][0])
    
    # Menghitung nilai interpolasi pada x
    result = divided_diff[0][0]
    product = 1.0
    for i in range(1, n):
        product *= (x - points[i-1][0])
        result += divided_diff[0][i] * product
    
    return result

# Kode Testing, contoh penyelesaian problem
points = [(5, 10), (10, 30), (15, 25), (20, 40), (25, 18), (30, 20), (35, 22), (40, 15)]
x = 33
interpolated_value = newton_interpolation(points, x)
print(f"P({x}) = {interpolated_value:.5f}")
print(f"Jadi nilai interpolasi pada x = {x} yaitu {interpolated_value:.5f}")

# Plot Grafik hasil interpolasi dengan 5 <= x <= 40
x_values = np.arange(5, 40.1, 0.1)
y_values = [newton_interpolation(points, x) for x in x_values]

plt.plot(x_values, y_values, "b")
plt.grid()
plt.xlim(0, 42)
plt.xlabel('x')
plt.ylabel('Interpolated y')
plt.title('Interpolasi Polinomial Newton')

plt.show()