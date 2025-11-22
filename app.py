import pickle
import streamlit as st
st.header('Movie Recommender System')
movies = pickle.load(open('model/movie_list.pkl','rb'))
similarity = pickle.load(open('model/similarity.pkl','rb'))
movie_list = movies['title'].values
selected_movie = st.selectbox(
"Type or select a movie from the dropdown",
movie_list
)