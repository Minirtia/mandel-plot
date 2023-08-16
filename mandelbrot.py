import cmath

#estimates how quickly the mandelbrot series for c diverges, if iter_max is reached, we say the series converges, so c is in the set
def mandelbrot(c, iter_max):
    z= complex(0, 0)    
    n = int(0)
    while(abs(z) <= 2 and n < iter_max):
        z = (z*z) + c
        n += 1

    return n
