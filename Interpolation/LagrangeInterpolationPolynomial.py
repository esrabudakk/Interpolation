import numpy as np
import matplotlib.pyplot as plt
x = [20, 21 , 23 , 24 , 25 , 27 , 29, 30]
y = [346,362,343,339,347,346,339,394]
m = len(x)
n= m - 1
x_value = 26
y_value = 0
for i in range(n+1):
    p = 1
    for j in range(n+1):
        if j != i:
            p*= (x_value - ×[j])/(x[i] - ×[j])
    y_value += y[i]*p
print('Number of Deaths on April %.0f Using Lagrange Interpolation Polynomial : %.7f % (x_value, y_value))
print()
print("Plot of Resulting Polynomial: ")
plt.figure(figsize=(30,8))
plt.subplot(133)
plt.plot(x, y, 'r')
plt.title("Number of Deaths of Days April")
plt.xlabel("Days")
plt.ylabel("Deaths")
plt.grid()
plt.show()