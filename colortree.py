from PIL import Image, ImageDraw
import math
import colorsys

spread = 17  # Amount branches spread apart
width, height = 1000, 800  # Window size
maxd = 12  # Maximum recursion depth
len_factor = 8.0  # Branch length factor

img = Image.new('RGB', (width, height))
d = ImageDraw.Draw(img)

def draw_tree(x, y, angle, depth):
    if depth > 0:
        x1 = x + int(math.cos(math.radians(angle)) * depth * len_factor)
        y1 = y + int(math.sin(math.radians(angle)) * depth * len_factor)

        (r, g, b) = colorsys.hsv_to_rgb(float(depth) / maxd, 1.0, 1.0)
        red, green, blue = int(255 * r), int(255 * b), int(255 * g)

        d.line([x, y, x1, y1], (red, green, blue), depth)

        draw_tree(x1, y1, angle - spread, depth-1)
        draw_tree(x1, y1, angle + spread, depth-1)

def main():
    draw_tree(width /2, height *0.9, -90, maxd)
    img.show()
    img.save("tree.png", "PNG")


if __name__ == '__main__':
    main()
