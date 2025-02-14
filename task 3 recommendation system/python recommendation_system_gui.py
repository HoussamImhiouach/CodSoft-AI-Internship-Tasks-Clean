import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import tkinter as tk
from tkinter import messagebox, scrolledtext
import zipfile
import os
import requests

# Download MovieLens dataset (if not already downloaded)
MOVIELENS_URL = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
MOVIELENS_ZIP = "ml-latest-small.zip"

if not os.path.exists("ml-latest-small"):
    print("Downloading dataset...")
    response = requests.get(MOVIELENS_URL)
    with open(MOVIELENS_ZIP, "wb") as file:
        file.write(response.content)
    with zipfile.ZipFile(MOVIELENS_ZIP, "r") as zip_ref:
        zip_ref.extractall(".")
    os.remove(MOVIELENS_ZIP)

# Load movie data
movies = pd.read_csv("ml-latest-small/movies.csv")
ratings = pd.read_csv("ml-latest-small/ratings.csv")

# Merge movies and ratings
df = pd.merge(ratings, movies, on="movieId")

# Compute average rating for each movie
movie_ratings = df.groupby("title")["rating"].mean().reset_index()
movie_ratings.columns = ["title", "average_rating"]

# Merge with movies dataset
df = pd.merge(movies, movie_ratings, on="title")

# Content-Based Filtering using TF-IDF on movie genres
vectorizer = TfidfVectorizer(stop_words="english")
genre_matrix = vectorizer.fit_transform(df["genres"])
cosine_sim = cosine_similarity(genre_matrix, genre_matrix)

# Mapping movie titles to indices
indices = pd.Series(df.index, index=df["title"]).drop_duplicates()

def recommend_movies(movie_title, num_recommendations=5):
    """Recommends movies based on genre similarity using MovieLens dataset."""
    
    # Convert input to lowercase for better matching
    movie_title = movie_title.lower()
    
    # Find closest match in dataset (ignoring case)
    matching_titles = [title for title in df["title"] if movie_title in title.lower()]
    
    if not matching_titles:
        return ["Movie not found. Try another title."]
    
    # Use the first matched title
    selected_movie = matching_titles[0]
    
    idx = indices[selected_movie]
    similarity_scores = list(enumerate(cosine_sim[idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    recommended_indices = [i[0] for i in similarity_scores[1:num_recommendations+1]]
    
    return df["title"].iloc[recommended_indices].tolist()


# GUI Application
def get_recommendations():
    """Fetches recommendations based on user input."""
    user_movie = entry.get()
    recommendations = recommend_movies(user_movie)
    
    text_area.config(state="normal")
    text_area.delete("1.0", tk.END)
    
    if "Movie not found" in recommendations:
        text_area.insert(tk.END, recommendations[0] + "\n")
    else:
        text_area.insert(tk.END, "Recommended Movies:\n")
        for movie in recommendations:
            text_area.insert(tk.END, f"- {movie}\n")

    text_area.config(state="disabled")

# Tkinter GUI Setup
root = tk.Tk()
root.title("Movie Recommendation System")
root.geometry("500x400")

tk.Label(root, text="Enter a movie title:", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, font=("Arial", 12), width=40)
entry.pack(pady=5)

search_button = tk.Button(root, text="Get Recommendations", font=("Arial", 12), command=get_recommendations)
search_button.pack(pady=10)

text_area = scrolledtext.ScrolledText(root, width=50, height=10, font=("Arial", 12), state="disabled")
text_area.pack(pady=10)

root.mainloop()
