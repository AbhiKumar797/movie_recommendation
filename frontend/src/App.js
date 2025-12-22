import React, { useState, useEffect, useCallback } from 'react';
import axios from 'axios';
import './App.css';
import MovieCard from './components/MovieCard';
import Header from './components/Header';
import Spinner from './components/Spinner'; // Import Spinner

const API_URL = 'https://movie-recommendation-api-sldt.onrender.com';

function App() {
  const [movies, setMovies] = useState([]);
  const [selectedMovie, setSelectedMovie] = useState('');
  const [numRecommendations, setNumRecommendations] = useState(10);
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    axios.get(`${API_URL}/api/movies`)
      .then(response => {
        setMovies(response.data.movies);
      })
      .catch(err => {
        console.error('Error fetching movies:', err);
        setError('Failed to load movie list');
      });
  }, []);

  const handleRecommend = useCallback(async (movie) => {
    const movieToRecommend = movie || selectedMovie;
    if (!movieToRecommend) {
      setError('Please select a movie');
      return;
    }

    setLoading(true);
    setError('');
    setRecommendations([]);
    setSelectedMovie(movieToRecommend); // Ensure selected movie is updated

    try {
      const response = await axios.post(`${API_URL}/api/recommend`, {
        movie: movieToRecommend,
        count: numRecommendations
      });
      setRecommendations(response.data.recommendations);
    } catch (err) {
      setError('Failed to get recommendations. Please try again.');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  }, [selectedMovie, numRecommendations]);

  const handleSurpriseMe = () => {
    if (movies.length > 0) {
      const randomIndex = Math.floor(Math.random() * movies.length);
      const randomMovie = movies[randomIndex];
      handleRecommend(randomMovie);
    }
  };

  return (
    <div className="App">
      <Header />
      
      <div className="container">
        <div className="input-section">
          <div className="input-group">
            <label htmlFor="movie-select">Type or select a movie:</label>
            <input
              type="text"
              id="movie-select"
              value={selectedMovie}
              onChange={(e) => setSelectedMovie(e.target.value)}
              className="movie-select"
              list="movie-options"
              placeholder="e.g., The Dark Knight"
            />
            <datalist id="movie-options">
              {movies.map((movie, index) => (
                <option key={index} value={movie} />
              ))}
            </datalist>
          </div>

          <div className="input-group">
            <label htmlFor="num-recommendations">
              Number of Recommendations: {numRecommendations}
            </label>
            <input
              id="num-recommendations"
              type="range"
              min="5"
              max="20"
              step="5"
              value={numRecommendations}
              onChange={(e) => setNumRecommendations(Number(e.target.value))}
              className="slider"
            />
            <div className="slider-labels">
              <span>5</span>
              <span>10</span>
              <span>15</span>
              <span>20</span>
            </div>
          </div>

          <div className="button-group">
            <button 
              onClick={() => handleRecommend()} 
              className="recommend-btn"
              disabled={loading || !selectedMovie}
            >
              Show Recommendations
            </button>
            <button
              onClick={handleSurpriseMe}
              className="surprise-btn"
              disabled={loading}
            >
              🎉 Surprise Me!
            </button>
          </div>

          {error && <div className="error-message">{error}</div>}
        </div>

        {loading && <Spinner />}

        {!loading && recommendations.length > 0 && (
          <div className="recommendations-section">
            <h2>Top {numRecommendations} Recommendations for "{selectedMovie}"</h2>
            <div className="movie-grid">
              {recommendations.map((movie, index) => (
                <MovieCard key={index} movie={movie} />
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
