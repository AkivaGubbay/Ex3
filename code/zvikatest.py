from mpl_toolkits.mplot3d import  axes3d,Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from tkinter import *



fig = plt.figure()
ax = Axes3D(fig) #<-- Note the difference from your original code..

date1_Entry = Entry(None)
date1_Entry.pack()

#,antialiased=False
#cmap=cm.jet
plt.show()