import os
from PIL import Image

# for currentdir, dirs, files in os.walk('Attack3'):
#     for file in files:
#         print(f"{currentdir}/{file}")
#         if file == ".DS_Store":
#             continue
#         name = int(file.split('-')[-1].split('.')[0]) + 1
img = Image.open(f"1.png")
x, y = img.size
img = img.resize((x // 3, 158))

img.save(f"1.png", "PNG")