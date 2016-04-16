def flatten(aList):
        temp =[]
        for i in aList:
                if  type(i)!=list:
                        temp.append(i)
                else:
                        temp += flatten(i)
            
        return temp





print flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
