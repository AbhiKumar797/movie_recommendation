import pickle
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)  


movies = pickle.load(open('../model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('../model/similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
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
                time.sleep(retry_delay)
                continue
            else:
                print(f"Could not fetch poster for movie_id {movie_id}: {e}")
    
    return "placeholder.svg"

def recommend(movie, num_recommendations=5):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        
        recommended_movies = []
        
        for i in distances[1:num_recommendations+1]:
            movie_id = movies.iloc[i[0]].movie_id
            movie_title = movies.iloc[i[0]].title
            
            recommended_movies.append({
                'id': int(movie_id),
                'title': movie_title,
                'poster': fetch_poster(movie_id),
                'similarity_score': float(i[1])
            })
        
        return recommended_movies
    except Exception as e:
        print(f"Error in recommend: {e}")
        return []

@app.route('/api/movies', methods=['GET'])
def get_movies():
    """Get all movie titles"""
    movie_list = movies['title'].values.tolist()
    return jsonify({'movies': movie_list})

@app.route('/api/recommend', methods=['POST'])
def get_recommendations():
    """Get movie recommendations"""
    data = request.json
    movie_name = data.get('movie')
    num_recommendations = data.get('count', 10)
    
    if not movie_name:
        return jsonify({'error': 'Movie name is required'}), 400
    
    recommendations = recommend(movie_name, num_recommendations)
    
    if not recommendations:
        return jsonify({'error': 'Movie not found or no recommendations available'}), 404
    
    return jsonify({
        'selected_movie': movie_name,
        'count': num_recommendations,
        'recommendations': recommendations
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'Movie Recommender API is running'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
