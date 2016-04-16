def f(a,b):
        return a+b

def dict_interdiff(c1,c2  ):
        d1={}
        d2={}

        for i in c1:
                if i in c2:
                        
                        d1[i] =  f(c1.get(i) , c2.get(i))
                else:
                        d2[i] =   c1.get(i,0) + c2.get(i,0)
        for j in c2:
                if j not  in c1:
                        
                        d2[j] =   c1.get(j,0) + c2.get(j,0)
                        

        return (d1 ,d2      )



c1 = {1:30,     2:20,      3:40 ,     }
c2 = {    1:40,        5:50,       3:60,     8:40,   666:60}
# 1  , 3
#0, 2 , 5,8,666,"evil"



print dict_interdiff ( c1,c2   )

