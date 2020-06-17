import random as rn
import Rubik_s_cube as rc

def scramble(scrambleCount):
    for i in range(scrambleCount):
        randI = rn.randint(1,18)
        #randI = i
        if randI == 1:
            rc.cubes = rc.xRot(0, 'r', rc.cubes)
        elif randI == 2:
            rc.cubes = rc.xRot(1, 'r', rc.cubes)
        elif randI == 3:
            rc.cubes = rc.xRot(2, 'r', rc.cubes)
        elif randI == 4:
            rc.cubes = rc.xRot(0, 'l', rc.cubes)
        elif randI == 5:
            rc.cubes = rc.xRot(1, 'l', rc.cubes)
        elif randI == 6:
            rc.cubes = rc.xRot(2, 'l', rc.cubes)
        elif randI == 7:
            rc.cubes = rc.yRot(0, 'r', rc.cubes)
        elif randI == 8:
            rc.cubes = rc.yRot(1, 'r', rc.cubes)
        elif randI == 9:
            rc.cubes = rc.yRot(2, 'r', rc.cubes)
        elif randI == 10:
            rc.cubes = rc.yRot(0, 'l', rc.cubes)
        elif randI == 11:
            rc.cubes = rc.yRot(1, 'l', rc.cubes)
        elif randI == 12:
            rc.cubes = rc.yRot(2, 'l', rc.cubes)
        elif randI == 13:
            rc.cubes = rc.zRot(0, 'r', rc.cubes)
        elif randI == 14:
            rc.cubes = rc.zRot(1, 'r', rc.cubes)
        elif randI == 15:
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
        elif randI == 16:
            rc.cubes = rc.zRot(0, 'l', rc.cubes)
        elif randI == 17:
            rc.cubes = rc.zRot(1, 'l', rc.cubes)
        elif randI == 18:
            rc.cubes = rc.zRot(2, 'l', rc.cubes)
        #rc.plt.draw()
        #rc.plt.pause(0.0001)
        print(randI)


def tab():
    rc.plt.pause(10)