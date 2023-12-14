import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

characters = ['Nami', 'Zoro', 'Luffy']
popularity_data = {
    '2010': [60, 75, 80],
    '2011': [65, 80, 85],
    '2012': [70, 85, 90],
    '2013': [72, 88, 92],
    '2014': [75, 90, 95],
    '2015': [78, 92, 98],
    '2016': [76, 91, 97],
    '2017': [74, 89, 94],
    '2018': [73, 88, 93],
    '2019': [77, 93, 99],
    '2020': [89, 95, 102],
}

fig, ax = plt.subplots()
bar_width = 0.2
bar_colors = ['#1E90FF', '#008000', '#FF0000']
bar_positions = np.arange(len(characters))


def update(frame):
    ax.clear()
    year = str(2010 + frame)
    plt.title(f'One Piece Characters Popularity in {year}')
    plt.xlabel('Popularity')
    plt.ylabel('Characters')

    for i, character in enumerate(characters):
        popularity = popularity_data[year][i]
        ax.barh(character, popularity, color=bar_colors[i])

animation = FuncAnimation(fig, update, frames=len(popularity_data), interval=1000, repeat=False)

plt.show()

