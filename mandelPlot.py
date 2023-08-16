from mandelbrot import mandelbrot
import cmath
from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import font

#returns a color inversely proportional to divergence speed of the mandelbrot series of z
def mandelColor(z, iter_max):
    m = mandelbrot(z, iter_max)
    color = 255 - int(255 * m / iter_max)
    return color


class MandelPlotter():
    def __init__(self, p_height, center, unit_scale, iter_max, aspect):
        #calculate resolution based on fixed aspect ratio
        self.aspect = aspect
        self.p_width = int(p_height * aspect)
        self.p_height = p_height
        
        self.center = center
        self.unit_scale = unit_scale
        self.iter_max =iter_max

        self.bg_color = (0, 0, 0) #TODO implement hex color picker

        self._set_picture_settings()
        self._find_bounds()


    def _set_picture_settings(self):
        palette = []
        self._im = Image.new('RGB', (self.p_width, self.p_height), self.bg_color)
        self._draw = ImageDraw.Draw(self._im)


    #given a complex z, finds the corresponding RGB triple
    def _get_color(self, z):
        red = self._get_red(z)
        blue = self._get_blue(z)
        green = self._get_green(z)
        return (red, blue, green)

    def _get_red(self, z):
        return mandelColor(z, self.iter_max)

    def _get_blue(self, z):
        return mandelColor(z, self.iter_max)

    def _get_green(self, z):
        return mandelColor(z, self.iter_max)


    #sets bounds such that the imaginary axis is (-unit_scale + Im(center), unit_scale + Im(center)
    def _find_bounds(self):
        self.im_start = - self.unit_scale + self.center.imag
        self.im_end = self.unit_scale + self.center.imag
        self.re_start = -(self.aspect * self.unit_scale) + self.center.imag
        self.re_end = (self.aspect * self.unit_scale) + self.center.imag
  
    #converts pixels to complex numbers
    def _pixel_to_complex(self, x, y):
        z = complex(self.re_start + (x / self.p_width) * (self.re_end - self.re_start),
                    self.im_start + (y / self.p_height) * (self.im_end - self.im_start))
        return z

    def make_picture(self):
        #draws each pixel based on its complex counterpart
        for x in range(0, self.p_width):
            for y in range(0, self.p_height):
                current_complex = self._pixel_to_complex(x, y)
                color = self._get_color(current_complex)
                self._draw.point([x, y], color)

    def save_image(self):
        self._im.save('output.png', 'PNG')

DEFAULT_PLOTTER = MandelPlotter(600, 0, 1, 30, 1.5)

def main():
    DEFAULT_PLOTTER.make_picture()
    DEFAULT_PLOTTER.save_image()

if __name__=="__main__":
    main()
   
