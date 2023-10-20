import numpy as np
import matplotlib.pyplot as plt
x = input()
y = input()
x = np.array(x)
y = np.array(x)
slope,intercept = np.polyfit(x,y,1)
print('slope = ',slope,'\ny - intercept = ',intercept)
plt.plot(x,y,'o')
plt.plot(x,slope*x+intercept)
