def getSublists(L,n):

        newL=[]

        for i in range(len(L)-n+1):
                newL.append( L[i:i+n])

        return newL
        
