def f(x):
    import math
    x= 10*math.e**(math.log(0.5)/5.27 * x)
    return x

def radiationExposure(start, stop, step):

    start  =  float(start)
    stop  = float(stop)
    step  = float(step)
    
    summary=0
    while start<stop:

        summary+= step*f(start)
        start +=step
        
        
    return summary


x= radiationExposure(0, 5, 1)
