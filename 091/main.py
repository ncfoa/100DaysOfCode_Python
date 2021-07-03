import matplotlib.image as img
import matplotlib.pyplot as plt
from scipy.cluster.vq import whiten
from scipy.cluster.vq import kmeans
import pandas as pd

image = img.imread('./IMG_3403.JPG')

r = []
g = []
b = []
for row in image:
    for temp_r, temp_g, temp_b in row:
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)

print(len(r))
print(len(g))
print(len(b))

image_df = pd.DataFrame({'red': r, 'green': g, 'blue': b})

image_df['scaled_color_red'] = whiten(image_df['red'])
image_df['scaled_color_blue'] = whiten(image_df['blue'])
image_df['scaled_color_green'] = whiten(image_df['green'])
print("1")
cluster_centers, _ = kmeans(image_df[['scaled_color_red', 'scaled_color_blue', 'scaled_color_green']], 3)
print("2")
dominant_colors = []

red_std, green_std, blue_std = image_df[['red', 'green', 'blue']].std()
print("3")
for cluster_center in cluster_centers:
    red_scaled, green_scaled, blue_scaled = cluster_center
    dominant_colors.append((
        red_scaled * red_std / 255,
        green_scaled * green_std / 255,
        blue_scaled * blue_std / 255
    ))
print("4")
plt.imshow([dominant_colors])
plt.show()
