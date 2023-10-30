import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio
import sys
sys.path.append("./src")

import function as func # Import functions.py
import spotify_utils  as spoti # Import spotify_utils.py


final_df = spoti.get_spotify_data()

func.average_song(final_df, save=True, file_path='./images/', file_name='average_song_duration.png')
func.scatter_plot(final_df)
func.top_artist(final_df)
func.average_danceability(final_df)
func.heatmap(final_df)
func.barplot(final_df)
func.piechart(final_df)

plt.savefig('./images/average_song_duration.png')
plt.savefig('./images/scatter_plot.png')
plt.savefig('./images/top_artist.png')
plt.savefig('./images/average_danceability.png')
plt.savefig('./images/heatmap.png')
plt.savefig('./images/barplot.png')
plt.savefig('./images/piechart.png')

plt.show()