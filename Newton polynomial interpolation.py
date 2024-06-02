import matplotlib.pyplot as plt
import numpy as np

def divided_difference(x, y):
    """
    Menghitung selisih terbagi untuk interpolasi polinomial Newton.
    
    Parameters:
    x (list): Daftar nilai x.
    y (list): Daftar nilai y.
    
    Returns:
    list: Selisih terbagi.
    """
    n = len(x)
    coefficients = np.copy(y)
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coefficients[i] = (coefficients[i] - coefficients[i-1]) / (x[i] - x[i-j])
    return coefficients

def newton_interpolation(x, y, xi):
    """
    Menghitung nilai interpolasi polinomial Newton pada titik xi.
    
    Parameters:
    x (list): Daftar nilai x.
    y (list): Daftar nilai y.
    xi (float): Nilai x yang ingin diinterpolasi.
    
    Returns:
    float: Nilai interpolasi pada titik xi.
    """
    coefficients = divided_difference(x, y)
    n = len(x)
    result = coefficients[0]
    for i in range(1, n):
        term = coefficients[i]
        for j in range(i):
            term *= (xi - x[j])
        result += term
    return result

# Contoh penggunaan fungsi newton_interpolation
points = [(1, 1.5709), (4, 1.5727), (6, 1.5751)]
x_values, y_values = zip(*points)
x = 3.5
interpolated_value = newton_interpolation(x_values, y_values, x)
print(f"P({x}) = {interpolated_value:.5f}")
print(f"Jadi nilai interpolasi pada x = {x} yaitu {interpolated_value:.5f}")