import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from mpl_toolkits.mplot3d import Axes3D
from math import pi

class Cube:
    def __init__(self, pos):
        self.colors = ["#ffffff", "#00008f", "#ff6f00", "#ffcf00", "#009f0f", "#cf0000"]
        self.xCenter = pos[0]
        self.yCenter = pos[1]
        self.zCenter = pos[2]

        #bovenvlak
        self.Xu = np.array([[self.xCenter - 0.5, self.xCenter + 0.5], [self.xCenter - 0.5, self.xCenter + 0.5]])
        self.Yu = np.array([[self.yCenter - 0.5, self.yCenter - 0.5], [self.yCenter + 0.5, self.yCenter + 0.5]])
        self.Zu = np.array([[self.zCenter + 0.5, self.zCenter + 0.5], [self.zCenter + 0.5, self.zCenter + 0.5]])

        #ondervlak
        self.Xd = self.Xu
        self.Yd = self.Yu
        self.Zd = self.Zu - 1
        
        #achtervlak
        self.Xb = np.array([[self.xCenter - 0.5, self.xCenter + 0.5], [self.xCenter - 0.5, self.xCenter + 0.5]])
        self.Yb = np.array([[self.yCenter + 0.5, self.yCenter + 0.5], [self.yCenter + 0.5, self.yCenter + 0.5]])
        self.Zb = np.array([[self.zCenter - 0.5, self.zCenter - 0.5], [self.zCenter + 0.5, self.zCenter + 0.5]])

        #voorvlak
        self.Xf = self.Xb
        self.Yf = self.Yb - 1
        self.Zf = self.Zb
        
        #rechterzijvlak
        self.Xrs = np.array([[self.xCenter + 0.5, self.xCenter + 0.5], [self.xCenter + 0.5, self.xCenter + 0.5]])
        self.Yrs = np.array([[self.yCenter - 0.5, self.yCenter - 0.5], [self.yCenter + 0.5, self.yCenter + 0.5]])
        self.Zrs = np.array([[self.zCenter + 0.5, self.zCenter - 0.5], [self.zCenter + 0.5, self.zCenter - 0.5]])

        #linkerzijvlak
        self.Xls = self.Xrs - 1
        self.Yls = self.Yrs
        self.Zls = self.Zrs

        self.X = [self.Xu, self.Xd, self.Xb, self.Xf, self.Xrs, self.Xls]
        self.Y = [self.Yu, self.Yd, self.Yb, self.Yf, self.Yrs, self.Yls]
        self.Z = [self.Zu, self.Zd, self.Zb, self.Zf, self.Zrs, self.Zls]

        self.u = ax.plot_surface(self.X[0], self.Y[0], self.Z[0], color = self.colors[0])
        self.uc = self.colors[0]
        self.d = ax.plot_surface(self.X[1], self.Y[1], self.Z[1], color = self.colors[1])
        self.dc = self.colors[1]
        self.b = ax.plot_surface(self.X[2], self.Y[2], self.Z[2], color = self.colors[2])
        self.bc = self.colors[2]
        self.f = ax.plot_surface(self.X[3], self.Y[3], self.Z[3], color = self.colors[3])
        self.fc = self.colors[3]
        self.rs = ax.plot_surface(self.X[4], self.Y[4], self.Z[4], color = self.colors[4])
        self.rsc = self.colors[4]
        self.ls = ax.plot_surface(self.X[5], self.Y[5], self.Z[5], color = self.colors[5])
        self.lsc = self.colors[5]

    def removeOldSurfaces(self):
        self.u.remove()
        self.d.remove()
        self.b.remove()
        self.f.remove()
        self.rs.remove()
        self.ls.remove()

    def draw(self):
        self.u = ax.plot_surface(self.X[0], self.Y[0], self.Z[0], color = self.colors[0])
        self.d = ax.plot_surface(self.X[1], self.Y[1], self.Z[1], color = self.colors[1])
        self.b = ax.plot_surface(self.X[2], self.Y[2], self.Z[2], color = self.colors[2])
        self.f = ax.plot_surface(self.X[3], self.Y[3], self.Z[3], color = self.colors[3])
        self.rs = ax.plot_surface(self.X[4], self.Y[4], self.Z[4], color = self.colors[4])
        self.ls = ax.plot_surface(self.X[5], self.Y[5], self.Z[5], color = self.colors[5])

    def reallocColors(self, rot):
        if rot == 'xr':
            temp1 = self.fc
            self.fc = self.uc
            self.uc = self.bc
            self.bc = self.dc
            self.dc = temp1
        elif rot == 'xl':
            temp1 = self.bc
            self.bc = self.uc
            self.uc = self.fc
            self.fc = self.dc
            self.dc = temp1
        elif rot == 'yr':
            temp1 = self.rsc
            self.rsc = self.uc
            self.uc = self.lsc
            self.lsc = self.dc
            self.dc = temp1
        elif rot == 'yl':
            temp1 = self.lsc
            self.lsc = self.uc
            self.uc = self.rsc
            self.rsc = self.dc
            self.dc = temp1
        elif rot == 'zr':
            temp1 = self.rsc
            self.rsc = self.fc
            self.fc = self.lsc
            self.lsc = self.bc
            self.bc = temp1
        elif rot == 'zl':
            temp1 = self.rsc
            self.rsc = self.bc
            self.bc = self.lsc
            self.lsc = self.fc
            self.fc = temp1

class Quaternion:
    #rotation quaternion
    def q1(self, u, theta):
        qIndices = [x*np.sin(theta/2) for x in u]
        w = np.cos(theta/2)
        qIndices.append(w)
        return qIndices

    #inverted rotation quaternion
    def q2(self, u, theta):
        qIndices = [-x*np.sin(theta/2) for x in u]
        w = np.cos(theta/2)
        qIndices.append(w)
        return qIndices

    def __init__(self, u, theta):
        self.q1Indices = self.q1(u, theta)
        self.q2Indices = self.q2(u, theta)

    def mul(self, p):
        #q1*p
        p.append(0) 
        a = self.q1Indices[3]
        b = self.q1Indices[0]
        c = self.q1Indices[1]
        d = self.q1Indices[2]
        e = p[3]
        f = p[0]
        g = p[1]
        h = p[2]
        temp = [b*e + a*f + c*h - d*g, a*g - b*h + c*e + d*f, a*h + b*g - c*f + d*e, a*e - b*f - c*g- d*h]

        #q1*p*q2
        a = temp[3]
        b = temp[0]
        c = temp[1]
        d = temp[2]
        e = self.q2Indices[3]
        f = self.q2Indices[0]
        g = self.q2Indices[1]
        h = self.q2Indices[2]
        newp = [b*e + a*f + c*h - d*g, a*g - b*h + c*e + d*f, a*h + b*g - c*f + d*e, a*e - b*f - c*g- d*h]
        if round(newp[3]) != 0.0:
            print("Quaternion calculation error: real part != 0")
        return newp

def rotateFace(cube, face, quat):
    faces = [cube.u, cube.d, cube.b, cube.f, cube.rs, cube.ls]

    temp1 = [cube.X[face][0][0], cube.Y[face][0][0], cube.Z[face][0][0]]
    temp2 = [cube.X[face][0][1], cube.Y[face][0][1], cube.Z[face][0][1]]
    temp3 = [cube.X[face][1][0], cube.Y[face][1][0], cube.Z[face][1][0]]
    temp4 = [cube.X[face][1][1], cube.Y[face][1][1], cube.Z[face][1][1]]
    temp1 = quat.mul(temp1)
    temp2 = quat.mul(temp2)
    temp3 = quat.mul(temp3)
    temp4 = quat.mul(temp4)
    cube.X[face] = np.array([[temp1[0], temp2[0]], [temp3[0], temp4[0]]])
    cube.Y[face] = np.array([[temp1[1], temp2[1]], [temp3[1], temp4[1]]])
    cube.Z[face] = np.array([[temp1[2], temp2[2]], [temp3[2], temp4[2]]])
    cube.removeOldSurfaces()
    cube.draw()

def rotate(cube, quat):
    for i in range(6):
        rotateFace(cube, i, quat)

def xRot(x, dir, cubes):
    if dir == 'r':
        theta = np.pi/2
    elif dir == 'l':
        theta = np.pi/(-2)
    else:
        print("Rotation call error: invalid direction")

    q = Quaternion([1, 0, 0], theta)
    rot = 'x' + dir

    for i in range(3):
        for j in range(3):
            rotate(cubes[i][x][j], q)

    #new location
    if dir == 'r':
        temp1 = cubes[0][x][2]
        cubes[0][x][2] = cubes[0][x][0]
        temp2 = cubes[2][x][2]
        cubes[2][x][2] = temp1
        temp1 = cubes[2][x][0]
        cubes[2][x][0] = temp2
        cubes[0][x][0] = temp1

        temp1 = cubes[1][x][2]
        cubes[1][x][2] = cubes[0][x][1]
        temp2 = cubes[2][x][1]
        cubes[2][x][1] = temp1
        temp1 = cubes[1][x][0]
        cubes[1][x][0] = temp2
        cubes[0][x][1] = temp1
    elif dir == 'l':
        temp1 = cubes[2][x][0]
        cubes[2][x][0] = cubes[0][x][0]
        temp2 = cubes[2][x][2]
        cubes[2][x][2] = temp1
        temp1 = cubes[0][x][2]
        cubes[0][x][2] = temp2
        cubes[0][x][0] = temp1

        temp1 = cubes[2][x][1]
        cubes[2][x][1] = cubes[1][x][0]
        temp2 = cubes[1][x][2]
        cubes[1][x][2] = temp1
        temp1 = cubes[0][x][1]
        cubes[0][x][1] = temp2
        cubes[1][x][0] = temp1

    for i in range(3):
        for j in range(3):
            cubes[i][x][j].reallocColors(rot)

    #plt.draw()
    #plt.pause(0.0001)

    plt.gcf().canvas.flush_events()
    plt.show(block=False)

    return cubes

def yRot(y, dir, cubes):
    if dir == 'r':
        theta = np.pi/2
    elif dir == 'l':
        theta = np.pi/(-2)
    else:
        print("Rotation call error: invalid direction")

    q = Quaternion([0, 1, 0], theta)
    rot = 'y' + dir

    for i in range(3):
        for j in range(3):
            rotate(cubes[i][j][y], q)

    #new location
    if dir == 'r':
        temp1 = cubes[2][0][y]
        cubes[2][0][y] = cubes[0][0][y]
        temp2 = cubes[2][2][y]
        cubes[2][2][y] = temp1
        temp1 = cubes[0][2][y]
        cubes[0][2][y] = temp2
        cubes[0][0][y] = temp1

        temp1 = cubes[2][1][y]
        cubes[2][1][y] = cubes[1][0][y]
        temp2 = cubes[1][2][y]
        cubes[1][2][y] = temp1
        temp1 = cubes[0][1][y]
        cubes[0][1][y] = temp2
        cubes[1][0][y] = temp1
    elif dir == 'l':
        temp1 = cubes[0][2][y]
        cubes[0][2][y] = cubes[0][0][y]
        temp2 = cubes[2][2][y]
        cubes[2][2][y] = temp1
        temp1 = cubes[2][0][y]
        cubes[2][0][y] = temp2
        cubes[0][0][y] = temp1

        temp1 = cubes[1][2][y]
        cubes[1][2][y] = cubes[0][1][y]
        temp2 = cubes[2][1][y]
        cubes[2][1][y] = temp1
        temp1 = cubes[1][0][y]
        cubes[1][0][y] = temp2
        cubes[0][1][y] = temp1

    for i in range(3):
        for j in range(3):
            cubes[i][j][y].reallocColors(rot)

    #plt.draw()
    #plt.pause(0.0001)

    plt.gcf().canvas.flush_events()
    plt.show(block=False)

    return cubes

def zRot(z, dir, cubes):
    if dir == 'r':
        theta = np.pi/2
    elif dir == 'l':
        theta = np.pi/(-2)
    else:
        print("Rotation call error: invalid direction")

    q = Quaternion([0, 0, 1], theta)
    rot = 'z' + dir

    for i in range(3):
        for j in range(3):
            rotate(cubes[z][i][j], q)
    
    #new location
    if dir == 'r':
        temp1 = cubes[z][2][0]
        cubes[z][2][0] = cubes[z][0][0]
        temp2 = cubes[z][2][2]
        cubes[z][2][2] = temp1
        temp1 = cubes[z][0][2]
        cubes[z][0][2] = temp2
        cubes[z][0][0] = temp1

        temp1 = cubes[z][2][1]
        cubes[z][2][1] = cubes[z][1][0]
        temp2 = cubes[z][1][2]
        cubes[z][1][2] = temp1
        temp1 = cubes[z][0][1]
        cubes[z][0][1] = temp2
        cubes[z][1][0] = temp1
    elif dir == 'l':
        temp1 = cubes[z][0][2]
        cubes[z][0][2] = cubes[z][0][0]
        temp2 = cubes[z][2][2]
        cubes[z][2][2] = temp1
        temp1 = cubes[z][2][0]
        cubes[z][2][0] = temp2
        cubes[z][0][0] = temp1

        temp1 = cubes[z][1][2]
        cubes[z][1][2] = cubes[z][0][1]
        temp2 = cubes[z][2][1]
        cubes[z][2][1] = temp1
        temp1 = cubes[z][1][0]
        cubes[z][1][0] = temp2
        cubes[z][0][1] = temp1

    for i in range(3):
        for j in range(3):
            cubes[z][i][j].reallocColors(rot)

    #plt.draw()
    #plt.pause(0.0001)

    plt.gcf().canvas.flush_events()
    plt.show(block=False)

    return cubes

#initialize
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.axis('off')

#draw rubik's cube
cubes = [[[[], [], []], [[], [], []], [[], [], []]], [[[], [], []], [[], [], []], [[], [], []]], [[[], [], []], [[], [], []], [[], [], []]]] #zxy
for i in range(0, 3):           #z
    for j in range(0, 3):       #x
        for k in range(0, 3):   #y
            cubes[i][j][k] = Cube([j - 1, k - 1, i - 1])

