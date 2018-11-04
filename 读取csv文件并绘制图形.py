import numpy as np
import matplotlib.pyplot as plt
import  pandas as pd

num = 4288

x = np.linspace(1, num, num)

data = pd.read_csv("temp_log.csv", names=['value'])

print data
plt.plot(x, data.value)

# plt.ylim(0, 50)
plt.show()



#x=np.linspace(-np.pi,np.pi,256,endpoint=True)
#C,S=np.cos(x),np.sin(x)
#plt.plot(x,C)
#plt.plot(x,S)

#plt.plot(x,C,color='red',linewidth=2.5,linestyle='-')
#plt.plot(x,S,color='blue',linewidth=2.5,linestyle='-')
#plt.show()