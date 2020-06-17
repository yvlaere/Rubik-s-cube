import Rubik_s_cube as rc

def solve():
#initialize
    print("initialize")
    counter0 = 0
    while rc.cubes[2][2][0].uc != rc.cubes[2][1][1].uc:
        if counter0 < 3:
            rc.cubes = rc.xRot(1, 'r', rc.cubes)
        else:
            rc.cubes = rc.yRot(1, 'r', rc.cubes)
        counter0 = counter0 + 1
        print(counter0)

#step 1
    print("step 1")
    for i in range(3):
        color1 = [rc.cubes[2][2][0].uc, rc.cubes[2][2][0].rsc]
        rc.cubes = rc.zRot(0, 'l', rc.cubes)
        rc.cubes = rc.zRot(1, 'l', rc.cubes)
        rc.cubes = rc.zRot(2, 'l', rc.cubes)

        #check upper cube
        counter1 = 0
        if rc.cubes[2][2][0].uc in color1:
            counter1 = counter1 + 1
        if rc.cubes[2][2][0].fc in color1:
            counter1 = counter1 + 1
        if rc.cubes[2][2][0].rsc in color1:
            counter1 = counter1 + 1

        #not upper cube
        if counter1 < 2:
            counter2 = 0
            counter3 = 0
            while counter2 < 2:
                rc.cubes = rc.zRot(0, 'r', rc.cubes)
                if rc.cubes[0][2][0].dc in color1:
                    counter2 = counter2 + 1
                if rc.cubes[0][2][0].fc in color1:
                    counter2 = counter2 + 1
                if rc.cubes[0][2][0].rsc in color1:
                    counter2 = counter2 + 1
                if counter2 < 2:
                    counter2 = 0
                counter3 = counter3 + 1
                if counter3 > 5:
                    print("something might go wrong")
                    if i == 0:
                        rc.cubes = rc.yRot(2, 'l', rc.cubes)
                        rc.cubes = rc.yRot(2, 'l', rc.cubes)
                    else:
                        rc.cubes = rc.xRot(2, 'l', rc.cubes)
                        rc.cubes = rc.xRot(2, 'l', rc.cubes)
                    counter3 = 0

            if rc.cubes[0][2][0].dc == color1[0]:
                print("algorithm 1.3")
                rc.cubes = rc.xRot(2, 'r', rc.cubes)
                rc.cubes = rc.zRot(0, 'r', rc.cubes)
                rc.cubes = rc.xRot(2, 'l', rc.cubes)
                rc.cubes = rc.zRot(0, 'r', rc.cubes)
                rc.cubes = rc.zRot(0, 'r', rc.cubes)
                rc.cubes = rc.xRot(2, 'r', rc.cubes)
                rc.cubes = rc.zRot(0, 'l', rc.cubes)
                rc.cubes = rc.xRot(2, 'l', rc.cubes)
            elif rc.cubes[0][2][0].fc == color1[0]:
                print("algorithm 1.2")
                rc.cubes = rc.zRot(0, 'l', rc.cubes)
                rc.cubes = rc.xRot(2, 'r', rc.cubes)
                rc.cubes = rc.zRot(0, 'r', rc.cubes)
                rc.cubes = rc.xRot(2, 'l', rc.cubes)
            elif rc.cubes[0][2][0].rsc == color1[0]:
                print("algorithm 1.1")
                rc.cubes = rc.xRot(2, 'r', rc.cubes)
                rc.cubes = rc.zRot(0, 'l', rc.cubes)
                rc.cubes = rc.xRot(2, 'l', rc.cubes)

        #upper cube
        else:
            if rc.cubes[2][2][0].uc == color1[0]:
                print("cubie already in place")
            elif rc.cubes[2][2][0].fc == color1[0]:
                print("algorithm 1.4")
                rc.cubes = rc.yRot(0, 'r', rc.cubes)
                rc.cubes = rc.zRot(0, 'r', rc.cubes)
                rc.cubes = rc.yRot(0, 'l', rc.cubes)
                rc.cubes = rc.zRot(0, 'r', rc.cubes)
                rc.cubes = rc.zRot(0, 'r', rc.cubes)
                rc.cubes = rc.xRot(2, 'r', rc.cubes)
                rc.cubes = rc.zRot(0, 'r', rc.cubes)
                rc.cubes = rc.xRot(2, 'l', rc.cubes)
            elif rc.cubes[2][2][0].rsc == color1[0]:
                print("algorithm 1.5")
                rc.cubes = rc.xRot(2, 'r', rc.cubes)
                rc.cubes = rc.zRot(0, 'l', rc.cubes)
                rc.cubes = rc.xRot(2, 'l', rc.cubes)
                rc.cubes = rc.zRot(0, 'r', rc.cubes)
                rc.cubes = rc.xRot(2, 'r', rc.cubes)
                rc.cubes = rc.zRot(0, 'l', rc.cubes)
                rc.cubes = rc.xRot(2, 'l', rc.cubes)

#step 2
    print("step 2")
    counter0 = 0
    tempcounter = 0
    while counter0 < 4:
        color1 = [rc.cubes[2][2][0].uc, rc.cubes[2][2][0].fc]

        #check upper cube
        counter1 = 0
        if rc.cubes[2][1][0].uc in color1:
            counter1 = counter1 + 1
        if rc.cubes[2][1][0].fc in color1:
            counter1 = counter1 + 1

        #not upper cube
        if counter1 < 2:
            counter2 = 0
            counter3 = 0
            temp0 = 0
            while counter2 < 2:
                rc.cubes = rc.zRot(0, 'r', rc.cubes)
                if rc.cubes[0][1][0].dc in color1:
                    counter2 = counter2 + 1
                if rc.cubes[0][1][0].fc in color1:
                    counter2 = counter2 + 1
                if counter2 < 2:
                    counter2 = 0
                counter3 = counter3 + 1
                if counter3 > 5:
                    temp0 = 1
                    counter2 = 2

            #down cube
            if temp0 == 0:
                if rc.cubes[0][1][0].dc == color1[0]:
                    print("algorithm 2.1")
                    rc.cubes = rc.xRot(1, 'r', rc.cubes)
                    rc.cubes = rc.zRot(0, 'l', rc.cubes)
                    rc.cubes = rc.zRot(0, 'l', rc.cubes)
                    rc.cubes = rc.xRot(1, 'l', rc.cubes)
                elif rc.cubes[0][1][0].fc == color1[0]:
                    print("algorithm 2.2")
                    rc.cubes = rc.zRot(0, 'l', rc.cubes)
                    rc.cubes = rc.xRot(1, 'r', rc.cubes)
                    rc.cubes = rc.zRot(0, 'r', rc.cubes)
                    rc.cubes = rc.xRot(1, 'l', rc.cubes)

            #middle cube
            elif temp0 == 1:
                counter2 = 0
                counter3 = 0
                while counter2 < 2:
                    rc.cubes = rc.zRot(1, 'r', rc.cubes)
                    if rc.cubes[1][2][0].fc in color1:
                        counter2 = counter2 + 1
                    if rc.cubes[1][2][0].rsc in color1:
                        counter2 = counter2 + 1
                    if counter2 < 2:
                        counter2 = 0
                    counter3 = counter3 + 1
                    if counter3 > 5:
                        temp0 = 2
                        counter2 = 2

                if temp0 == 1:
                    if rc.cubes[1][2][0].fc == color1[0]:
                        print("algorithm 2.4")
                        rc.cubes = rc.zRot(1, 'r', rc.cubes)
                        rc.cubes = rc.yRot(0, 'l', rc.cubes)
                        rc.cubes = rc.zRot(1, 'l', rc.cubes)
                        rc.cubes = rc.zRot(1, 'l', rc.cubes)
                        rc.cubes = rc.yRot(0, 'r', rc.cubes)
                        tempcounter = 0
                    elif rc.cubes[1][2][0].rsc == color1[0]:
                        print("algorithm 2.3")
                        rc.cubes = rc.zRot(1, 'r', rc.cubes)
                        rc.cubes = rc.yRot(0, 'r', rc.cubes)
                        rc.cubes = rc.zRot(1, 'l', rc.cubes)
                        rc.cubes = rc.yRot(0, 'l', rc.cubes)
                        tempcounter = 0
                else:
                    print("temporarily skipping")
                    counter0 = counter0 - 4
                    tempcounter = tempcounter + 1

                if tempcounter == 4:
                    print("incorrect algorithm 2.5")
                    rc.cubes = rc.xRot(1, 'r', rc.cubes)
                    rc.cubes = rc.zRot(0, 'l', rc.cubes)
                    rc.cubes = rc.zRot(0, 'l', rc.cubes)
                    rc.cubes = rc.xRot(1, 'l', rc.cubes)
                    rc.cubes = rc.zRot(0, 'l', rc.cubes)
                    rc.cubes = rc.xRot(1, 'r', rc.cubes)
                    rc.cubes = rc.zRot(0, 'r', rc.cubes)
                    rc.cubes = rc.xRot(1, 'l', rc.cubes)

        #upper cube
        else:
            tempcounter = 0
            if rc.cubes[2][1][0].uc == color1[0]:
                print("cubie already in place")
            elif rc.cubes[2][1][0].fc == color1[0]:
                print("algorithm 2.5")
                rc.cubes = rc.xRot(1, 'r', rc.cubes)
                rc.cubes = rc.zRot(0, 'l', rc.cubes)
                rc.cubes = rc.zRot(0, 'l', rc.cubes)
                rc.cubes = rc.xRot(1, 'l', rc.cubes)
                rc.cubes = rc.zRot(0, 'l', rc.cubes)
                rc.cubes = rc.xRot(1, 'r', rc.cubes)
                rc.cubes = rc.zRot(0, 'r', rc.cubes)
                rc.cubes = rc.xRot(1, 'l', rc.cubes)

        rc.cubes = rc.zRot(0, 'l', rc.cubes)
        rc.cubes = rc.zRot(1, 'l', rc.cubes)
        rc.cubes = rc.zRot(2, 'l', rc.cubes)
        counter0 = counter0 + 1


#step 3
    print("step 3")
    while rc.cubes[2][2][0].fc != rc.cubes[1][1][0].fc:
        rc.cubes = rc.zRot(1, 'r', rc.cubes)
    
    counter0 = 0
    counter2 = 0
    counter4 = 0
    finished = []
    while counter0 < 8:
        temp0 = 0
        counter1 = 0
        while temp0 == 0:
            if rc.cubes[0][1][0].fc == rc.cubes[1][1][0].fc:

                #fronts match
                if rc.cubes[0][1][0].dc == rc.cubes[1][2][1].rsc:
                    print("algorithm 3.2")
                    rc.cubes = rc.zRot(0, 'l', rc.cubes)
                    rc.cubes = rc.xRot(2, 'r', rc.cubes)
                    rc.cubes = rc.zRot(0, 'r', rc.cubes)
                    rc.cubes = rc.xRot(2, 'l', rc.cubes)
                    rc.cubes = rc.zRot(0, 'r', rc.cubes)
                    rc.cubes = rc.yRot(0, 'r', rc.cubes)
                    rc.cubes = rc.zRot(0, 'l', rc.cubes)
                    rc.cubes = rc.yRot(0, 'l', rc.cubes)
                    counter1 = 0
                    counter4 = counter4 + 1
                    temp0 = 1
                    counter2 = 0
                elif rc.cubes[0][1][0].dc == rc.cubes[1][0][1].lsc:
                    print("algorithm 3.1")
                    rc.cubes = rc.zRot(0, 'r', rc.cubes)
                    rc.cubes = rc.xRot(0, 'r', rc.cubes)
                    rc.cubes = rc.zRot(0, 'l', rc.cubes)
                    rc.cubes = rc.xRot(0, 'l', rc.cubes)
                    rc.cubes = rc.zRot(0, 'l', rc.cubes)
                    rc.cubes = rc.yRot(0, 'l', rc.cubes)
                    rc.cubes = rc.zRot(0, 'r', rc.cubes)
                    rc.cubes = rc.yRot(0, 'r', rc.cubes)
                    counter1 = 0
                    counter4 = counter4 + 1
                    temp0 = 1
                    counter2 = 0
                else:
                    print("only front match, maybe something goes wrong here")
                    #temp0 = 1
                    rc.cubes = rc.zRot(0, 'l', rc.cubes)
                    counter1 = counter1 + 1
                    #counter0 = counter0 - 1

            #fronts dont match
            else:
                rc.cubes = rc.zRot(0, 'l', rc.cubes)
                counter1 = counter1 + 1

            #temporarily skip
            if counter1 > 5:
                print("temporarily skipping")
                ##############################################next line probs needs fixing
                counter0 = counter0 - 1
                counter2 = counter2 + 1
                ########
                #counter1 = 0
                print("skipcounter = " + str(counter2))
                temp0 = 2

        if counter2 > 4:
            temp1 = 0
            counter3 = 0
            while temp1 == 0:
                print("special routine")
                rc.cubes = rc.zRot(0, 'l', rc.cubes)
                rc.cubes = rc.zRot(1, 'l', rc.cubes)
                rc.cubes = rc.zRot(2, 'l', rc.cubes)

                if rc.cubes[1][2][0].rsc != rc.cubes[2][2][0].rsc:
                    print("incorrect algorithm 3.2")
                    rc.cubes = rc.zRot(0, 'l', rc.cubes)
                    rc.cubes = rc.xRot(2, 'r', rc.cubes)
                    rc.cubes = rc.zRot(0, 'r', rc.cubes)
                    rc.cubes = rc.xRot(2, 'l', rc.cubes)
                    rc.cubes = rc.zRot(0, 'r', rc.cubes)
                    rc.cubes = rc.yRot(0, 'r', rc.cubes)
                    rc.cubes = rc.zRot(0, 'l', rc.cubes)
                    rc.cubes = rc.yRot(0, 'l', rc.cubes)
                    #counter4 = counter4 - 1
                elif rc.cubes[1][0][0].lsc != rc.cubes[2][0][0].lsc:
                    print("incorrect algorithm 3.1")
                    rc.cubes = rc.zRot(0, 'r', rc.cubes)
                    rc.cubes = rc.xRot(0, 'r', rc.cubes)
                    rc.cubes = rc.zRot(0, 'l', rc.cubes)
                    rc.cubes = rc.xRot(0, 'l', rc.cubes)
                    rc.cubes = rc.zRot(0, 'l', rc.cubes)
                    rc.cubes = rc.yRot(0, 'l', rc.cubes)
                    rc.cubes = rc.zRot(0, 'r', rc.cubes)
                    rc.cubes = rc.yRot(0, 'r', rc.cubes)
                    #counter4 = counter4 - 1
                temp1 = 1
                counter2 = 0
                #counter3 = counter3 + 1
                #if counter3 > 5:
                #    temp1 = 1
        
        if counter4 == 4:
            counter0 = 8

        counter0 = counter0 + 1
        print("counter0: " + str(counter0))

        #terminating statement
        if rc.cubes[1][2][0].fc  == rc.cubes[1][1][0].fc and rc.cubes[1][2][0].rsc == rc.cubes[1][2][1].rsc:
            if rc.cubes[1][0][0].fc  == rc.cubes[1][1][0].fc and rc.cubes[1][0][0].lsc == rc.cubes[1][0][1].lsc:
                if rc.cubes[1][1][0] not in finished:
                    finished.append(rc.cubes[1][1][0])
                    print("finished3: " + str(len(finished)))

        if len(finished) == 4:
            counter0 = 8

        rc.cubes = rc.zRot(0, 'l', rc.cubes)
        rc.cubes = rc.zRot(1, 'l', rc.cubes)
        rc.cubes = rc.zRot(2, 'l', rc.cubes)


#step 4
    print("step 4")
    rc.cubes = rc.xRot(0, 'l', rc.cubes)
    rc.cubes = rc.xRot(1, 'l', rc.cubes)
    rc.cubes = rc.xRot(2, 'l', rc.cubes)
    rc.cubes = rc.xRot(0, 'l', rc.cubes)
    rc.cubes = rc.xRot(1, 'l', rc.cubes)
    rc.cubes = rc.xRot(2, 'l', rc.cubes)

    color2 = [rc.cubes[2][2][0].uc,  rc.cubes[2][2][0].rsc, rc.cubes[2][2][0].fc]
    while rc.cubes[1][2][0].fc not in color2 or rc.cubes[1][2][0].rsc not in color2 or rc.cubes[2][1][1].uc not in color2:
        rc.cubes = rc.zRot(2, 'l', rc.cubes)
        color2 = [rc.cubes[2][2][0].uc,  rc.cubes[2][2][0].rsc, rc.cubes[2][2][0].fc]

    rc.cubes = rc.zRot(0, 'l', rc.cubes)
    rc.cubes = rc.zRot(1, 'l', rc.cubes)
    rc.cubes = rc.zRot(2, 'l', rc.cubes)
    rc.cubes = rc.zRot(0, 'l', rc.cubes)
    rc.cubes = rc.zRot(1, 'l', rc.cubes)
    rc.cubes = rc.zRot(2, 'l', rc.cubes)

    #colors left
    color2 = [rc.cubes[2][1][1].uc,  rc.cubes[1][0][0].lsc, rc.cubes[1][0][0].fc]

    if rc.cubes[2][0][0].fc in color2 and rc.cubes[2][0][0].lsc in color2 and rc.cubes[2][0][0].uc in color2:
        print("left cubie already in place")
    elif rc.cubes[2][2][0].fc in color2 and rc.cubes[2][2][0].rsc in color2 and rc.cubes[2][2][0].uc in color2:
        print("algorithm 4.1")
        rc.cubes = rc.xRot(0, 'l', rc.cubes)
        rc.cubes = rc.zRot(2, 'r', rc.cubes)
        rc.cubes = rc.xRot(0, 'r', rc.cubes)
        rc.cubes = rc.yRot(0, 'r', rc.cubes)
        rc.cubes = rc.zRot(2, 'l', rc.cubes)
        rc.cubes = rc.yRot(0, 'l', rc.cubes)
        rc.cubes = rc.xRot(0, 'l', rc.cubes)
        rc.cubes = rc.zRot(2, 'l', rc.cubes)
        rc.cubes = rc.xRot(0, 'r', rc.cubes)
        rc.cubes = rc.zRot(2, 'l', rc.cubes)
        rc.cubes = rc.zRot(2, 'l', rc.cubes)
    else:
        print("algorithm 4.2 followed by algorithm 4.1")
        rc.cubes = rc.zRot(2, 'l', rc.cubes)
        rc.cubes = rc.xRot(0, 'l', rc.cubes)
        rc.cubes = rc.zRot(2, 'r', rc.cubes)
        rc.cubes = rc.xRot(0, 'r', rc.cubes)
        rc.cubes = rc.yRot(0, 'r', rc.cubes)
        rc.cubes = rc.zRot(2, 'l', rc.cubes)
        rc.cubes = rc.yRot(0, 'l', rc.cubes)
        rc.cubes = rc.xRot(0, 'l', rc.cubes)
        rc.cubes = rc.zRot(2, 'l', rc.cubes)
        rc.cubes = rc.xRot(0, 'r', rc.cubes)
        rc.cubes = rc.zRot(2, 'l', rc.cubes)

        rc.cubes = rc.xRot(0, 'l', rc.cubes)
        rc.cubes = rc.zRot(2, 'r', rc.cubes)
        rc.cubes = rc.xRot(0, 'r', rc.cubes)
        rc.cubes = rc.yRot(0, 'r', rc.cubes)
        rc.cubes = rc.zRot(2, 'l', rc.cubes)
        rc.cubes = rc.yRot(0, 'l', rc.cubes)
        rc.cubes = rc.xRot(0, 'l', rc.cubes)
        rc.cubes = rc.zRot(2, 'l', rc.cubes)
        rc.cubes = rc.xRot(0, 'r', rc.cubes)
        rc.cubes = rc.zRot(2, 'l', rc.cubes)
        rc.cubes = rc.zRot(2, 'l', rc.cubes)

    #colors front
    color2 = [rc.cubes[2][1][1].uc,  rc.cubes[1][2][0].rsc, rc.cubes[1][2][0].fc]

    if rc.cubes[2][2][0].fc in color2 and rc.cubes[2][2][0].rsc in color2 and rc.cubes[2][2][0].uc in color2:
        print("cubie already in place")
    else:
        print("algorithm 4.2")
        rc.cubes = rc.zRot(2, 'l', rc.cubes)
        rc.cubes = rc.xRot(0, 'l', rc.cubes)
        rc.cubes = rc.zRot(2, 'r', rc.cubes)
        rc.cubes = rc.xRot(0, 'r', rc.cubes)
        rc.cubes = rc.yRot(0, 'r', rc.cubes)
        rc.cubes = rc.zRot(2, 'l', rc.cubes)
        rc.cubes = rc.yRot(0, 'l', rc.cubes)
        rc.cubes = rc.xRot(0, 'l', rc.cubes)
        rc.cubes = rc.zRot(2, 'l', rc.cubes)
        rc.cubes = rc.xRot(0, 'r', rc.cubes)
        rc.cubes = rc.zRot(2, 'l', rc.cubes)

#step 5
    print("step 5")
    color3 = rc.cubes[2][1][1].uc
    finished = []

    while len(finished) < 4:
        temp0 = 0
        counter0 = 0

        while temp0 == 0:
            if rc.cubes[2][0][0].fc == color3 and rc.cubes[2][2][0].uc == color3:
                print("algorithm 5.1")
                temp0 = 1
            elif rc.cubes[2][2][2].rsc == color3 and rc.cubes[2][2][0].rsc == color3:
                print("algorithm 5.2")
                temp0 = 1
            elif rc.cubes[2][2][2].rsc == color3 and rc.cubes[2][2][0].uc == color3:
                print("algorithm 5.3")
                temp0 = 1
            else:
                ##########################
                for i in range(4):
                    if rc.cubes[2][2][0].fc == rc.cubes[1][2][0].fc and rc.cubes[2][2][0].uc == rc.cubes[2][1][1].uc and rc.cubes[2][2][0].rsc == rc.cubes[1][2][0].rsc:
                        print("cubie is already in place")
                        if rc.cubes[1][1][0] not in finished:
                            finished.append(rc.cubes[1][1][0])
                            print("finished51: " + str(len(finished)))
                        rc.cubes = rc.zRot(0, 'l', rc.cubes)
                        rc.cubes = rc.zRot(1, 'l', rc.cubes)
                        rc.cubes = rc.zRot(2, 'l', rc.cubes)
                rc.cubes = rc.zRot(2, 'l', rc.cubes)
                if len(finished) < 4:
                    counter0 = counter0 + 1
                if len(finished) == 4:
                    temp0 = 3
            if counter0 > 4:
                print("incorrect algorithm 5")
                temp0 = 2

        if temp0 == 1 or temp0 == 2:
            rc.cubes = rc.xRot(0, 'l', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
            rc.cubes = rc.xRot(0, 'r', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
            rc.cubes = rc.xRot(0, 'l', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
            rc.cubes = rc.xRot(0, 'r', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)

        counter0 = 0

        #terminating statement
        for i in range(4):
            if rc.cubes[2][2][0].fc == rc.cubes[1][2][0].fc and rc.cubes[2][2][0].uc == rc.cubes[2][1][1].uc and rc.cubes[2][2][0].rsc == rc.cubes[1][2][0].rsc:
                print("cubie is already in place")
                if rc.cubes[1][1][0] not in finished:
                        finished.append(rc.cubes[1][1][0])
                        print("finished52: " + str(len(finished)))
                rc.cubes = rc.zRot(0, 'l', rc.cubes)
                rc.cubes = rc.zRot(1, 'l', rc.cubes)
                rc.cubes = rc.zRot(2, 'l', rc.cubes)

    while rc.cubes[2][2][0].fc != rc.cubes[1][2][0].fc:
        rc.cubes = rc.zRot(2, 'l', rc.cubes)

#step 6
    print("step 6")

    #putting right cubie in front maybe counter for more than four times, then alg
    counter1 = 0
    color7 = [rc.cubes[2][1][1].uc, rc.cubes[1][1][0].fc]
    while counter1 < 4:
        if rc.cubes[2][1][0].fc not in color7 or rc.cubes[2][1][0].uc not in color7:
            rc.cubes = rc.zRot(0, 'l', rc.cubes)
            rc.cubes = rc.zRot(1, 'l', rc.cubes)
            rc.cubes = rc.zRot(2, 'l', rc.cubes)
            color7 = [rc.cubes[2][1][1].uc, rc.cubes[1][1][0].fc]
        counter1 = counter1 + 1

    if counter1 > 4:
        #twice?
        print("incorrect algorithm 6")
        rc.cubes = rc.xRot(1, 'l', rc.cubes)
        rc.cubes = rc.zRot(2, 'r', rc.cubes)
        rc.cubes = rc.xRot(1, 'r', rc.cubes)
        rc.cubes = rc.zRot(2, 'r', rc.cubes)
        rc.cubes = rc.zRot(2, 'r', rc.cubes)
        rc.cubes = rc.xRot(1, 'l', rc.cubes)
        rc.cubes = rc.zRot(2, 'r', rc.cubes)
        rc.cubes = rc.xRot(1, 'r', rc.cubes)
        counter0 = counter0 + 1

    temp0 = 0
    counter0 = 0
    while temp0 == 0:
        #terminating statement
        color4 = [rc.cubes[2][1][1].uc, rc.cubes[1][1][0].fc]
        color5 = [rc.cubes[2][1][1].uc, rc.cubes[1][2][1].rsc]
        color6 = [rc.cubes[2][1][1].uc, rc.cubes[1][0][1].lsc]
        if rc.cubes[2][1][0].fc in color4 and rc.cubes[2][1][0].uc in color4:
            print("s1")
            if rc.cubes[2][2][1].rsc in color5 and rc.cubes[2][2][1].uc in color5:
                print("s2")
                temp0 = 1
                if rc.cubes[2][0][1].rsc in color6 and rc.cubes[2][0][1].uc in color6:
                    print("s3")
                    temp0 = 1

        if temp0 == 0:
            print("algorithm 6")
            rc.cubes = rc.xRot(1, 'l', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
            rc.cubes = rc.xRot(1, 'r', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
            rc.cubes = rc.xRot(1, 'l', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
            rc.cubes = rc.xRot(1, 'r', rc.cubes)
            counter0 = counter0 + 1

        if counter0 > 3:
            temp0 = 1

        rc.cubes = rc.zRot(2, 'l', rc.cubes)

        while rc.cubes[2][2][0].fc != rc.cubes[1][2][0].fc:
            rc.cubes = rc.zRot(2, 'l', rc.cubes)

#step 7
    print("step 7")

    counter0 = 0
    while counter0 < 4:
        if rc.cubes[2][2][1].uc == rc.cubes[2][1][1].uc:
            rc.cubes = rc.zRot(0, 'l', rc.cubes)
            rc.cubes = rc.zRot(1, 'l', rc.cubes)
            rc.cubes = rc.zRot(2, 'l', rc.cubes)
            counter0 = counter0 + 1
        else:
            counter0 = counter0 + 1

    temp0 = 0
    while temp0 == 0:
        if rc.cubes[2][0][1].uc != rc.cubes[2][1][1].uc:
            print("algorithm 7.1")
            rc.cubes = rc.xRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(1, 'l', rc.cubes)
            rc.cubes = rc.xRot(2, 'r', rc.cubes)
            rc.cubes = rc.xRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(1, 'l', rc.cubes)
            rc.cubes = rc.zRot(1, 'l', rc.cubes)
            rc.cubes = rc.xRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
            rc.cubes = rc.xRot(2, 'l', rc.cubes)
            rc.cubes = rc.zRot(1, 'r', rc.cubes)
            rc.cubes = rc.zRot(1, 'r', rc.cubes)
            rc.cubes = rc.xRot(2, 'r', rc.cubes)
            rc.cubes = rc.xRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(1, 'r', rc.cubes)
            rc.cubes = rc.xRot(2, 'l', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
        elif rc.cubes[2][1][0].uc != rc.cubes[2][1][1].uc:
            print("algorithm 7.2")
            rc.cubes = rc.yRot(0, 'l', rc.cubes)
            rc.cubes = rc.xRot(0, 'l', rc.cubes)
            rc.cubes = rc.xRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(1, 'l', rc.cubes)
            rc.cubes = rc.xRot(2, 'r', rc.cubes)
            rc.cubes = rc.xRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(1, 'l', rc.cubes)
            rc.cubes = rc.zRot(1, 'l', rc.cubes)
            rc.cubes = rc.xRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
            rc.cubes = rc.xRot(2, 'l', rc.cubes)
            rc.cubes = rc.zRot(1, 'r', rc.cubes)
            rc.cubes = rc.zRot(1, 'r', rc.cubes)
            rc.cubes = rc.xRot(2, 'r', rc.cubes)
            rc.cubes = rc.xRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(1, 'r', rc.cubes)
            rc.cubes = rc.xRot(2, 'l', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
            rc.cubes = rc.xRot(0, 'r', rc.cubes)
            rc.cubes = rc.yRot(0, 'r', rc.cubes)
        elif rc.cubes[2][1][2].uc != rc.cubes[2][1][1].uc:
            rc.cubes = rc.zRot(0, 'l', rc.cubes)
            rc.cubes = rc.zRot(1, 'l', rc.cubes)
            rc.cubes = rc.zRot(2, 'l', rc.cubes)
            print("algorithm 7.2")
            rc.cubes = rc.yRot(0, 'l', rc.cubes)
            rc.cubes = rc.xRot(0, 'l', rc.cubes)
            rc.cubes = rc.xRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(1, 'l', rc.cubes)
            rc.cubes = rc.xRot(2, 'r', rc.cubes)
            rc.cubes = rc.xRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(1, 'l', rc.cubes)
            rc.cubes = rc.zRot(1, 'l', rc.cubes)
            rc.cubes = rc.xRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
            rc.cubes = rc.xRot(2, 'l', rc.cubes)
            rc.cubes = rc.zRot(1, 'r', rc.cubes)
            rc.cubes = rc.zRot(1, 'r', rc.cubes)
            rc.cubes = rc.xRot(2, 'r', rc.cubes)
            rc.cubes = rc.xRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(1, 'r', rc.cubes)
            rc.cubes = rc.xRot(2, 'l', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
            rc.cubes = rc.zRot(2, 'r', rc.cubes)
            rc.cubes = rc.xRot(0, 'r', rc.cubes)
            rc.cubes = rc.yRot(0, 'r', rc.cubes)

        else:
            temp0 = 1