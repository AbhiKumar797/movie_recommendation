import React from 'react';
import './MovieCard.css';

function MovieCard({ movie }) {
  return (
    <div className="movie-card">
      <div className="poster-container">
        <img 
          src={movie.poster} 
          alt={movie.title}
          className="movie-poster"
          onError={(e) => {
            e.target.src = 'https://via.placeholder.com/500x750.png?text=No+Poster';
          }}
        />
      </div>
      <div className="movie-info">
        <h3 className="movie-title">{movie.title}</h3>
        <div className="similarity-badge">
          {(movie.similarity_score * 100).toFixed(1)}% Match
        </div>
      </div>
    </div>
  );
}

export default MovieCard;
