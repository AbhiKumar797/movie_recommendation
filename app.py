import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    max_retries = 3
    retry_delay = 1
    
    for attempt in range(max_retries):
        try:
            data = requests.get(url, timeout=5)
            data.raise_for_status()
            data = data.json()
            poster_path = data.get('poster_path')
            if poster_path:
                full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
                return full_path
        except Exception as e:
            if attempt < max_retries - 1:
                import time
                time.sleep(retry_delay)
                continue
            else:
                print(f"Could not fetch poster for movie_id {movie_id} after {max_retries} attempts: {e}")
    
    return "https://via.placeholder.com/500x750.png?text=No+Poster+Available"

def recommend(movie, num_recommendations=5):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    
    for i in distances[1:num_recommendations+1]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        movie_title = movies.iloc[i[0]].title
        
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movie_title)

    return recommended_movie_names, recommended_movie_posters

st.header('Movie Recommender System')
movies = pickle.load(open('model/movie_list.pkl','rb'))
similarity = pickle.load(open('model/similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Add slider for number of recommendations
num_recommendations = st.slider(
    "How many recommendations do you want?",
    min_value=5,
    max_value=20,
    value=10,
    step=5
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie, num_recommendations)
    
    st.subheader(f"Top {num_recommendations} Recommendations for '{selected_movie}'")
    
    # Display movies in rows of 5
    for row_start in range(0, len(recommended_movie_names), 5):
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            movie_idx = row_start + idx
            if movie_idx < len(recommended_movie_names):
                with col:
                    st.image(recommended_movie_posters[movie_idx])
                    st.text(recommended_movie_names[movie_idx])