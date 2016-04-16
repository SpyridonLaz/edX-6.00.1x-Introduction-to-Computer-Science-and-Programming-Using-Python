def lenIter(aStr):
        '''
        aStr: a string
    
        returns: int, the length of aStr
        '''
        count = 0
        newStr = ""
        
        while aStr>newStr :
                newStr += aStr[count]
                count +=1
        return count
print lenIter("")
