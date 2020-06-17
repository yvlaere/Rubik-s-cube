import Rubik_s_cube as rc
import scrambler as sc
import cubeSolver as cs

command = input("Enter command: ")

while command != "quit":
    if command[0:8] == "scramble":
        print("scrambling")
        scrambleCount = command[:-1][9:]
        sc.scramble(int(scrambleCount))
    elif command == "solve":
        print("solving")
        cs.solve()
        print("solved")
    elif command[0:4] == "xrot":
        rc.cubes = rc.xRot(int(command[5]), command[4], rc.cubes)
    elif command[0:4] == "yrot":
        rc.cubes = rc.yRot(int(command[5]), command[4], rc.cubes)
    elif command[0:4] == "zrot":
        rc.cubes = rc.zRot(int(command[5]), command[4], rc.cubes)
    else:
        print("invalid command")
    command = input("Enter command: ")

rc.plt.show()

#errors

##step 6 if there is no correct cubie
##check sooner if cubie is in place in step 2 or something wrong or endless loop