import numpy as np
x = np.array([20,21,23,24,25,27,29,30])
y = np.array([346,362,343,339,347,346,339,394])
def newtonDivDiffInter(x, y):
""" Creates NDD pyramid and extracts coeffs """
    n = np.shape(y)[0]
    pyramid = np.zeros([n, n])
    pyramid[::,0] = y 
    for j in range(1,n):
        for i in range(n-j):

            pyramid[i][j] = (pyramid[i+1][j-1] - pyramid[i][j-1]) / (x[i+j] - x[i])
    return pyramid[0]
covector = newtonDivDiffInter(x, y)
print("Resulting divided diference are : (b0,b1,b2…)")
print (covector)
final_pol = np.polynomial.Polynomial([0.])
n = covector.shape[0]
 for i in range(n):
    p = np.polynomial.Polynomial([1.])

    for j in range(i):

        p_temp = np. polynomial. Polynomial([-x[j], 1.])
        p = np.polymul(p, p_temp)
    p *= covector[i]
    final_pol = np.polyadd(final_pol, p)
p = np.flip(final_pol[0]. coef, axis=0)
print("Resulting polynomial coefficients are : (a0,a1,a2…)")
print(p)
import matplotlib. pyplot as plt
x_axis = np.linspace(20, 30, num=5000)
y_axis = np.polyval(p, x_axis)
print()
print("Plot of Resulting Polynomial: ")
plt.figure(figsize = (30,8))
plt.subplot(133)
plt.plot(x_axis, y_axis, 'r')

plt.title("Number of Deaths of Days April")
plt.xlabel("Days")
plt.ylabel("Deaths")
plt.grid()
plt.show()
print()
print("Number of Deaths on April 26 Using Newton's Divided Difference Interpolation: "
, np.polyval(p,26))