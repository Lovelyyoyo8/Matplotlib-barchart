from data_define import Record
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


file_path = r'F:\Downloads\One Piece Popularity 2018-10 to 2019-12.xlsx'

class FileReader:
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        df = pd.read_excel(self.path, index_col=0)  # Assuming dates are in the first column
        characters = df.columns.tolist()
        popularity_data = {str(year): df[year].tolist() for year in df.columns}

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


def update(frame):
    ax.clear()
    year = str(2018-10 + frame)
    plt.title(f'One Piece Characters Popularity in {year}')
    plt.xlabel('Characters')
    plt.ylabel('Popularity')

    for i, character in enumerate(characters):
        popularity = popularity_data[year][i]
        ax.bar(character, popularity, color=bar_colors[i], width=bar_width, align='center')


animation = FuncAnimation(fig, update, frames=len(popularity_data), interval=1000, repeat=False)

plt.show()
