import streamlit as st
import pandas as pd
import pickle
import requests
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# To Fetch Poster of Recommended movies

@st.cache_data #recommended by AI
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Recommendation Function

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key = lambda x : x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch Poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies

# end of recommend function

# Recommendations to deploy on streamlit cloud
similarity = joblib.load(
    os.path.join(BASE_DIR, "similarity_movies.pkl")
)

movies_dict = pickle.load(
    open(os.path.join(BASE_DIR, "movie_dictionary.pkl"), "rb")
)
movies = pd.DataFrame(movies_dict)

st.title("Movie Recommendation Engine")

selected_movie_name = st.selectbox(
    'Which Movie do you Like ?',
    movies['title'].values
)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
