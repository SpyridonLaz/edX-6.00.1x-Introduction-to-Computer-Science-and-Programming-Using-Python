def ndigits(x):
        
        """     x: is an integer,either positive or negative.
                How many digits x has?
                Lets study this function to find out!
                """
        
        if x==0:
                """ x :integer must be only positive/negative."""
                return 0
        
        if x<10 and x>-10:
                """ if True , it returns +1 digit (and recursion stops).      """
                
                return 1
                # Notice the  addition " 1+ " before recursive call.
                # That will help us count how many digits x initially has.
        else:
                """     If False , it starts/continues with recursion.    """
                x=x/10
                # Notice: everytime an integer is divided by 10 it loses one digit, until it equals zero.
                # remember: in python, dividing integer by integer gives the quotient only, not the decimal part.

                return 1+ndigits(x)

print ndigits(190)
