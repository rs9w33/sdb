import rasterio as rio
import matplotlib.pyplot as plt
import os
import pandas as pd

fpath = r'D:\bathydem\wwf-turtles-guianas\data\sdb-intertidal'

files = [i for i in os.listdir(fpath) if ('mndwi' in i) and (i.endswith('tiff'))]

src_files = [rio.open(os.path.join(fpath,f)) for f in files]
raster_data = [src.read(1) for src in src_files]

fig, ax = plt.subplots()
plt.axis('off')
im = ax.imshow(raster_data[0], cmap='coolwarm_r', vmin=-0.1, vmax=0.15)

ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

cbar = fig.colorbar(im, ax=ax)
cbar.set_label('Water Index [mndwi]')
def update(frame):
    im.set_array(raster_data[frame])
    date = '-'.join(files[frame].split('-')[3:6])
    ax.set_title(f'{date}')
    return im,

import matplotlib.animation as animation

anim = animation.FuncAnimation(fig, update, frames=len(files), interval = 500)

anim.save(r'D:\bathydem\wwf-turtles-guianas\data\braamspunt_2016-2023.gif', writer='pillow')