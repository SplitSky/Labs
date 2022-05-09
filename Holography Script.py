import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def fit_function(x, A, B, C):
    return A + B * x + C * x ** 2


y1 = [76.5, 75, 74, 73.1, 71.5, 69.4, 69.7, 68.3, 67.6, 67.1, 66.6, 65.1, 64.3, 63.7, 63.1, 61.7, 61.6, 60.5, 59.2,
      59.7, 59, 58, 56, 54.8, 56.5, 55.1, 54.5, 53.6, 52.4]
x1 = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5,
      11.0, 11.5, 12.0, 13.0, 13.5, 14.0, 14.5]
y2 = [94.5, 90.9, 89.4, 86.6, 86.9, 85.4, 82.8, 80.5, 81.9, 80.7, 79.7, 79.3, 77.3, 76.5, 75.4, 74.3, 73.4, 72.1, 71.6,
      70.5, 69.6, 68.9, 68.0, 66.1, 65.2, 64.6, 63.7, 63.2, 62.3, 61.6, 61.0, 60.4, 59.6, 58.7, 57.8, 57.6, 56.8, 56.2,
      55.5, 55.0, 54.3]
x2 = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5,
      11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0]

x1 = np.array(x1)
y1 = np.array(y1)
y2 = np.array(y2)
x2 = np.array(x2)
x1 += 7

thing1 = np.vstack((x1, y1))
thing2 = np.vstack((x2, y2))
full_data = np.hstack((thing1, thing2))
sorted_data = full_data[:, full_data[0].argsort()]

x = sorted_data[0]
y = sorted_data[1]

popt, pcov = curve_fit(fit_function, x, y)
xspace = np.linspace(0, 25, 10000)
plt.plot(xspace, fit_function(xspace, *popt), label="Fitted Function")
error = (y/y) * 0.5
plt.errorbar(x, y, yerr=error, fmt="+", label="Cooling Curve", capsize=3)
print("Equation is: ")
A = popt[0]
B = popt[1]
C = popt[2]
print("{:04.3f} + {:04.3f}x + {:04.3f}x^2".format(A, B, C))
# plt.scatter(x, y, label="Cooling Curve", marker="+")
plt.legend()
plt.xlabel(r'Time/ min')
plt.ylabel(r'Temperature/ C')
plt.title("The Cooling curve")
plt.show()
