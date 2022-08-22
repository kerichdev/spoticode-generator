from PIL import Image, ImageDraw
import sys, hashlib

song_hash = hashlib.sha256(sys.argv[1].encode()).digest();

im = Image.new("RGBA", (3200, 500), (0, 0, 0, 0))
dr = ImageDraw.Draw(im)

def circle(draw, center, radius, fill):
    dr.ellipse((center[0] - radius + 1, center[1] - radius + 1, center[0] + radius - 1, center[1] + radius - 1), fill=fill, outline=None)

W = 50
COLOR = (255, 255, 255)

coords = [50, 0, 50, 0]

def coderound(x, base=25):
    return base * round(x/base)

for i, byte in enumerate(song_hash):
    percent = 0.7
    coords[1] = coderound(round(196/percent + byte*percent))
    coords[3] = 500 - coords[1]
    dr.line(coords, width=W, fill=COLOR)
    circle(dr, (coords[0], coords[1]), W / 2, COLOR)
    circle(dr, (coords[2], coords[3]), W / 2, COLOR)
    coords[0] = coords[0] + 100
    coords[2] = coords[2] + 100
  
im.save(sys.argv[1] + ".png")
im.close()
