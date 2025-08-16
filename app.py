import streamlit as st
import pickle
import pandas as pd

# Load the data outside the function so it's available globally
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_list = movies['title'].values


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    sorted_dist = distance.argsort()[::-1]
    top_5_indices = sorted_dist[1:6]

    recommended_movies = []
    for i in top_5_indices:
        recommended_movies.append(movies.iloc[i].title)
    return recommended_movies


# Streamlit UI
st.title('MOVIES RECOMMENDER SYSTEM')

selected_movie_name = st.selectbox(
    'Select a movie from the given list and click on Recommend.',
    movies_list
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for movie in recommendations:
        st.write(movie)
