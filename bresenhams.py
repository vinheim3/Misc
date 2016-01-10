import sys
r = int(sys.argv[1])
word = sys.argv[2]
wptr = 0

xc, yc = r, r
xk, yk, pk = 0, r, 3-2*r

display = [[" " for i in range((r*2+1)*2)] for j in range(r*2+1)]
quadPoints = [[xk, yk]] #list of ordered octant points, relative to a center
plotPoints = set() #set of unique absolute points

#bresenham's circle algorithm for finding the right points in 1 octant
while xk < yk:
    xk += 1

    if pk < 0:
        quadPoints.append([xk, yk])
        pk += 4*xk + 6
    else:
        yk -= 1
        quadPoints.append([xk, yk])
        pk += 4*(xk-yk)+10

#leftI, rightI is 0 or 1 depending if x or y is used for that part
#leftMod, rightMod is 1 or -1 depending on if that part is negative relative to the center
def plotLetter(array, leftI, leftMod, rightI, rightMod):
    global xc, yc, wptr, word
    for i in array:
        newPoint = (i[leftI]*leftMod + xc, i[rightI]*rightMod + yc)
        if newPoint in plotPoints: continue #skip printing overlapped points
        plotPoints.add(newPoint)
        display[newPoint[1]][newPoint[0]*2] = word[wptr%len(word)]; wptr += 1
        display[newPoint[1]][newPoint[0]*2+1] = word[wptr%len(word)]; wptr += 1

#plots points clockwise starting from 12o'clock
#reflected octants are printed in reverse, to loop letters correctly
plotLetter(quadPoints,       0,  1, 1, -1)
plotLetter(quadPoints[::-1], 1,  1, 0, -1)
plotLetter(quadPoints,       1,  1, 0,  1)
plotLetter(quadPoints[::-1], 0,  1, 1,  1)
plotLetter(quadPoints,       0, -1, 1,  1)
plotLetter(quadPoints[::-1], 1, -1, 0,  1)
plotLetter(quadPoints,       1, -1, 0, -1)
plotLetter(quadPoints[::-1], 0, -1, 1, -1)

for i in display: print "".join(i)
