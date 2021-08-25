from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt
 x= [20, 21 , 23 , 24 , 25 , 27 , 29, 30]
 y = [346,362,343,339,347,346,339,394]
f = CubicSpline(x, y, bc_type='natural')
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
print("Number of Deaths on April 26 Using Direct Method Interpolation: ", f(26))