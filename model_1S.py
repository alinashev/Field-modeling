import matplotlib.pyplot as plt

def Fx(V_x):
    return 0 - r * V_x**2

def Fy(V_y):
    return -q - r * V_y**2

def step_method(X_n_prev_2, VX_n_prev_1, Y_n_prev_2, VY_n_prev_1):
    X_n = X_n_prev_2 + 2 * dt * VX_n_prev_1
    Y_n = Y_n_prev_2 + 2 * dt * VY_n_prev_1
    VX_next = VX_n_prev_1 + 2 * dt * 1 / m * Fx(VY_n_prev_1)
    VY_next = VY_n_prev_1 + 2 * dt * 1 / m * Fy(VX_n_prev_1)
    return [X_n, VX_next, Y_n, VY_next]

m = 1
r = 0
q = 9.8
V_x = [15]
V_y = [15]
X = [0]
Y = [0]
dt = 0.001
t = 0
T = [t]

t = t + dt
VX_n = V_x[0] + dt * Fx(V_x[0] + r) / m
X_n = X[0] + VX_n * dt
VY_n = V_y[0] + dt * Fy(V_y[0] + r)  / m
Y_n = Y[0] + VY_n * dt

X.append(X_n)
Y.append(Y_n)
V_x.append(VX_n)
V_y.append(VY_n)

i = 2

while Y[i - 1] > 0:
    X_n, VX_next, Y_n, VY_next = step_method(X[i - 2], V_x[i - 1], Y[i - 2], V_y[i - 1])
    X.append(X_n)
    Y.append(Y_n)
    V_x.append(VX_next)
    V_y.append(VY_next)
    T.append(t)
    t = t + dt
    i = i + 1

plt.plot(X,Y)
plt.ylabel('y')
plt.xlabel('x')
plt.grid()
plt.show()