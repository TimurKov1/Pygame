import os

for currentdir, dirs, files in os.walk('Sprites/Characters/Leaf'):
    for file in files:
        os.rename(f"{currentdir}/{file}", f"{currentdir}/{file.split('.')[0].split('_')[-1]}.png")