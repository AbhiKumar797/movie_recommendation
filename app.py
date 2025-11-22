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

