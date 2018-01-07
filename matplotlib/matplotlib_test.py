import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

plt.subplot(231)
plt.plot([0,1],[0,1])
plt.title("A strait line")
plt.xlabel("x value")
plt.ylabel("y value")

plt.subplot(232)
import matplotlib.image as mpimg
img = mpimg.imread('1.png')
plt.imshow(img)
plt.title("imshow")


#plt.savefig("demo.jpg")
plt.show()

