def sudoku(size):
    import time
    start_time=time.time()

    import sys
    import random as rn
    mydict = {}
    n = 0
    print ('--started calculating--')
    while len(mydict) < 9:
        n += 1
        x = range(1, size+1)
        testlist = rn.sample(x, len(x))

        isgood = True
        for dictid,savedlist in mydict.items():
            if isgood == False:
                break
            for v in savedlist:
                if testlist[savedlist.index(v)] == v:
                    isgood = False
                    break

        if isgood == True:
            isgoodafterduplicatecheck = True
            mod = len(mydict) % 3
            dsavedlists = {}
            dtestlists = {}
            dcombindedlists = {}
            for a in range(1,mod + 1):
                savedlist = mydict[len(mydict) - a]               
                for v1 in savedlist:
                    modsavedlists = (savedlist.index(v1) / 3) % 3
                    dsavedlists[len(dsavedlists)] = [modsavedlists,v1]
                for t1 in testlist:
                    modtestlists = (testlist.index(t1) / 3) % 3
                    dtestlists[len(dtestlists)] = [modtestlists,t1]
                for k,v2 in dsavedlists.items():
                    dcombindedlists[len(dcombindedlists)] = v2
                    dcombindedlists[len(dcombindedlists)] = dtestlists[k]
            vsave = 0
            lst1 = []
            for k, vx in dcombindedlists.items():
                vnew = vx[0]
                if not vnew == vsave:
                    lst1 = []
                    lst1.append(vx[1])
                else:
                    if vx[1] in lst1:
                        isgoodafterduplicatecheck = False
                        break
                    else:
                        lst1.append(vx[1])
                vsave = vnew

            if isgoodafterduplicatecheck == True:

                mydict[len(mydict)] = testlist
                print ('success found', len(mydict), 'row')   

    print ('--finished calculating--')
    total_time = time.time()-start_time
    return mydict, n, total_time

return_dict, total_tries, amt_of_time = sudoku(9)
print ('')
print ('--printing output--')
for n,v in return_dict.items():
    print (n,v)
print ('process took',total_tries,'tries in', round(amt_of_time,2), 'secs')
print ('-------------------')

from random import sample
base  = 3  # Will generate any size of random sudoku board in O(n^2) time
side  = base*base
nums  = sample(range(1,side+1),side) # random numbers
board = [[nums[(base*(r%base)+r//base+c)%side] for c in range(side) ] for r in range(side)]
rows  = [ r for g in sample(range(base),base) for r in sample(range(g*base,(g+1)*base),base) ] 
cols  = [ c for g in sample(range(base),base) for c in sample(range(g*base,(g+1)*base),base) ]            
board = [[board[r][c] for c in cols] for r in rows]

for line in board: print(line) #Prints solved board

#Begin Number Removal
squares = side*side
empties = squares * 3//4
for p in sample(range(squares),empties):
    board[p//side][p%side] = 0

numSize = len(str(side))
for line in board: print("["+"  ".join(f"{n or '.':{numSize}}" for n in line)+"]")
                                       #Print Solvable Puzzle
                                       
#Begin Graphics Additions
                                       
def expandLine(line):
    return line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:13]
line0  = expandLine("╔═══╤═══╦═══╗")
line1  = expandLine("║ . │ . ║ . ║")
line2  = expandLine("╟───┼───╫───╢")
line3  = expandLine("╠═══╪═══╬═══╣")
line4  = expandLine("╚═══╧═══╩═══╝")

symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums   = [ [""]+[symbol[n] for n in row] for row in board ]
print(line0)
for r in range(1,side+1):
    print( "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )
    print([line2,line3,line4][(r%side==0)+(r%base==0)])
