from ODE import System
import numpy as np
import matplotlib.pyplot as plt

A = np.matrix('1, 1, 0.5; 0, 1, 1; 0, 0, 1')
B = np.matrix('0; 0; 0')
C = np.matrix('1, 0, 0; 0, 1, 0')
D = np.matrix('0')

x0 = np.matrix('0; 1; 0')

t0 = 0
tN = 100
dt = 0.1

sys = System(A=A, B=B, C=C, D=D)
t = np.linspace(t0, tN, int((tN-t0)/dt + 1))

y = sys.sim_unperturbed(t=t, x0=x0)

y1 = [y1[0, 0] for y1 in y]
y2 = [y2[1, 0] for y2 in y]

plt.plot(t, y1)
plt.plot(t, y2)
plt.xlim([0,1])
plt.ylim([-10,5])