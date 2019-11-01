# Simple interface for coloring
# I was to lazy to implement hsv2rgb myself but I plan to change it sometime
from colorsys import hsv_to_rgb


def hsv2rgb(h,s,v):
    r,g,b = hsv_to_rgb(h, s, v)
    return (int(255*r),int(255*g),int(255*b))


def rainbow(hue):
    return hsv2rgb(hue, 1.0, 1.0)


def main():
    from PIL import Image, ImageDraw

    img = Image.new('RGB', (800, 200))
    pencil = ImageDraw.Draw(img)

    for i in range(800):
        hue = i/800
        r,g,b = hsv_to_rgb(hue, 1.0, 1.0)
        R,G,B = int(255*r),int(255*g),int(255*b) 
        pencil.line((i,0,i,200), fill = (R,G,B), width=2)
        
    img.show()


if __name__=='__main__':
    main()
