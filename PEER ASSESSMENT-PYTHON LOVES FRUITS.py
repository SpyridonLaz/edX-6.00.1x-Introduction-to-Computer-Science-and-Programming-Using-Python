

def nfruits(basket,eatPattern):
        """
        basket ::  {dictionary}  This represents the fruit basket. Keys are the fruits , values are quantities of each fruit type.
        eatPattern :: This is the sequence that we choose to eat fruits.

        After each fruit eaten, we buy 1 fruit of each other fruit type there is.EXCEPT for the last fruit in sequence.
        
        Purpose of this function is to  determine the maximum quantity out of the different types of fruits that is
        present within Python's basket when he has reached the campus.
        
        """
        # Notice the below line.It removes the last fruit from basket preemptively to ensure we wont buy fruits after.
        basket[eatPattern[-1]]-=1

        # Iterates through sequence length , minus the last one to exclude the last fruit as above.
        for i in range(len(eatPattern)-1):
                basket[eatPattern[i]]-=1 

                # This loop iterates through all fruits and it gives +1 to each except for the one we just ate.
                for Key in basket:                        
                        if Key!=eatPattern[i]:
                                basket[Key]+=1
        #   Value of max( key:value) in basket is returned.
        return basket[max(basket, key=basket.get)]



print nfruits({'E': 8, 'K': 8, 'M': 7, 'Q': 10, 'S': 6, 'R': 9, 'T': 7}, 'Q')
