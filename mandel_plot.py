from mandelbrot import mandelbrot
import cmath
from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import font
import color_modules as cm

class MandelPlotter():
    def __init__(self, p_height, center, unit_scale, iter_max, aspect, bg_color):
        #calculate resolution based on fixed aspect ratio
        self.aspect = aspect
        self.p_width = int(p_height * aspect)
        self.p_height = p_height
        
        self.center = center
        self.unit_scale = unit_scale
        self.iter_max =iter_max

        self.bg_color = bg_color

        self._set_picture_settings()
        self._find_bounds()


    def _set_picture_settings(self):
        palette = []
        self._im = Image.new('RGB', (self.p_width, self.p_height), self.bg_color)
        self._draw = ImageDraw.Draw(self._im)

    def _get_color(self, comp):
        m = mandelbrot(comp, self.iter_max)
        if m < self.iter_max:
            red = self._get_red(comp, m)
            blue = self._get_blue(comp, m)
            green = self._get_green(comp, m)
            return (red, blue, green)
        return self.bg_color

    def _get_red(self, z, mandel):
        return cm.axisColor(z.real, self.re_start, self.re_end)

    def _get_blue(self, z, mandel):
        return cm.axisColor(z.imag, self.im_start, self.im_end)

    def _get_green(self, z, mandel):
        return cm.mandelColor(z, mandel, self.iter_max)

    def _find_bounds(self):
        self.im_start = - self.unit_scale + self.center.imag 
        self.im_end = self.unit_scale + self.center.imag
        self.re_start = -(self.aspect * self.unit_scale) + self.center.real
        self.re_end = (self.aspect * self.unit_scale) + self.center.real
  
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

DEFAULT_PLOTTER = MandelPlotter(600, -1/2 , 1, 30, 1.5, 0x000000)

def main():
    DEFAULT_PLOTTER.make_picture()
    DEFAULT_PLOTTER.save_image()
    print("[", DEFAULT_PLOTTER.re_start, ", ", DEFAULT_PLOTTER.re_end,  
          "]x[", DEFAULT_PLOTTER.im_start, ", ",  DEFAULT_PLOTTER.im_start, "]")

if __name__=="__main__":
    main()
   
