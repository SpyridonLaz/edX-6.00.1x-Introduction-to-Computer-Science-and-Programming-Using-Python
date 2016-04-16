import math
# Import math so we can implement  methods and constants.


def polysum(n , s ):
        '''
        This function calculates and sums the following :
                1. area  - area of polygon
                2.perimeter - perimeter of polygon
        ,then we return the sum rounded by 4 decimals.
                
        n  ::  number of sides
        s  ::   length of a side                             '''
        
        area = 0.25*n*s**2/ (math.tan(math.pi/n))
        #  tan,  pi  are  method() and constant respectively.
        #To implement them, do not forget to 'import math' at the top.
        
        perimeter =  (n*s)**2
        return round (area+perimeter,4)


