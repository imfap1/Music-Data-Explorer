
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt
import seaborn as sns
import os


def piechart(final_df, save=True, file_path=None, file_name=None):
    # Count the number of explicit and non-explicit songs
    explicit_count = len(final_df[final_df['Explicit'] == True])
    non_explicit_count = len(final_df[final_df['Explicit'] == False])

    # Create a list of counts and labels
    counts = [explicit_count, non_explicit_count]
    labels = ['Explicit', 'Non-Explicit']

    # Create the pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Explicit vs. Non-Explicit Songs')

    # Show the pie chart
    plt.show()

    # Save the chart as an image if save is set to True
    if save and file_path and file_name:
        plt.savefig(file_path + file_name, format='png')
def top_popularity_songs(final_df):
    popularity_songs = final_df.loc[final_df.groupby('Country')['Popularity'].idxmax()]
    return popularity_songs


def barplot(final_df, save=False, file_path=None, file_name=None):
    # Filter the DataFrame to keep only the top song for each country
    top_songs = final_df.loc[final_df.groupby('Country')['Popularity'].idxmax()]

    # Get unique countries
    unique_countries = top_songs['Country'].unique()

    # Create a bar plot with different colors for each country
    fig, ax = plt.subplots(figsize=(12, 6))

    for idx, country in enumerate(unique_countries):
        country_data = top_songs[top_songs['Country'] == country]
        ax.bar(country, country_data['Popularity'], label=country)

        # Display song titles as text labels above the bars
        for i, title in enumerate(country_data['Title']):
            ax.text(idx, country_data['Popularity'].iloc[i] + 2, title, ha='center', rotation=0)

    ax.set_xlabel("Country")
    ax.set_ylabel("Popularity")
    ax.set_title("Top Songs by Country with Highest Popularity")
    ax.legend(title="Country", loc="upper right")

    plt.tight_layout()
    plt.show()

    # Save the plot as an image if save is set to True
    if save and file_path and file_name:
        plt.savefig(file_path + file_name, format='png')

    plt.show()


def heatmap(final_df, save=True, file_path=None, file_name=None):
    numeric_columns = final_df.select_dtypes(include='number')  # Selecting only the numerical values
    correlation_matrix = numeric_columns.corr()  # Calculating correlation

    plt.figure(figsize=(10, 5))
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f')

    # Save the heatmap as an image if save is set to True
    if save and file_path and file_name:
        plt.savefig(file_path + file_name, format='png')

    plt.show()


def average_danceability(final_df, save=False, file_path=None, file_name=None):
    # Group data by country
    grouped_data = final_df.groupby('Country')

    # Calculate average danceability and energy for each country
    avg_danceability = grouped_data['Danceability'].mean()
    avg_energy = grouped_data['Energy'].mean()

    # Create a grouped bar chart
    width = 0.35  # Width of each bar

    fig, ax = plt.subplots(figsize=(10, 6))

    # Define x-axis locations for each bar
    x = range(len(avg_danceability))

    # Plot danceability bars
    ax.bar([i - width/2 for i in x], avg_danceability, width, label='Danceability', align='center')

    # Plot energy bars
    ax.bar([i + width/2 for i in x], avg_energy, width, label='Energy', align='center')

    ax.set_xlabel('Country')
    ax.set_ylabel('Score')
    ax.set_title('Average Danceability and Energy by Country')
    ax.set_xticks(x)
    ax.set_xticklabels(avg_danceability.index)
    ax.legend()

    # Save the grouped bar chart as an image if save is set to True
    if save and file_path and file_name:
        plt.savefig(file_path + file_name, format='png')

    plt.show()


def top_artist(final_df, save=False, file_path=None, file_name=None):
    # Group the data by the 'Artist' column and count the occurrences
    artist_counts = final_df['Artist'].value_counts()

    # Sort the artists by count in descending order
    sorted_artists = artist_counts.sort_values(ascending=False)

    # Limit the number of top artists to show in the plot (adjust as needed)
    top_n = 5
    top_artists = sorted_artists.head(top_n)

    # Create a bar chart
    plt.figure(figsize=(12, 6))
    top_artists.plot(kind='bar', color='skyblue')
    plt.title('Top Artists in the Playlist')
    plt.xlabel('Artist')
    plt.ylabel('Count')
    plt.xticks(rotation=45)

    # Save the bar chart as an image if save is set to True
    if save and file_path and file_name:
        plt.savefig(file_path + file_name, format='png')

    plt.show()


import matplotlib.pyplot as plt

def scatter_plot(final_df, save=False, file_path=None, file_name=None):
    # Calculate the overall correlation
    correlation_all = final_df["Tempo"].corr(final_df["Energy"])

    # Calculate the correlation by country
    correlations_by_country = final_df.groupby("Country")[["Tempo", "Energy"]].corr().iloc[0::2, -1]

    # Create scatter plots
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=final_df, x="Tempo", y="Energy")
    plt.title("Scatter Plot of Tempo vs. Energy")

    # Save the scatter plot as an image if save is set to True
    if save and file_path and file_name:
        plt.savefig(file_path + file_name, format='png')

    plt.show()

    # Print correlation results
    print("Overall Correlation: {:.2f}".format(correlation_all))
    print("Correlations by Country:")
    print(correlations_by_country)

def average_song(final_df, save=False, file_path=None, file_name=None):
    final_df["Duration (m)"] = final_df["Duration (s)"] / 60

    # Group data by "Country"
    grouped_data = final_df.groupby("Country")

    # Calculate the average duration for each country
    average_durations = grouped_data["Duration (m)"].mean()

    # Sort countries by average duration in ascending order
    average_durations = average_durations.sort_values(ascending=True)

    # Create a bar chart to visualize the results
    plt.figure(figsize=(10, 6))
    average_durations.plot(kind="bar", color="skyblue")
    plt.title("Average Song Duration by Country")
    plt.xlabel("Country")
    plt.ylabel("Average Duration (minutes)")
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

    # Save the bar chart as an image if save is set to True
    if save and file_path and file_name:
        plt.savefig(file_path + file_name, format='png')

    plt.show()

    return average_durations

def save_dataframe_to_csv(dataframe, folder_path, file_name):
    try:
        file_path = folder_path + file_name
        dataframe.to_csv(file_path, index=False)
        return True
    except Exception as e:
        print(f"Error saving DataFrame: {e}")
        return False




