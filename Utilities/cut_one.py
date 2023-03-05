from PIL import Image
import os

path = 'Attack3'

for currentdir, dirs, files in os.walk(path):
    for file in files:
        print(f"{currentdir}/{file}")
        if file == '.DS_Store':
            continue
        im = Image.open(f"{currentdir}/{file}")
        pixels = im.load()
        x, y = im.size
        coords = {
            'left': x,
            'right': 0,
            'top': y,
            'bottom': 0
        }

        for i in range(x - 1):
            for j in range(y - 1):
                if pixels[i, j] != pixels[i + 1, j] and i < coords['left']:
                    coords['left'] = i + 1
                if pixels[i, j] != pixels[i - 1, j] and i > coords['right']:
                    coords['right'] = i
                if pixels[i, j] != pixels[i, j + 1] and j < coords['top']:
                    coords['top'] = j + 1
                if pixels[i, j] != pixels[i, j - 1] and j > coords['bottom']:
                    coords['bottom'] = j
        height = coords['bottom'] - coords['top']
        im = im.crop((coords['left'], 0, coords['right'], 477))
        im.save(f"{currentdir}/{file}")