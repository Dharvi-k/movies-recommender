
🎬 Movie Recommender System

A simple yet powerful Movie Recommendation System built with Python, Streamlit, and Machine Learning. The app recommends movies similar to the one selected by the user, based on content-based filtering (cosine similarity on movie metadata).

🚀 Live Demo: [Click here to try the app](https://dharvi-k-movies-recommender-movies-qyztqx.streamlit.app/)

📖 Project Notebook: [Colab Notebook](https://colab.research.google.com/drive/1iBHdqKeywQ-wBRHJnXyKgRU0pIfuX9Wt)

---
🔍 Features

Search for any movie and get top recommendations.

Uses content-based filtering with cosine similarity.

Simple and interactive Streamlit UI.

Deployed live on Streamlit Cloud.

---
⚙️ Tech Stack

Python

Pandas, NumPy (data processing)

scikit-learn (vectorization & similarity)

Streamlit (web app)

---
🛠 How It Works

Extracts important metadata (title, genres, keywords, etc.) for each movie.

Converts text data into numerical vectors using CountVectorizer.

Computes cosine similarity between movies.

Given a movie, recommends the most similar ones.
