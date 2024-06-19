import streamlit as st
import pickle
import pandas as pd

st.title("Movie Recommender System")


def fetchIndex(string):
    return movies[movies['title'] == string].index[0]


def recommend(movie):
    movie_index = fetchIndex(movie)
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_list = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movies = pd.DataFrame(movies_list)
recommended_movies=[]

selected_movie_name = st.selectbox(
    "Please select a movie",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        movie_id:i[0]
        st.write(i)