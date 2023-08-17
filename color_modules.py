import cmath
from mandelbrot import mandelbrot


#returns a color inversely proportional to divergence speed of the mandelbrot series of z
def mandelColor(z, mandel, iter_max):
    color = 255 - int(255 * mandel / iter_max)
    return color

#returns a color that decays further from the center of a single axis
def axisColor(x, start, end):
    cen = (end + start) / 2
    max_dist = end - start
    dist = abs(x - cen)
    return int((-255 / max_dist * dist) + 255)
    

