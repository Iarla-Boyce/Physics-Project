import numpy as np
import matplotlib.pyplot as plt
f = open('masses.txt' , 'r')
f.readline()
radius=[]
deltaradius=[]
mass=[]
darkmatter=[]
combined=[]

for line in f:
  radius.append(float(line.split('\t')[0]))
  deltaradius.append(float(line.split('\t')[2]))
  mass.append(float(line.split('\t')[4]))
  combined.append(float(line.split('\t')[5]))
  darkmatter.append(float(line.split('\t')[6]))

  
x=np.array(radius)
y=np.array(mass)
z=np.array(darkmatter)
q=np.array(combined)

plt.plot(x,y)
plt.plot(x,z)
plt.plot(x,q)
plt.xlabel('Radius(kpc)')
plt.ylabel('Mass(kg)')
plt.show()
