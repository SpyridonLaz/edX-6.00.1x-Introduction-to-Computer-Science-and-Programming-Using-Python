
counter=0


def ndigits(x):
        global counter

        
        if x<10 and x>-10:
                counter+=1
                temp=counter;counter=0;return temp
        else:
                x=x/10
                counter+=1
                return ndigits(x)



print ndigits(3369)
