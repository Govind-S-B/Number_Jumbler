A = [[1,2,2,5],
     [6,3,8,1],
     [7,2,8,3],
     [1,5,9,3]]
B = [[4],
     [3],
     [3],
     [1]]
def matrix_converter(A):
    lst = []
    for m in A:
        for f in m:
            lst.append(f)
    return lst
plf_A = matrix_converter(A)                             #plf -> pure list form
plf_B = matrix_converter(B)
def multiplier(A,B,plf_A,plf_B):
    leng = len(A)
    pdt = []
    pdtlist = []
    rows = []
    pdtmatrix = []
    b = 0
    x = 0
    z = 0
    d = 0
    while x<(2*(int(len(plf_A)/len(B)))):
        for m in range(0,int(len(plf_A)/len(B))):
            for a in range(0,int(len(plf_A)/len(A))):
                #print(a)
                #print(x)
                p1 = plf_A[a+x]
                print(a+x)
                #print(p1)
                while b<(int(len(plf_B)/len(A)))**2:
                    #print(b)
                    p2 = plf_B[b+m]
                    #print(p2)
                    pdt.append(p1*p2)
                    #print(b+m)
                    b += int(len(plf_B)/len(B))
                    break
            b = 0
            pdt = sum(pdt)
            pdtlist.append(pdt)
            pdt = []
        x += int(len(plf_A)/leng)
    #print(pdtlist)
    while d <(int(len(plf_A)/len(B))**2):
        #print(d)
        rows = []
        while z < (int(len(pdtlist)/leng)):
            #print(d)
            rows.append(pdtlist[z+d])
            #print(z+d)
            z += 1
        z = 0
        d += int(len(plf_A)/len(B))
        #print(rows)
        pdtmatrix.append(rows)
    return(pdtmatrix)
print(multiplier(A,B,plf_A,plf_B))

