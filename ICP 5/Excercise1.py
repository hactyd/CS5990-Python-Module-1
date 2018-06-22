import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([1,3,2,5,7,8,8,9,10,12])
ymean=np.mean(y)
xmean=np.mean(x)
number=np.sum((x - xmean) * (y - ymean))
den=np.sum(pow((x - xmean), 2))
slope= number / den
intercept= ymean - (slope * xmean)
print("slope",slope)
print("intercept",intercept)
value= (slope * x) + intercept
plt.plot(x,y)
plt.plot(x, value)
plt.show()
new_x = input("Enter new new x value:")
new_y = int(new_x) * slope + intercept
print(new_y)
