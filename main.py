import numpy as np
import matplotlib.pyplot as plt
f = open('galaxy.txt' , 'r')
f.readline()
radius=[]
velocity=[]
deltaradius=[]
deltavelocity=[]
mass=[]
velocity1=[]
G=4.3*(10**-6)

for line in f:
  radius.append(float(line.split('\t')[0]))
  velocity.append(float(line.split('\t')[1]))
  deltaradius.append(float(line.split('\t')[2]))
  deltavelocity.append(float(line.split('\t')[3]))
  mass.append(float(line.split('\t')[4]))
  velocity1.append((float(G)) * (float(line.split('\t')[4])) / (float(line.split('\t')[0]))**(1/2))
  
x=np.array(radius)
y=np.array(velocity)
z=np.array(velocity1)

plt.plot(x,y)
plt.plot(x,z)
plt.xlabel('Radius(kpc)')
plt.ylabel('Velocity(km/s)')
plt.show()
