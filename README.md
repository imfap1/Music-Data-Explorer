# Project-II: Music Data Explorer

## Introduction

Welcome to the "Music Data Explorer" project, a tool that lets you extract, analyze, and visualize Spotify data. This project provides a deep dive into your music playlists, offering insights into song and artist characteristics and creating captivating visualizations. Whether you're a music enthusiast, aspiring data analyst, or simply curious about your musical tastes, this project is your gateway to unlocking the secrets hidden within your music collection.


## Data and Methodology

### Data Source

- The project utilizes Spotify's extensive data for song and artist details.
- Specifically, data was collected from the top playlists of 5 European countries, providing a diverse and representative sample of music preferences.

### Methodology

- Data retrieval from the Spotify API.
- Data analysis and visualization using Python and relevant libraries.

## Key Features

The "Music Data Explorer" project offers a range of powerful features for exploring and understanding your Spotify playlist data. These key features are organized into separate categories:


### Song Characteristics Analysis
- **Average Song Duration:** Visualize and analyze the average duration of songs in your playlist, helping you understand the composition of your music collection.

- **Scatter Plot:** Discover correlations between song tempo and energy, providing insights into the dynamics of your favorite tunes.

- **Top Artists:** Identify and visualize the most prominent artists in your playlist, allowing you to recognize your musical preferences.

### Regional Insights
- **Average Danceability:** Gain insights into the danceability and energy of songs by country, providing a unique perspective on regional music preferences.

- **Heatmap:** Visualize the correlation between numerical attributes in the dataset, uncovering patterns and relationships in your music data.

- **Bar Plot:** Create country-specific bar plots to identify the top songs by popularity in different regions, revealing local favorites.

### Content Analysis
- **Pie Chart:** Explore the distribution of explicit and non-explicit songs in your playlist, offering insights into the content of your music collection.

## Requirements/Libraries Used

This project harnesses the power of various Python libraries to accomplish its feats. Here's an updated list of the primary dependencies:

- **pandas:** The backbone of data manipulation and analysis, providing DataFrames and Series, extensively used in the project.

- **spotipy:** A Python library that seamlessly connects to Spotify's Web API for retrieving track information and artist details.

- **SpotifyClientCredentials:** A module from Spotipy, facilitating the setup of Spotify API credentials for authentication and data retrieval.

- **matplotlib.pyplot:** Essential for crafting diverse plots and charts, such as bar plots and scatter plots. It's a leading data visualization library in the Python ecosystem.

- **seaborn:** This data visualization library not only enhances the aesthetics of Matplotlib's plots but also simplifies common data visualization tasks and boosts visual appeal.

- **plotly.express:** A high-level data visualization library that simplifies the creation of interactive plots like pie charts and bar plots, with minimal code. It's perfect for creating visually appealing and interactive visualizations.

With these libraries at your disposal, you're well-equipped to explore, analyze, and visualize your music data.

## Hypotheses

1. **Explicit Songs Proportion:** Investigating the proportion of explicit songs in the playlist compared to non-explicit songs.

2. **Top Song Popularity by Country:** Exploring the popularity variations of the top songs in different countries.

3. **Danceability and Energy Variation by Country:** Analyzing the variation in average danceability and energy scores of songs from different countries.

4. **Dominant Artists in the Playlist:** Uncovering the presence of dominant artists within the playlist who significantly contribute to its content.

## Analysis

### Hypothesis 1: Explicit Songs Proportion

- **Null Hypothesis (H0):** The percentage of explicit songs in the playlist is equal to the percentage of non-explicit songs.
- **Alternative Hypothesis (H1):** The percentage of explicit songs in the playlist is different from the percentage of non-explicit songs.

![PieChart](https://github.com/imfap1/Project-II/blob/main/images/piechart.png?raw=true)

This hypothesis delves into the presence of explicit songs within the playlist, evaluating their impact on the overall composition.

### Hypothesis 2: Top Song Popularity by Country

- **Null Hypothesis (H0):** There is no significant difference in the popularity of the top songs among different countries.
- **Alternative Hypothesis (H1):** The popularity of the top songs varies significantly across different countries.

![Top Songs](https://github.com/imfap1/Project-II/blob/main/images/barplot.png)

This hypothesis aims to uncover any significant differences in the popularity of top songs among various countries, potentially influenced by cultural or regional factors.

### Hypothesis 3: Danceability and Energy Variation by Country

- **Null Hypothesis (H0):** The average danceability and energy scores of songs from different countries are not significantly different.
- **Alternative Hypothesis (H1):** There is a significant variation in the average danceability and energy scores of songs from different countries.

![Danceability](https://github.com/imfap1/Project-II/blob/main/images/average_danceability.png)

This hypothesis explores the variation in danceability and energy scores based on the songs' countries of origin, potentially revealing cultural or regional musical influences.

### Hypothesis 4: Dominant Artists in the Playlist

- **Null Hypothesis (H0):** The distribution of artists in the playlist is uniform, with no specific artist dominating.
- **Alternative Hypothesis (H1):** There are a few dominant artists who significantly contribute to the playlist, while most artists have minimal representation.

![Dominant Artists](https://github.com/imfap1/Project-II/blob/main/images/top_artists.png)
 
This hypothesis seeks to identify any dominant artists within the playlist, potentially indicating listener preferences or specific musical genres' popularity.

## Conclusion

In the "Music Data Explorer" project, we've embarked on a journey of discovery within the realm of Spotify data. By employing data analysis and visualization techniques, we've uncovered patterns and insights about the songs, artists, and countries represented in our playlists.

Here are the key findings:

- **Explicit Songs Proportion:** The playlist boasts a significant proportion of non-explicit songs, catering to a diverse audience.

- **Top Songs by Country:** Our analysis reveals varying preferences in song popularity among different countries, shedding light on unique cultural influences.

- **Danceability and Energy Variation:** We've detected subtle differences in the danceability and energy of songs from various countries, reflecting cultural or regional music styles.

- **Dominant Artists:** Our analysis uncovers the presence of dominant artists, providing valuable insights into listener preferences and musical diversity.

This project showcases the power of data analysis and visualization in unveiling hidden trends and nuances within Spotify playlists. These findings can prove invaluable to playlist curators, music enthusiasts, and anyone intrigued by the intricate world of music preferences across the globe.
