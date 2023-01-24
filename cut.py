from PIL import Image
import os

for currentdir, dirs, files in os.walk('Warrior'):
    for file in files:
        name = file.split('.')[0]
        os.mkdir(f"Warrior/{name}")
    
        im = Image.open(f"Warrior/{name}.png")
        pixels = im.load()
        x, y = im.size
        coords = {
            'left': x,
            'right': 0,
            'top': y,
            'bottom': 0
        }
        count = 1
        loop_prev = []
        loop = 0

        for i in range(x - 1):
            loop_current = []
            for j in range(y - 1):
                if pixels[i, j] == (0, 0, 0, 0):
                    loop_current.append(True)
                else:
                    loop_current.append(False)
                if pixels[i, j] != pixels[i + 1, j] and i < coords['left']:
                    coords['left'] = i + 1
                if pixels[i, j] != pixels[i - 1, j] and i > coords['right']:
                    coords['right'] = i
                if pixels[i, j] != pixels[i, j + 1] and j < coords['top']:
                    coords['top'] = j + 1
                if pixels[i, j] != pixels[i, j - 1] and j > coords['bottom']:
                    coords['bottom'] = j

            if len(loop_prev) > 0:
                if (not all(loop_prev)) and all(loop_current):
                    width = coords['right'] - coords['left']
                    height = coords['bottom'] - coords['top']
                    new_image = im.crop((coords['left'], 0, coords['right'], coords['bottom']))
                    new_image.save(f"Warrior/{name}/{count}.png", "PNG")
                    count += 1
                    coords = {
                        'left': x,
                        'right': 0,
                        'top': y,
                        'bottom': 0
                    }
                    loop = 0

            if all(loop_current):
                loop += 1

            loop_prev = loop_current.copy()