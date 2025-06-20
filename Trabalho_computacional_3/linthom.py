def linthom(a,b,c,d):
    
    N = len(b) # number of equations

    # Test for diagonal dominance
    is_diagonally_dominant = True
    if (abs(float(b[0]))<abs(float(c[0]))):
        is_diagonally_dominant = False
    for k in range(1,N-1):
        if (abs(float(b[k]))<abs(float(c[k]))+abs(float(a[k-1]))):
            is_diagonally_dominant = False
    if (abs(float(b[N-1]))<abs(float(a[N-2]))):
            is_diagonally_dominant = False        
        
    # Replicating variables
    ab, ad, aa, b = map(list, (a, b, c, d)) 
    # Algorithm 
    for i in range(1, N):
        m = float(ab[i-1])/float(ad[i-1])
        ad[i] = float(ad[i]) - m*float(aa[i-1])
        b[i] = float(b[i]) - m*float(b[i-1])
    
    # Solving    	    
    x = ad
    x[-1] = b[-1]/ad[-1]
    for j in range(N-2, -1, -1):
        x[j] = (b[j]-aa[j]*x[j+1])/ad[j]
    
    return x, is_diagonally_dominant