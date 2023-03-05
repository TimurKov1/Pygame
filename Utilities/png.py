import os
from PIL import Image

# for currentdir, dirs, files in os.walk('Attack3'):
#     for file in files:
#         print(f"{currentdir}/{file}")
#         if file == ".DS_Store":
#             continue
# name = int(file.split('-')[-1].split('.')[0]) + 1
img = Image.open(f"logo.jpg")
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if 200 <= item[0] <= 255 and 200 <= item[1] <= 255 and 200 <= item[2] <= 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)

img.save(f"logo.png", "PNG")