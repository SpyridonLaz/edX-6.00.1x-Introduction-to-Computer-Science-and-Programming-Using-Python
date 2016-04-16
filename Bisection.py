def multi ( ):
        high = 100
        low = 0
        midpoint = (high + low) / 2

        while high-low >2:

                print midpoint 
                x = raw_input("h   or   l   :     ")
                if x== "l":
                        high = midpoint
                elif x=="h":
                        low = midpoint


                else:
                        print "Wrong Input"

                midpoint = (high + low) / 2

                        
        print "Number is ",midpoint

 

def restart():

        x ="y"
        while x=="y":
                multi()
                x=raw_input("Play again?  y/n      :    ")
                print
                print
                print
                print
                






print restart ()
