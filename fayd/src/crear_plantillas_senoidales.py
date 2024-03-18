import numpy as np
import matplotlib.pyplot as plt

SR = 100
T  = 7.5
N  = SR*T
t  = np.arange(N)/SR


s1 = np.sin(2*np.pi*t)
s2 = np.sin(2*np.pi*t/2)
s3 = np.sin(2*np.pi*t/3)

plt.figure(figsize=(12,6))
plt.plot(t, s1, linewidth=3)

plt.figure(figsize=(12,6))
plt.plot(t, s2, linewidth=3)

plt.figure(figsize=(12,6))
plt.plot(t, s3, linewidth=3)

plt.figure(figsize=(12,6))
plt.plot(t, s1+s2, linewidth=3)
plt.show()
