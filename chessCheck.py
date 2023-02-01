pos = 0
hold = 0
piece = 0
status = 2 #هنگام ساخت برد اگر به سفید رسید 0 میشه به سیاه رسید 1 میشه
dm = 0 #donmove holder

#لیست متغیر ها
wkingList = []
bkingList = []
wqList = [] #queen
bqList = []

wrList = [] #white rooks list
brList = []

wbList = [] #white bishops lists
bbList = [] #b bishops list

wkList = [] #w kinghts list
bkList = [] #b knights list

wpawnList = [] #w pawns List
bpawnList = [] #b pawns List

wpList = [] #white positions
bpList = [] #black positions
apList = [] #all

#لیست برد ها
wkingm = [] #white king moves
bkingm = [] #black king moves

wqm = [] #white queen moves
bqm = [] #black queen moves

wrm = [] #rooks
brm = []

wbm = [] #bishops
bbm = []

wkm = [] #knights
bkm = []

wpm = [] # pawns moves
bpm = []

wpattack = []#pawns attack
bpattack = []

wam = [] #white all moves
bam = [] #black // //
am = []  #all moves

bchtlist = [] #black check takers
wchtlist = [] #white check takers
bchb = []#check board for black chtakers
wchb = []#  //    //   // white    //
wsp = [] #white support positions
bsp = [] #black   //      // 
wkingPM = []
bkingPM = []
bdonmove = [] # blacks which cant move
wdonmove = [] # whites which 

bchremover = []
bchblocker = []
wchblocker = []
wchremover = []

#FORCE white king
while True:
    wkingList.append(int(input("enter white king position")))
    if wkingList[0]>77 or wkingList[0]<0 or (wkingList[0]%10)>7:
        wkingList.pop()
        continue
    else:
        apList.append(wkingList[0])
        wpList.append(wkingList[0])
        print(f"so white king is on : {wkingList[0]}")
        break

#white king board generator
rs = wkingList[0]
r = rs // 10
s = rs % 10
rr = r-1
ss = s-1
while (rr != r + 2):
    while(ss != s + 2):
        if rr == r and ss == s: #limit self position
            ss = ss + 1
            continue
        if (rr * 10 + ss) in wpList: # limit self reserved position
            ss = ss + 1
            continue
        if (rr * 10 + ss) < 0 or (rr * 10 + ss) > 77 or ((rr * 10 + ss)%10) > 7: #limit board
            ss = ss + 1
            continue
        wkingm.append(rr * 10 + ss)
        ss = ss + 1
    rr = rr + 1
    ss = s - 1

#FORCE black king
while True:
    bkingList.append(int(input("enter black king position")))
    if bkingList[0]>77 or bkingList[0]<0 or (bkingList[0]%10)>7:
        bkingList.pop()
        continue
    elif bkingList[0] in wkingm:
        print("black & white kings cant touch eachothers; its HARAM!")
        bkingList.pop()
        continue
    else:
        print(f"so black king is on : {bkingList[0]}")
        apList.append(bkingList[0])
        bpList.append(bkingList[0])
        break


print("***")
print("position setting!")
print("white :   queen 2    rook  4     Bishop   6     knight   8     pawn    10")
print("black :   queen 20    rook  40     Bishop   60     knight   80     pawn    100")
print("1111 : exit")

#set pieces
while True:
    piece = int(input("select a piece by a number: "))
    if piece == 1111:
        break
    pos = int(input("now enter a valid position: "))
    if pos in apList:
        print("this position was reserved! try again!")
        continue
    if 77<pos or pos<0 or (pos%10)>7:
        print("enter valid position")
        continue

    match piece:
        #case 1:
            #wkingList.append(pos)
            #apList.append(pos)
            #wpList.append(pos)
        #case 10:
            #bkingList.append(pos)
            #apList.append(pos)
            #bpList.append(pos)
        case 2:
            wqList.append(pos)
            apList.append(pos)
            wpList.append(pos)
        case 20:
            bqList.append(pos)
            apList.append(pos)
            bpList.append(pos)
        case 4:
            wrList.append(pos)
            apList.append(pos)
            wpList.append(pos)
        case 40:
            brList.append(pos)
            apList.append(pos)
            bpList.append(pos)
        case 6:
            wbList.append(pos)
            apList.append(pos)
            wpList.append(pos)
        case 60:
            bbList.append(pos)
            apList.append(pos)
            bpList.append(pos)
        case 8:
            wkList.append(pos)
            apList.append(pos)
            wpList.append(pos)
        case 80:
            bkList.append(pos)
            apList.append(pos)
            bpList.append(pos)
        case 10:
            wpawnList.append(pos)
            apList.append(pos)
            wpList.append(pos)
        case 100:
            bpawnList.append(pos)
            apList.append(pos)
            bpList.append(pos)
        case _:
            print("enter correct piece!")


#set board---------------------------------------------------------------------------------------

#black king board
rs = bkingList[0]
r = rs // 10
s = rs % 10
rr = r - 1
ss = s - 1
while (rr != r + 2):
    while(ss != s+2):
        if rr == r and ss == s: #limit self position
            ss = ss + 1
            continue
        if (rr * 10 + ss) in bpList: # limit self reserved position
            bsp.append(rr * 10 + ss)
            ss = ss + 1
            continue
        if (rr * 10 + ss) < 0 or (rr * 10 + ss) > 77 or ((rr * 10 + ss)%10) > 7: #limit board
            ss = ss + 1
            continue
        bkingm.append(rr * 10 + ss)
        bam.append(rr * 10 + ss)
        am.append(rr * 10 + ss)
        ss = ss + 1
    rr = rr + 1
    ss = s - 1

#white king move update
wkingm = []
rs = wkingList[0]
r = rs // 10
s = rs % 10
rr = r-1
ss = s-1
while (rr != r + 2):
    while(ss != s + 2):
        if rr == r and ss == s: #limit self position
            ss = ss + 1
            continue
        if (rr * 10 + ss) in wpList: # limit self reserved position
            wsp.append(rr * 10 + ss)
            ss = ss + 1
            continue
        if (rr * 10 + ss) < 0 or (rr * 10 + ss) > 77 or ((rr * 10 + ss)%10) > 7: #limit board
            ss = ss + 1
            continue
        wkingm.append(rr * 10 + ss)
        wam.append(rr * 10 + ss)
        am.append(rr * 10 + ss)
        ss = ss + 1
    rr = rr + 1
    ss = s - 1

#chb[] check board
#donmove [] 
#w queen board
for number in wqList:
    r = number // 10
    s = number % 10
    rr = r
    ss = s - 1

    #horizontal-----------------------------------------------
    while ss >= 0:
        if (rr*10+ss) in wpList:
            status = 0
            wsp.append((rr*10+ss))
            break
        elif (rr*10+ss) in bpList:
            status = 1# dm...........................
            dm = (rr*10+ss)
            wqm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
            if (rr*10+ss) == bkingList[0]:
                for x in range(rr*10+ss+1 , number+1 ):# special #chb
                    wchb.append(x)
                wchtlist.append(number)
                wsp.append(rr*10+ss-1)
            break
        elif ss == s:
            ss = ss -1
            continue
        else:
            wqm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
        ss = ss - 1
    if bkingList [0] == dm:# dm ...................
        1+1
    elif status == 1 :
        ss = ss - 1
        while ss >= 0:
            if ((rr*10+ss)) in wpList:
                break
            if ((rr*10+ss)) in bpList:
                if (rr*10+ss) == bkingList[0]:
                    bdonmove.append(dm)
                    break
                else:
                    break
            ss = ss - 1

    ss = s + 1
    while ss < 8:
        if (rr*10+ss) in wpList:
            status = 0
            wsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in bpList:
            status = 1
            dm = (rr*10+ss)
            wqm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
            if (rr*10+ss) == bkingList[0]:
                for x in range( number + 1 , rr*10+ss+1):
                    wchb.append(x)
                wchtlist.append(number)
                wsp.append(rr*10+ss+1)
            break
        elif ss == s:
            ss = ss + 1
            continue
        else:
            wqm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
        ss = ss + 1

    if bkingList [0] == dm:# dm ...................
        1+1
    elif status == 1 :
        ss = ss + 1
        while ss < 8:
            if ((rr*10+ss)) in wpList:
                break
            if ((rr*10+ss)) in bpList:
                if (rr*10+ss) == bkingList[0]:
                    bdonmove.append(dm)
                    break
                else:
                    break
            ss = ss + 1
    ss = s
    rr = r - 1
    #vertical--------------------------------------------------------
    while rr >= 0:
        if (rr*10+ss) in wpList:
            status = 0
            wsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in bpList:
            status = 1
            dm = (rr*10+ss)
            wqm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
            if (rr*10+ss) == bkingList[0]:
                for x in range(number-10 , (rr*10+ss) , -10 ):
                    wchb.append(x)
                wchtlist.append(number)
                wsp.append((rr-1)*10+ss)
            break
        elif rr == r:
            rr = rr -1
            continue
        else:
            wqm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr - 1
    if bkingList [0] == dm:# dm ...................
        1+1
    elif status == 1 :
        rr = rr - 1
        while rr >= 0:
            if ((rr*10+ss)) in wpList:
                break
            if ((rr*10+ss)) in bpList:
                if (rr*10+ss) == bkingList[0]:
                    bdonmove.append(dm)
                    break
                else:
                    break
            rr = rr - 1

    rr = r + 1
    while rr < 8:
        if (rr*10+ss) in wpList:
            status = 0
            wsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in bpList:
            status = 1
            dm = (rr*10+ss)
            wqm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
            if (rr*10+ss) == bkingList[0]:
                for x in range(number+10 , (rr*10+ss) , 10 ):# special #chb
                    wchb.append(x)
                wchtlist.append(number)
                wsp.append((rr+1)*10+ss)
            break
        elif rr == r:
            rr = rr + 1
            continue
        else:
            wqm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr + 1
    if bkingList [0] == dm:# dm ...................
        1+1
    elif status == 1 :
        rr = rr + 1
        while rr < 8:
            if ((rr*10+ss)) in wpList:
                break
            if ((rr*10+ss)) in bpList:
                if (rr*10+ss) == bkingList[0]:
                    bdonmove.append(dm)
                    break
                else:
                    break
            rr = rr + 1
    ss = s + 1
    rr = r + 1
    #negetive d----------------------------------------------------------
    while rr < 8 and ss<8:
        if (rr*10+ss) in wpList:
            status = 0
            wsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in bpList:
            status = 1
            dm = (rr*10+ss)
            wqm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
            if (rr*10+ss) == bkingList[0]:
                for x in range(number+1 , (rr*10+ss) , 11 ):# special #chb
                    wchb.append(x)
                wchtlist.append(number)
                wsp.append((rr+1)*10+ss+1)
            break
        elif rr == r:
            rr = rr + 1
            ss = ss + 1
            continue
        else:
            wqm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr + 1
        ss = ss + 1
    if bkingList [0] == dm:# dm ...................
        1+1
    elif status == 1 :
        ss = ss + 1
        rr = rr + 1
        while rr < 8 and ss<8:
            if ((rr*10+ss)) in wpList:
                break
            if ((rr*10+ss)) in bpList:
                if (rr*10+ss) == bkingList[0]:
                    bdonmove.append(dm)
                    break
                else:
                    break
            ss = ss + 1
            rr = rr + 1
    ss = s - 1
    rr = r - 1
    while rr > -1 and ss > -1:
        if (rr*10+ss) in wpList:
            status = 0
            wsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in bpList:
            status = 1
            dm = (rr*10+ss)
            wqm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
            if (rr*10+ss) == bkingList[0]:
                for x in range(number-11 , (rr*10+ss) ,-11 ):# special #chb
                    wchb.append(x)
                wchtlist.append(number)
                wsp.append((rr-1)*10+ss-1)
            break
        elif rr == r:
            rr = rr - 1
            ss = ss - 1
            continue
        else:
            wqm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr - 1
        ss = ss - 1
    if bkingList [0] == dm:# dm ...................
        1+1
    elif status == 1 :
        ss = ss - 1
        rr = rr - 1
        while rr > -1 and ss > -1:
            if ((rr*10+ss)) in wpList:
                break
            if ((rr*10+ss)) in bpList:
                if (rr*10+ss) == bkingList[0]:
                    bdonmove.append(dm)
                    break
                else:
                    break
            ss = ss - 1
            rr = ss - 1
    ss = s + 1
    rr = r - 1
    #pos------------------------------------------------------------------
    while (rr > -1 and ss<8):
        if (rr*10+ss) in wpList:
            status = 0
            wsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in bpList:
            status = 0
            dm = (rr*10+ss)
            wqm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
            if (rr*10+ss) == bkingList[0]:
                for x in range( number-9 , rr*10+ss , -9):# special #chb
                    wchb.append(x)
                wchtlist.append(number)
                wsp.append((rr-1)*10+ss+1)
            break
        elif rr == r:
            rr = rr - 1
            ss = ss + 1
            continue
        else:
            wqm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr -1
        ss = ss + 1
    if bkingList [0] == dm:
        1+1
    elif status == 1 :
        rr = rr -1
        ss = ss + 1
        while rr > -1 and ss<8:
            if ((rr*10+ss)) in wpList:
                break
            if ((rr*10+ss)) in bpList:
                if (rr*10+ss) == bkingList[0]:
                    bdonmove.append(dm)
                    break
                else:
                    break
            rr = rr -1
            ss = ss + 1


    ss = s - 1
    rr = r + 1
    while (rr < 8 and ss > -1):
        if (rr*10+ss) in wpList:
            status = 0
            wsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in bpList:
            status = 1
            dm = (rr*10+ss)
            wqm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
            if (rr*10+ss) == bkingList[0]:
                for x in range(number+9 , (rr*10+ss) , 9 ):# special #chb
                    wchb.append(x)
                wchtlist.append(number)
                wsp.append((rr+1)*10+ss-1)
            break
        elif rr == r:
            rr = rr + 1
            ss = ss - 1
            continue
        else:
            wqm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr + 1
        ss = ss - 1
    if bkingList [0] == dm:# dm ...................
        1+1
    elif status == 1 :
        rr = rr + 1
        ss = ss - 1
        while rr < 8 and ss > -1:
            if ((rr*10+ss)) in wpList:
                break
            if ((rr*10+ss)) in bpList:
                if (rr*10+ss) == bkingList[0]:
                    bdonmove.append(dm)
                    break
                else:
                    break
            rr = rr + 1
            ss = ss - 1
    wqm.append(2000)
    wam.append(2000)
    am.append(2000)

#b queen board
for number in bqList:
    r = number // 10
    s = number % 10
    rr = r
    ss = s - 1

    #horizontal
    while ss >= 0:
        if (rr*10+ss) in bpList:
            status = 1
            bsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in wpList:
            status = 0
            dm = (rr*10+ss)
            bqm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
            if (rr*10+ss) == wkingList[0]:
                for x in range(rr*10+ss+1 , number ):# special #chb
                    bchb.append(x)
                bchtlist.append(number)
                bsp.append(rr*10+ss-1)
            break
        elif ss == s:
            ss = ss -1
            continue
        else:
            bqm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
        ss = ss - 1
    if wkingList [0] == dm:# dm ...................
        1+1
    elif status == 0 :
        ss = ss - 1
        while ss >= 0:
            if ((rr*10+ss)) in bpList:
                break
            if ((rr*10+ss)) in wpList:
                if (rr*10+ss) == wkingList[0]:
                    wdonmove.append(dm)
                    break
                else:
                    break
            ss = ss - 1
    ss = s + 1
    while ss < 8:
        if (rr*10+ss) in bpList:
            status = 1
            bsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in wpList:
            status = 0
            dm = (rr&10+ss)
            bqm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
            if (rr*10+ss) == wkingList[0]:
                for x in range( number + 1 , rr*10+ss):
                    bchb.append(x)
                bchtlist.append(number)
                bsp.append(rr*10+ss+1)
            break
        elif ss == s:
            ss = ss + 1
            continue
        else:
            bqm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
        ss = ss + 1
    if wkingList [0] == dm:# dm ...................
        1+1
    elif status == 0 :
        ss = ss + 1
        while ss < 8:
            if ((rr*10+ss)) in bpList:
                break
            if ((rr*10+ss)) in wpList:
                if (rr*10+ss) == wkingList[0]:
                    wdonmove.append(dm)
                    break
                else:
                    break
            ss = ss + 1
    ss = s
    rr = r - 1
    #vertical.......................................................
    while rr >= 0:
        if (rr*10+ss) in bpList:
            status = 1
            bsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in wpList:
            status = 0
            dm = (rr*10+ss)
            bqm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
            if (rr*10+ss) == wkingList[0]:
                bchtlist.append(number)
                for x in range(number-10 , (rr*10+ss) , -10 ):
                    bchb.append(x)
                bsp.append((rr-1)*10+ss)
            break
        elif rr == r:
            rr = rr -1
            continue
        else:
            bqm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr - 1
    if wkingList [0] == dm:# dm ...................
        1+1
    elif status == 0 :
        rr = rr - 1
        while rr >= 0:
            if ((rr*10+ss)) in bpList:
                break
            if ((rr*10+ss)) in wpList:
                if (rr*10+ss) == wkingList[0]:
                    wdonmove.append(dm)
                    break
                else:
                    break
            rr = rr - 1

    rr = r + 1
    while rr < 8:
        if (rr*10+ss) in bpList:
            status = 1
            bsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in wpList:
            status = 0
            dm = (rr*10+ss)
            bqm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
            if (rr*10+ss) == wkingList[0]:
                for x in range(number+10 , (rr*10+ss) , 10 ):# special #chb
                    bchb.append(x)
                bchtlist.append(number)
                bsp.append((rr+1)*10+ss)
            break
        elif rr == r:
            rr = rr + 1
            continue
        else:
            bqm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr + 1

    if wkingList [0] == dm:# dm ...................
        1+1
    elif status == 0 :
        rr = rr + 1
        while rr < 8:
            if ((rr*10+ss)) in bpList:
                break
            if ((rr*10+ss)) in wpList:
                if (rr*10+ss) == wkingList[0]:
                    wdonmove.append(dm)
                    break
                else:
                    break
            rr = rr + 1

    ss = s + 1
    rr = r + 1
    #negetive d-----------------------------------------
    while rr < 8 and ss<8:
        if (rr*10+ss) in bpList:
            status = 1
            bsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in wpList:
            status = 0
            dm = (rr*10+ss)
            bqm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
            if (rr*10+ss) == wkingList[0]:
                for x in range(number+11 , (rr*10+ss) , 11 ):# special #chb
                    bchb.append(x)
                bchtlist.append(number)
                bsp.append((rr+1)*10+ss+1)
            break
        elif rr == r:
            rr = rr + 1
            ss = ss + 1
            continue
        else:
            bqm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr + 1
        ss = ss + 1

    if wkingList [0] == dm:# dm ...................
        1+1
    elif status == 0 :
        ss = ss + 1
        rr = rr + 1
        while rr < 8 and ss<8:
            if ((rr*10+ss)) in bpList:
                break
            if ((rr*10+ss)) in wpList:
                if (rr*10+ss) == wkingList[0]:
                    wdonmove.append(dm)
                    break
                else:
                    break
            ss = ss + 1
            rr = rr + 1

    ss = s - 1
    rr = r - 1
    while rr > -1 and ss > -1:
        if (rr*10+ss) in bpList:
            status = 1
            bsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in wpList:
            status = 0
            dm = (rr*10+ss)
            bqm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
            if (rr*10+ss) == wkingList[0]:
                for x in range(number-11 , (rr*10+ss) ,-11 ):# special #chb
                    bchb.append(x)
                bchtlist.append(number)
                bsp.append((rr-1)*10+ss-1)
            break
        elif rr == r:
            rr = rr - 1
            ss = ss - 1
            continue
        else:
            bqm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr - 1
        ss = ss - 1

    if wkingList [0] == dm:# dm ...................
        1+1
    elif status == 0 :
        ss = ss - 1
        rr = rr - 1
        while rr > -1 and ss > -1:
            if ((rr*10+ss)) in wpList:
                break
            if ((rr*10+ss)) in bpList:
                if (rr*10+ss) == wkingList[0]:
                    wdonmove.append(dm)
                    break
                else:
                    break
            ss = ss - 1
            rr = ss - 1

    ss = s + 1
    rr = r - 1
    #pos------------------------------------------------
    while (rr > -1 and ss<8):
        if (rr*10+ss) in bpList:
            status = 1
            bsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in wpList:
            status = 0
            dm = (rr*10+ss)
            bqm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
            if (rr*10+ss) == wkingList[0]:
                for x in range( number-9 , rr*10+ss , -9):# special #chb
                    bchb.append(x)
                bchtlist.append(number)
                bsp.append((rr-1)*10+ss+1)
            break
        elif rr == r:
            rr = rr - 1
            ss = ss + 1
            continue
        else:
            bqm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr -1
        ss = ss + 1

    if wkingList [0] == dm:#dm .................
        1+1
    elif status == 0 :
        rr = rr -1
        ss = ss + 1
        while rr > -1 and ss<8:
            if ((rr*10+ss)) in bpList:
                break
            if ((rr*10+ss)) in wpList:
                if (rr*10+ss) == wkingList[0]:
                    wdonmove.append(dm)
                    break
                else:
                    break
            rr = rr -1
            ss = ss + 1

    ss = s - 1
    rr = r + 1
    while (rr < 8 and ss > -1):
        if (rr*10+ss) in bpList:
            status = 1
            bsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in wpList:
            status = 0
            dm = rr*10+ss
            bqm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
            if (rr*10+ss) == wkingList[0]:
                for x in range(number+9 , (rr*10+ss) , 9 ):# special #chb
                    bchb.append(x)
                bchtlist.append(number)
                bsp.append((rr+1)*10+ss-1)
            break
        elif rr == r:
            rr = rr + 1
            ss = ss - 1
            continue
        else:
            bqm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr + 1
        ss = ss - 1

    if wkingList [0] == dm:# dm ...................
        1+1
    elif status == 0 :
        rr = rr + 1
        ss = ss - 1
        while rr < 8 and ss > -1:
            if ((rr*10+ss)) in bpList:
                break
            if ((rr*10+ss)) in wpList:
                if (rr*10+ss) == wkingList[0]:
                    wdonmove.append(dm)
                    break
                else:
                    break
            rr = rr + 1
            ss = ss - 1

    bqm.append(2000)
    bam.append(2000)
    am.append(2000)

#white knight board
for number in wkList:
    rs = number
    r = rs // 10
    s = rs % 10
    i1 = (r - 2) * 10 + s - 1
    i2 = (r - 2) * 10 + s + 1
    i3 = (r - 1) * 10 + s - 2
    i4 = (r - 1) * 10 + s + 2#
    i5 = (r + 1) * 10 + s - 2
    i6 = (r + 1) * 10 + s + 1
    i7 = (r + 2) * 10 + s - 1
    i8 = (r + 2) * 10 + s + 1
    ilist = [i1 , i2 , i3 , i4 , i5 , i6 , i7 , i8]
    for i in ilist:
        if i < 0 or i>77 or (i%10)>7 or (i//10)>7:
            continue
        if i in wpList:
            wsp.append(i)
        if i == bkingList[0]:
            wchtlist.append(number)
        wkm.append(i)
        wam.append(i)
        am.append(i)
    wkm.append(2000)
    wam.append(2000)
    am.append(2000)

#black knight moves
for number in bkList:
    rs = number
    r = rs // 10
    s = rs % 10
    i1 = (r - 2) * 10 + s - 1
    i2 = (r - 2) * 10 + s + 1
    i3 = (r - 1) * 10 + s - 2
    i4 = (r - 1) * 10 + s + 2
    i5 = (r + 1) * 10 + s - 2
    i6 = (r + 1) * 10 + s + 2
    i7 = (r + 2) * 10 + s - 1
    i8 = (r + 2) * 10 + s + 1
    ilist = [i1 , i2 , i3 , i4 , i5 , i6 , i7 , i8]
    for i in ilist:
        if i < 0 or i>77 or (i%10)>7 or (i//10)>7 :
            continue
        if i in bpList:
            bsp.append(i)
        else:
            if i == wkingList[0]:
                bchtlist.append(number)
        bkm.append(i)
        bam.append(i)
        am.append(i)
    bkm.append(2000)
    bam.append(2000)
    am.append(2000)

#white bishops board
for number in wbList:
    r = number // 10
    s = number % 10
    rr = r + 1
    ss = s + 1
    #negetive d----------------------------------------------------------
    while rr < 8 and ss<8:
        if (rr*10+ss) in wpList:
            status = 0
            wsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in bpList:
            status = 1
            dm = rr*10+ss
            if (rr*10+ss) == bkingList[0]:
                for x in range(number+11 , (rr*10+ss) , 11 ):# special #chb
                    wchb.append(x)
                wchtlist.append(number)
                wsp.append((rr+1)*10+ss+1)
            wbm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
            break
        elif rr == r:
            rr = rr + 1
            ss = ss + 1
            continue
        else:
            wbm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr + 1
        ss = ss + 1

    if bkingList [0] == dm:# dm ...................
        1+1
    elif status == 1 :
        ss = ss + 1
        rr = rr + 1
        while rr < 8 and ss<8:
            if ((rr*10+ss)) in wpList:
                break
            if ((rr*10+ss)) in bpList:
                if (rr*10+ss) == bkingList[0]:
                    bdonmove.append(dm)
                    break
                else:
                    break
            ss = ss + 1
            rr = rr + 1

    ss = s - 1
    rr = r - 1
    while rr > -1 and ss > -1:
        if (rr*10+ss) in wpList:
            status = 0
            wsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in bpList:
            if (rr*10+ss) == bkingList[0]:
                for x in range(number-11 , (rr*10+ss) ,-11 ):# special #chb
                    wchb.append(x)
                wchtlist.append(number)
                wsp.append((rr-1)*10+ss-1)
            wbm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
            break
        elif rr == r:
            rr = rr - 1
            ss = ss - 1
            continue
        else:
            wbm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr - 1
        ss = ss - 1

    if bkingList [0] == dm:# dm ...................
        1+1
    elif status == 1 :
        ss = ss - 1
        rr = rr - 1
        while rr > -1 and ss > -1:
            if ((rr*10+ss)) in wpList:
                break
            if ((rr*10+ss)) in bpList:
                if (rr*10+ss) == bkingList[0]:
                    bdonmove.append(dm)
                    break
                else:
                    break
            ss = ss - 1
            rr = ss - 1

    ss = s + 1
    rr = r - 1
    #pos------------------------------------------------------------------
    while (rr > -1 and ss<8):
        if (rr*10+ss) in wpList:
            status = 0
            wsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in bpList:
            status = 1
            dm = (rr*10+ss)
            if (rr*10+ss) == bkingList[0]:
                for x in range( number-9 , rr*10+ss , -9):# special #chb
                    wchb.append(x)
                wchtlist.append(number)
                wsp.append((rr-1)*10+ss+1)
            wbm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
            break
        elif rr == r:
            rr = rr - 1
            ss = ss + 1
            continue
        else:
            wbm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr -1
        ss = ss + 1
    
    if bkingList [0] == dm:
        1+1
    elif status == 1 :
        rr = rr -1
        ss = ss + 1
        while rr > -1 and ss<8:
            if ((rr*10+ss)) in wpList:
                break
            if ((rr*10+ss)) in bpList:
                if (rr*10+ss) == bkingList[0]:
                    bdonmove.append(dm)
                    break
                else:
                    break
            rr = rr -1
            ss = ss + 1

    ss = s - 1
    rr = r + 1
    while (rr < 8 and ss > -1):
        if (rr*10+ss) in wpList:
            status = 0
            wsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in bpList:
            status = 1
            dm = (rr*10+ss)
            if (rr*10+ss) == bkingList[0]:
                for x in range(number+9 , (rr*10+ss) , 9 ):# special #chb
                    wchb.append(x)
                wchtlist.append(number)
                wsp.append((rr+1)*10+ss-1)
            wbm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
            break
        elif rr == r:
            rr = rr + 1
            ss = ss - 1
            continue
        else:
            wbm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr + 1
        ss = ss - 1

    if bkingList [0] == dm:# dm ...................
        1+1
    elif status == 1 :
        rr = rr + 1
        ss = ss - 1
        while rr < 8 and ss > -1:
            if ((rr*10+ss)) in wpList:
                break
            if ((rr*10+ss)) in bpList:
                if (rr*10+ss) == bkingList[0]:
                    bdonmove.append(dm)
                    break
                else:
                    break
            rr = rr + 1
            ss = ss - 1

    wbm.append(2000)
    wam.append(2000)
    am.append(2000)

#black bishops board
for number in bbList:
    r = number // 10
    s = number % 10
    rr = r + 1
    ss = s + 1

    #negetive d-----------------------------------------
    while rr < 8 and ss<8:
        if (rr*10+ss) in bpList:
            status = 1
            bsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in wpList:
            status = 0
            dm = (rr*10+ss)
            if (rr*10+ss) == wkingList[0]:
                for x in range(number+11 , (rr*10+ss) , 11 ):# special #chb
                    bchb.append(x)
                bchtlist.append(number)
                bsp.append((rr+1)*10+ss+1)
            bbm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
            break
        elif rr == r:
            rr = rr + 1
            ss = ss + 1
            continue
        else:
            bbm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr + 1
        ss = ss + 1

    if wkingList [0] == dm:# dm ...................
        1+1
    elif status == 0 :
        ss = ss + 1
        rr = rr + 1
        while rr < 8 and ss<8:
            if ((rr*10+ss)) in bpList:
                break
            if ((rr*10+ss)) in wpList:
                if (rr*10+ss) == wkingList[0]:
                    wdonmove.append(dm)
                    break
                else:
                    break
            ss = ss + 1
            rr = rr + 1

    ss = s - 1
    rr = r - 1
    while rr > -1 and ss > -1:
        if (rr*10+ss) in bpList:
            status = 1
            bsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in wpList:
            status = 0
            dm = (rr*10+ss)
            if (rr*10+ss) == wkingList[0]:
                for x in range(number-11 , (rr*10+ss) ,-11 ):# special #chb
                    bchb.append(x)
                bchtlist.append(number)
                bsp.append((rr-1)*10+ss-1)
            bbm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
            break
        elif rr == r:
            rr = rr - 1
            ss = ss - 1
            continue
        else:
            bbm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr - 1
        ss = ss - 1

    if wkingList [0] == dm:# dm ...................
        1+1
    elif status == 0 :
        ss = ss - 1
        rr = rr - 1
        while rr > -1 and ss > -1:
            if ((rr*10+ss)) in wpList:
                break
            if ((rr*10+ss)) in bpList:
                if (rr*10+ss) == wkingList[0]:
                    wdonmove.append(dm)
                    break
                else:
                    break
            ss = ss - 1
            rr = ss - 1

    ss = s + 1
    rr = r - 1
    #pos------------------------------------------------
    while (rr > -1 and ss<8):
        if (rr*10+ss) in bpList:
            status = 1
            bsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in wpList:
            status = 0
            dm = rr*10+ss
            if (rr*10+ss) == wkingList[0]:
                for x in range( number-9 , rr*10+ss , -9):# special #chb
                    bchb.append(x)
                bchtlist.append(number)
                bsp.append((rr-1)*10+ss+1)
            bbm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
            break
        elif rr == r:
            rr = rr - 1
            ss = ss + 1
            continue
        else:
            bbm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr -1
        ss = ss + 1

    if wkingList [0] == dm:#dm .................
        1+1
    elif status == 0 :
        rr = rr -1
        ss = ss + 1
        while rr > -1 and ss<8:
            if ((rr*10+ss)) in bpList:
                break
            if ((rr*10+ss)) in wpList:
                if (rr*10+ss) == wkingList[0]:
                    wdonmove.append(dm)
                    break
                else:
                    break
            rr = rr -1
            ss = ss + 1

    ss = s - 1
    rr = r + 1
    while (rr < 8 and ss > -1):
        if (rr*10+ss) in bpList:
            status = 1
            bsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in wpList:
            status = 0
            dm = (rr*10+ss)
            if (rr*10+ss) == wkingList[0]:
                for x in range(number+9 , (rr*10+ss) , 9 ):# special #chb
                    bchb.append(x)
                bchtlist.append(number)
                bsp.append((rr+1)*10+ss-1)
            bbm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
            break
        elif rr == r:
            rr = rr + 1
            ss = ss - 1
            continue
        else:
            bbm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr + 1
        ss = ss - 1

    if wkingList [0] == dm:# dm ...................
        1+1
    elif status == 0 :
        rr = rr + 1
        ss = ss - 1
        while rr < 8 and ss > -1:
            if ((rr*10+ss)) in bpList:
                break
            if ((rr*10+ss)) in wpList:
                if (rr*10+ss) == wkingList[0]:
                    wdonmove.append(dm)
                    break
                else:
                    break
            rr = rr + 1
            ss = ss - 1

    bbm.append(2000)
    bam.append(2000)
    am.append(2000)

#black rooks board
for number in brList:
    r = number // 10
    s = number % 10
    rr = r
    ss = s - 1

    #horizontal
    while ss >= 0:
        if (rr*10+ss) in bpList:
            status = 1
            bsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in wpList:
            status = 0
            dm = (rr*10+ss)
            if (rr*10+ss) == wkingList[0]:
                bchtlist.append(number)
                for x in range(rr*10+ss+1 , number ):# special #chb
                    bchb.append(x)
                    bsp.append(rr*10+ss-1)
            brm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
            break
        elif ss == s:
            ss = ss -1
            continue
        else:
            brm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
        ss = ss - 1

    if wkingList [0] == dm:# dm ...................
        1+1
    elif status == 0 :
        ss = ss - 1
        while ss >= 0:
            if ((rr*10+ss)) in bpList:
                break
            if ((rr*10+ss)) in wpList:
                if (rr*10+ss) == wkingList[0]:
                    wdonmove.append(dm)
                    break
                else:
                    break
            ss = ss - 1

    ss = s + 1
    while ss < 8:
        if (rr*10+ss) in bpList:
            status = 1
            bsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in wpList:
            status = 0
            dm = (rr*10+ss)
            if (rr*10+ss) == wkingList[0]:
                for x in range( number + 1 , rr*10+ss):
                    bchb.append(x)
                bchtlist.append(number)
                bsp.append(rr*10+ss+1)
            brm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
            break
        elif ss == s:
            ss = ss + 1
            continue
        else:
            brm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
        ss = ss + 1

    if wkingList [0] == dm:# dm ...................
        1+1
    elif status == 0 :
        ss = ss + 1
        while ss < 8:
            if ((rr*10+ss)) in bpList:
                break
            if ((rr*10+ss)) in wpList:
                if (rr*10+ss) == wkingList[0]:
                    wdonmove.append(dm)
                    break
                else:
                    break
            ss = ss + 1

    ss = s
    rr = r - 1
    #vertical--------------------------------------
    while rr >= 0:
        if (rr*10+ss) in bpList:
            status = 1
            bsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in wpList:
            status = 0
            dm = rr*10+ss
            if (rr*10+ss) == wkingList[0]:
                for x in range(number-10 , (rr*10+ss) , -10 ):
                    bchb.append(x)
                bchtlist.append(number)
                bsp.append((rr-1)*10+ss)
            brm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
            break
        elif rr == r:
            rr = rr - 1
            continue
        else:
            brm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr - 1

    if wkingList [0] == dm:# dm ...................
        1+1
    elif status == 0 :
        rr = rr - 1
        while rr >= 0:
            if ((rr*10+ss)) in bpList:
                break
            if ((rr*10+ss)) in wpList:
                if (rr*10+ss) == wkingList[0]:
                    wdonmove.append(dm)
                    break
                else:
                    break
            rr = rr - 1

    rr = r + 1
    while rr < 8:
        if (rr*10+ss) in bpList:
            status = 1
            bsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in wpList:
            status = 0
            dm = rr*10+ss
            if (rr*10+ss) == wkingList[0]:
                for x in range(number+10 , (rr*10+ss) , 10 ):# special #chb
                    bchb.append(x)
                bchtlist.append(number)
                bsp.append((rr+1)*10+ss)
            brm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
            break
        elif rr == r:
            rr = rr + 1
            continue
        else:
            brm.append((rr*10+ss))
            bam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr + 1
    
    if wkingList [0] == dm:# dm ...................
        1+1
    elif status == 0 :
        rr = rr + 1
        while rr < 8:
            if ((rr*10+ss)) in bpList:
                break
            if ((rr*10+ss)) in wpList:
                if (rr*10+ss) == wkingList[0]:
                    wdonmove.append(dm)
                    break
                else:
                    break
            rr = rr + 1

    brm.append(2000)
    bam.append(2000)
    am.append(2000)
    
#white rooks board
for number in wrList:
    r = number // 10
    s = number % 10
    rr = r
    ss = s - 1

    #horizontal-----------------------------------------------
    while ss >= 0:
        if (rr*10+ss) in wpList:
            status = 0
            wsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in bpList:
            status = 1
            dm = rr*10+ss
            if (rr*10+ss) == bkingList[0]:
                for x in range(rr*10+ss+1 , number ):# special #chb
                    wchb.append(x)
                wchtlist.append(number)
                wsp.append(rr*10+ss-1)
            wrm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
            break
        elif ss == s:
            ss = ss -1
            continue
        else:
            wrm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
        ss = ss - 1

    if bkingList [0] == dm:# dm ...................
        1+1
    elif status == 1 :
        ss = ss - 1
        while ss >= 0:
            if ((rr*10+ss)) in wpList:
                break
            if ((rr*10+ss)) in bpList:
                if (rr*10+ss) == bkingList[0]:
                    bdonmove.append(dm)
                    break
                else:
                    break
            ss = ss - 1

    ss = s + 1
    while ss < 8:
        if (rr*10+ss) in wpList:
            status = 0
            wsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in bpList:
            status = 1
            dm = rr*10+ss
            if (rr*10+ss) == bkingList[0]:
                wchtlist.append(number)
                for x in range( number + 1 , rr*10+ss):
                    wchb.append(x)
                bsp.append(rr*10+ss+1)
            wrm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
            break
        elif ss == s:
            ss = ss + 1
            continue
        else:
            wrm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
        ss = ss + 1

    if bkingList [0] == dm:# dm ...................
        1+1
    elif status == 1 :
        ss = ss + 1
        while ss < 8:
            if ((rr*10+ss)) in wpList:
                break
            if ((rr*10+ss)) in bpList:
                if (rr*10+ss) == bkingList[0]:
                    bdonmove.append(dm)
                    break
                else:
                    break
            ss = ss + 1

    ss = s
    rr = r - 1
    #vertical--------------------------------------------------------
    while rr >= 0:
        if (rr*10+ss) in wpList:
            status = 0
            wsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in bpList:
            status = 1
            dm = rr*10+ss
            if (rr*10+ss) == bkingList[0]:
                for x in range(number-10 , (rr*10+ss) , -10 ):
                    wchb.append(x)
                wchtlist.append(number)
                bsp.append((rr-1)*10+ss)
            wrm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
            break
        elif rr == r:
            rr = rr - 1
            continue
        else:
            wrm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr - 1

    if bkingList [0] == dm:# dm ...................
        1+1
    elif status == 1 :
        rr = rr - 1
        while rr >= 0:
            if ((rr*10+ss)) in wpList:
                break
            if ((rr*10+ss)) in bpList:
                if (rr*10+ss) == bkingList[0]:
                    bdonmove.append(dm)
                    break
                else:
                    break
            rr = rr - 1

    rr = r + 1
    while rr < 8:
        if (rr*10+ss) in wpList:
            status = 0
            wsp.append(rr*10+ss)
            break
        elif (rr*10+ss) in bpList:
            status = 1
            dm = rr*10+ss
            if (rr*10+ss) == bkingList[0]:
                for x in range(number+10 , (rr*10+ss) , 10 ):# special #chb
                    wchb.append(x)
                wchtlist.append(number)
                bsp.append((rr+1)*10+ss)
            wrm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
            break
        elif rr == r:
            rr = rr + 1
            continue
        else:
            wrm.append((rr*10+ss))
            wam.append((rr*10+ss))
            am.append((rr*10+ss))
        rr = rr + 1

    if bkingList [0] == dm:# dm ...................
        1+1
    elif status == 1 :
        rr = rr + 1
        while rr < 8:
            if ((rr*10+ss)) in wpList:
                break
            if ((rr*10+ss)) in bpList:
                if (rr*10+ss) == bkingList[0]:
                    bdonmove.append(dm)
                    break
                else:
                    break
            rr = rr + 1
    wrm.append(2000)
    wam.append(2000)
    am.append(2000)

#white pwans board and attack
for number in wpawnList:
    r = number // 10
    s = number % 10
    rr = r
    ss = s

    if rr == 6:#پرشی....................................
        if ((rr-1)*10+ss) in wpList:
            1+1
        elif ((rr-1)*10+ss) in bpList:
            1+1
        elif ((rr-1)*10+ss) >-1 and ((rr-1)*10+ss)<78 and (((rr-1)*10+ss)%10)<8 :
            wpm.append((rr-1)*10+ss)
            #wam.append((rr+1)*10+ss)
            #am.append((rr+1)*10+ss)
            if ((rr-2)*10+ss) in wpList:
                1+1
            elif ((rr-2)*10+ss) in bpList:
                1+1
            elif ((rr-1)*10+ss) >-1 and ((rr-1)*10+ss)<78 and (((rr-1)*10+ss)%10)<8 :
                wpm.append((rr-2)*10+ss)
                #wam.append((rr+2)*10+ss)
                #am.append((rr+2)*10+ss)
    else:#ساده..............................................
        if rr == 0:
            1+1
        elif ((rr-1)*10+ss) in wpList:
            1+1
        elif ((rr-1)*10+ss) in bpList:
            1+1
        elif ((rr-1)*10+ss) >-1 and ((rr-1)*10+ss)<78 and (((rr-1)*10+ss)%10)<8 :
            wpm.append((rr-1)*10+ss)
            #wam.append((rr+1)*10+ss)
            #am.append((rr+1)*10+ss)
    if ((rr-1)*10+ss-1) in bpList:#زدنی...............................
        if ((rr-1)*10+ss-1) == bkingList[0]:
            wchtlist.append((rr-1)*10+ss-1)
        wpattack.append((rr-1)*10+ss-1)
        wam.append((rr-1)*10+ss-1)
        am.append((rr-1)*10+ss-1)
    
    wsp.append((rr-1)*10+ss-1)

    if ((rr-1)*10+ss+1) in bpList:
        if ((rr-1)*10+ss+1) == bkingList[0]:
            wchtlist.append((rr-1)*10+ss+1)
        wpattack.append((rr-1)*10+ss+1)
        wam.append((rr-1)*10+ss+1)
        am.append((rr-1)*10+ss+1)
    
    wsp.append((rr-1)*10+ss+1)
    wpm.append(2000)
    wpattack.append(2000)
    wam.append(2000)
    am.append(2000)

#black pawn board
for number in bpawnList:
    r = number // 10
    s = number % 10
    rr = r
    ss = s

    if rr == 1:#پرشی
        #کنترل درون کادر و وجود بلاک را اضافه کن
        if ((rr+1)*10+ss) in wpList:
            1+1
        elif ((rr+1)*10+ss) in bpList:
            1+1
        elif ((rr+1)*10+ss) >-1 and ((rr+1)*10+ss)<78 and (((rr+1)*10+ss)%10)<8 :
            bpm.append((rr+1)*10+ss)
            #bam.append((rr-1)*10+ss)
            #am.append((rr-1)*10+ss)
            if ((rr+2)*10+ss) in wpList:
                1+1
            elif ((rr+2)*10+ss) in bpList:
                1+1
            elif ((rr+2)*10+ss) > -1 and ((rr+2)*10+ss)<78 and (((rr+2)*10+ss)%10)<8 :
                bpm.append((rr+2)*10+ss)
                #bam.append((rr-2)*10+ss)
                #am.append((rr-2)*10+ss)
    else:#ساده
        if rr == 7:
            1+1
        elif ((rr+1)*10+ss) in wpList:
            1+1
        elif ((rr+1)*10+ss) in bpList:
            1+1
        elif ((rr+1)*10+ss) >-1 and ((rr+1)*10+ss)<78 and (((rr+1)*10+ss)%10)<8 :
            bpm.append((rr+1)*10+ss)
            #bam.append((rr-1)*10+ss)
            #am.append((rr-1)*10+ss)
    if ((rr+1)*10+ss-1) in wpList:#attack.........................
        if ((rr+1)*10+ss-1) == wkingList[0]:
            bchtlist.append((rr+1)*10+ss-1)
        bpattack.append((rr+1)*10+ss-1)
        bam.append((rr+1)*10+ss-1)
        am.append((rr+1)*10+ss-1)
    
    bsp.append((rr+1)*10+ss-1)

    if ((rr+1)*10+ss+1) in wpList:
        if ((rr+1)*10+ss+1) == wkingList[0]:
            bchtlist.append((rr+1)*10+ss+1)
        bpattack.append((rr+1)*10+ss+1)
        bam.append((rr+1)*10+ss+1)
        am.append((rr+1)*10+ss+1)
    
    bsp.append((rr+1)*10+ss+1)
    bpm.append(2000)
    bpattack.append(2000)
    bam.append(2000)
    am.append(2000)



#---------------------------------------------------------------------------------------------------
if len(wchtlist) == 0:
    wchtlist = [4000]
if len(bchtlist) == 0:
    bchtlist = [4000]

i=0
for x in brm:# black rooks  Remove&Block.........................
    if x == 2000:
        i = i + 1
    if x == wchtlist[0]:
        if brList[i] in bdonmove:
            1+1
        else:
            bchremover.append(brList[i])
    if x in wchb:
        if brList[i] in bdonmove:
            1+1
        else:
            bchblocker.append(brList[i])

i=0
for x in wrm:# white.
    if x == 2000:
        i = i + 1
    if x == bchtlist[0]:
        if wrList[i] in wdonmove:
            1+1
        else:
            wchremover.append(wrList[i])
    if x in bchb:
        if wrList[i] in wdonmove:
            1+1
        else:
            wchblocker.append(wrList[i])

i=0#         black bishops  R&B.........................
for x in bbm:
    if x == 2000:
        i = i + 1
    if x == wchtlist[0]:
        if bbList[i] in bdonmove:
            1+1
        else:
            bchremover.append(bbList[i])
    if x in wchb:
        if bbList[i] in bdonmove:
            1+1
        else:
            bchblocker.append(bbList[i])

i=0
for x in wbm:# white.
    if x == 2000:
        i = i + 1
    if x == bchtlist[0]:
        if wbList[i] in wdonmove:
            1+1
        else:
            wchremover.append(wbList[i])
    if x in bchb:
        if wbList[i] in wdonmove:
            1+1
        else:
            wchblocker.append(wbList[i])

i=0
for x in bkm:# black knights  R&B.........................
    if x == 2000:
        i = i + 1
    if x == wchtlist[0]:
        if bkList[i] in bdonmove:
            1+1
        else:
            bchremover.append(bkList[i])
    if x in wchb:
        if bkList[i] in bdonmove:
            1+1
        else:
            bchblocker.append(bkList[i])

i=0
for x in wkm:# white.
    if x == 2000:
        i = i + 1
    if x == bchtlist[0]:
        if wkList[i] in wdonmove:
            1+1
        else:
            wchremover.append(wkList[i])
    if x in bchb:
        if wkList[i] in wdonmove:
            1+1
        else:
            wchblocker.append(wkList[i])

i=0
for x in bqm:# black queen  R&B.........................
    if x == 2000:
        i = i + 1
    if x == wchtlist[0]:
        if bqList[i] in bdonmove:
            1+1
        else:
            bchremover.append(bqList[i])
    if x in wchb:
        if bqList[i] in bdonmove:
            1+1
        else:
            bchblocker.append(bqList[i])

i=0
for x in wqm:# white.
    if x == 2000:
        i = i + 1
    if x == bchtlist[0]:
        if wqList[i] in wdonmove:
            1+1
        else:
            wchremover.append(wqList[i])
    if x in bchb:
        if wqList[i] in wdonmove:
            1+1
        else:
            wchblocker.append(wqList[i])

i=0
for x in bpattack:# black pawns  R.........................
    if x == 2000:
        i = i + 1
    if x == wchtlist[0]:
        if bpawnList[i] in bdonmove:
            1+1
        else:
            bchremover.append(bpawnList[i])
i=0
for x in wpattack:# white.........................
    if x == 2000:
        i = i + 1
    if x == bchtlist[0]:
        if wpawnList[i] in wdonmove:
            1+1
        else:
            wchremover.append(wpawnList[i])


i=0
for x in bpm:# black pawns B..........................
    if x == 2000:
        i = i + 1
    if x in wchb:
        if bpawnList[i] in bdonmove:
            1+1
        else:
            bchblocker.append(bpawnList[i])

i=0
for x in wpm:# white.
    if x == 2000:
        i = i + 1
    if x in bchb:
        if wpawnList[i] in wdonmove:
            1+1
        else:
            wchblocker.append(wpawnList[i])


print("")
print("")
#............................................................................................................
print("***  black king check check!   ***")
if wchtlist[0] != 4000:
    if len(wchtlist) == 1:#     Wcht = 1 
        print(f"black king is in check by{wchtlist}")
        #TO MOVE.......................
        for x in bkingm:
            if x in wam or x in wsp:
                1+1
            else:
                bkingPM.append(x)

        if len(bkingPM) == 0:
            print("black king cant move!")
        else:
            print(f"black king can move to {bkingPM} so its not mate")
        
        #to hit with king
        if wchtlist[0] in bkingm:
            if wchtlist[0] in wsp:
                1+1
            else:
                print("black king can hit the checker!so its not mate")
                hold = 1
        
        #to remove
        if len(bchremover)>0:
            print(f"this black pieces({bchremover})can remove checker({wchtlist[0]})so its not mate")

        #to block
        if len(bchblocker)>0:
            print(f"this black pieces({bchblocker})can block checker({wchtlist[0]})so its not mate")
        
        #final result
        if len(bchblocker)<1 and len(bchblocker)<1 and hold != 1 and len(bkingPM)<1:
            print("black king is mate!")
        else:
            print("black king is Not mate")
elif len(wchtlist) == 1:
    print("black king is not in check")

if len(wchtlist)>1: #wcht > 1
    print(f"black king is in check by{wchtlist}")
    #TO MOVE.......................
    for x in bkingm:
        if x in wam or x in wsp:
            1+1
        else:
            bkingPM.append(x)

    if len(bkingPM) == 0:
        print("black king cant move! its mate")
    else:
        print(f"black king can move to {bkingPM}its not mate!")


if len(wchtlist) == 0:
    print("black king is not in check")

print("")
print("")
#------------------------------------------------------------------
hold = 0
print("***  white king check check!   ***")
if bchtlist [0] != 4000:
    if len(bchtlist) == 1:#                          bcht = 1 
        print(f"white king is in check by{bchtlist}")
        #TO MOVE.......................
        for x in wkingm:
            if x in bam or x in bsp:
                1+1
            else:
                wkingPM.append(x)

        if len(wkingPM) == 0:
            print("white king cant move!")
        else:
            print(f"white king can move to {wkingPM} and is not mate")
        
        #to hit with king
        if bchtlist[0] in wkingm:
            if bchtlist[0] in bsp:
                1+1
            else:
                print("white king can hit the checker!so its not mate")
                hold = 1
        
        #to remove
        if len(wchremover)>0:
            print(f"this white pieces({wchremover})can remove checker({bchtlist[0]}) so its not mate")

        #to block
        if len(wchblocker)>0:
            print(f"this white pieces({wchblocker})can block checker({bchtlist[0]}) so its not mate")
        
        if len(wchblocker)<1 and len(wchblocker)<1 and hold != 1 and len(wkingPM)<1:
            print("white king is mate!")
        else:
            print("white king is Not mate")
elif len(wchtlist) == 1:
    print("white king is not in check")


if len(bchtlist)>1: #bcht > 1
    #TO MOVE.......................
    for x in bkingm:
        if x in bam or x in bsp:
            1+1
        else:
            wkingPM.append(x)

    if len(bkingPM) == 0:
        print("white king cant move! its mate!")
    else:
        print(f"white king can move to {bkingPM}its not mate!")


if len(bchtlist) == 0:
    print("white king is not in check")

print("")