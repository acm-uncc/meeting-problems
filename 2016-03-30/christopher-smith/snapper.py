import math
def solve(n, k):
    #snaps = n
    #clicks = k
    #clickneed=(2**snaps)
    #print (2^1)
    #print (snaps,"snaps")
    #print (clickneed,"Clicks needed")
    #print (clicks, "clicks")

    return ((k+1)%(pow(2,n))==0)

input = open("input.txt","r+")

cases = int(input.readline())
solved = open("solution.txt",'w')
casenum = 1
for x in range(0,cases):

    test = input.readline().split()
    n = int(test[0])
    k=int(test[1])
    #print(n,k)
    if solve(n,k):
        solved.write("Case #" +str(casenum)+": ON\n")
    else:
        solved.write("Case #" +str(casenum)+": OFF\n")
    casenum = casenum+1

solved.close()
input.close()