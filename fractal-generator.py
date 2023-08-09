import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    if n == max_iter:
        return max_iter
    return n + 1 - np.log(np.log2(abs(z)))

def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    pixels = np.zeros((width, height))

    for i in range(width):
        for j in range(height):
            pixels[i, j] = mandelbrot(x[i] + 1j*y[j], max_iter)

    return pixels

def plot_mandelbrot(pixels, cmap='inferno'):
    plt.imshow(pixels.T, cmap=cmap, extent=(-2.0, 1.0, -1.5, 1.5))
    plt.colorbar()
    plt.title("Mandelbrot Fractal")
    plt.show()

if __name__ == "__main__":
    width = 800
    height = 800
    x_min, x_max = -2.0, 1.0
    y_min, y_max = -1.5, 1.5
    max_iter = 1000

    mandelbrot_pixels = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)
    plot_mandelbrot(mandelbrot_pixels)
