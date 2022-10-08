import numpy as np
import pandas as pd
from PIL import Image

img_fname = "obraz.jpg"
img = Image.open(img_fname)
img_array = np.array(img)
print(img_array.ndim, img_array.shape)
print(type(img_array.shape[0]))

colors = []
for i in range(img_array.shape[0]):
    for j in range(img_array.shape[1]):
        colors.append(tuple(img_array[i, j]))

print(colors[0])
counts = pd.Series(colors).value_counts()
print(counts.index[0])
for x, i in enumerate(counts[:10]):
    print(f"x: {counts.index[x]}, i: {i}")

