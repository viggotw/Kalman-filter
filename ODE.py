import numpy as np


class System:
    def __init__(self, A, B, C, D):
        self.A = np.matrix(A)
        self.B = np.matrix(B)
        self.C = np.matrix(C)
        self.D = np.matrix(D)

        self.dxdt = lambda x, u: self.A*x + self.B*u
        self.y = lambda x, u: self.C*x + self.D*u

    def ode(self, x, u, dt=0.1):
        x = np.matrix(x)
        u = np.matrix(u)

        x_new = x + dt*self.dxdt(x, u)
        return x_new

    def sim_unperturbed(self, t, x0):
        x0 = np.matrix(x0)
        u = np.zeros([self.B.shape[1], 1])

        x = [x0]
        y = [self.y(x=x0, u=u)]

        for i in range(len(t[1:])):
            dt = t[i] - t[i-1]

            x.append(
                x[-1] + dt * self.dxdt(x=x[-1], u=u)
            )

            y.append(
                self.y(x=x[-1], u=u)
            )

        return y


if __name__ == '__main__':
    print("Import as 'import ODE.System as System'")