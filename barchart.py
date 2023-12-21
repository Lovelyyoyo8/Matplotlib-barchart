from data_define import Record
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import urllib.request

file_path = r'F:\Downloads\One Piece Popularity 2019.xlsx'

class FileReader:
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        df = pd.read_excel(self.path, index_col=0)
        characters = df.columns.tolist()
        popularity_data = {str(month): df[month].tolist() for month in range(2, 13)}

        return characters, popularity_data

file_reader = FileReader(file_path)
characters, popularity_data = file_reader.read_data()

fig, ax = plt.subplots()
bar_width = 0.2
bar_colors = {
    'Monkey D. Luffy': '#FF0000',
    'Roronoa Zoro': '#008000',
    'Nami': '#1E90FF',
    'Charlotte Katakuri': '#8B0000',
    'Boa Hancock': '#9370D8',
    'Kaido': '#0000CD',
    'Nico Robin': '#FF69B4',
    'Sanji': '#FFD700'
}
bar_positions = np.arange(len(characters))

luffy_icon_url = 'https://i.pinimg.com/736x/b3/8c/b4/b38cb443bff8ba204fd6c2c075135d3e.jpg'
urllib.request.urlretrieve(luffy_icon_url, 'luffy_icon.jpg')
nami_icon_url = 'https://i.pinimg.com/736x/30/b5/f6/30b5f66efe7cc5311c757fd7074307b6.jpg'
urllib.request.urlretrieve(nami_icon_url, 'nami_icon.jpg')
zoro_icon_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9P_G7E4pvDVbLpFPdpK-Fe1jRXKOjlj5h4g&usqp=CAU'
urllib.request.urlretrieve(zoro_icon_url, 'zoro_icon.jpg')
robin_icon_url = 'https://i.pinimg.com/736x/30/88/6a/30886acd22fe6ddd35fc2efadba0a8d8.jpg'
urllib.request.urlretrieve(robin_icon_url, 'robin_icon.jpg')
katakuri_icon_url = 'https://i.pinimg.com/originals/5b/c6/9c/5bc69cae9513d474532ed7f27db6554b.jpg'
urllib.request.urlretrieve(katakuri_icon_url, 'katakuri_icon.jpg')
boa_icon_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFVHkPrJQ1vGEfQx0iHa6uCAag6_CMOElDTQ&usqp=CAU'
urllib.request.urlretrieve(boa_icon_url, 'boa_icon.jpg')

def update(frame):
    ax.clear()
    month = str(frame + 1)
    plt.title(f'One Piece Characters Popularity in {month}')
    plt.xlabel('Characters')
    plt.ylabel('Popularity')

    for i, character in enumerate(characters):
        popularity = popularity_data[month][i]
        bar = ax.bar(character, popularity, color=bar_colors[character], width=bar_width, align='center')

        # Add icons to the end of each bar
        icon_path = f'luffy_icon.jpg' if character == 'Monkey D. Luffy' else f'path/to/icon/{character.lower()}_icon.png'
        imagebox = OffsetImage(plt.imread(icon_path), zoom=0.1, resample=True, clip_path=bar)
        ab = AnnotationBbox(imagebox, (bar[i].get_x() + bar[i].get_width(), bar[i].get_height()), frameon=False)
        ax.add_artist(ab)

animation = FuncAnimation(fig, update, frames=len(popularity_data), interval=1000, repeat=False)

plt.show()
