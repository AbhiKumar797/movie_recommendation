# 🎬 Movie Recommendation System

A comprehensive movie recommendation system that suggests similar movies based on user selection, built with machine learning algorithms and modern web technologies.

## 📹 Video Showcase

> **Note:** Add your project demonstration video here
> 
> You can upload a video to GitHub or use platforms like YouTube/Loom and embed the link below:
> 
> ```markdown
> [![Watch the Demo](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)
> ```

## ✨ Features

### 🎯 Core Functionality
- **Movie Search & Selection** - Type or select from 5000+ movies
- **Smart Recommendations** - Get personalized movie suggestions using cosine similarity
- **Customizable Results** - Adjust number of recommendations (5, 10, 15, or 20)
- **Movie Posters** - Fetches real-time posters from TMDb API
- **Similarity Scores** - View how similar each recommendation is to your selection

### 🎲 Interactive Features
- **Surprise Me!** - Random movie recommendation feature
- **Auto-complete Search** - Easy movie selection with datalist dropdown
- **Responsive Design** - Works seamlessly on desktop and mobile devices
- **Loading Indicators** - Smooth user experience with loading spinners
- **Error Handling** - Graceful error messages for better UX

### 🔧 Technical Features
- **Dual Interface** - Streamlit app + React frontend
- **RESTful API** - Flask backend with CORS support
- **Case-Insensitive Search** - Flexible movie matching
- **Retry Mechanism** - API calls with automatic retries
- **Fallback Posters** - Placeholder images when posters unavailable

## 🛠️ Tech Stack

### Frontend
- **React.js** - UI framework
- **Axios** - HTTP client
- **CSS3** - Styling and animations

### Backend
- **Flask** - REST API framework
- **Flask-CORS** - Cross-origin resource sharing
- **Pandas** - Data manipulation
- **Pickle** - Model serialization

### Machine Learning
- **Scikit-learn** - Cosine similarity algorithm
- **Content-based filtering** - Recommendation engine

### External APIs
- **TMDb API** - Movie posters and metadata

### Alternative Interface
- **Streamlit** - Quick deployment UI

## 📂 Project Structure

```
Movie_recommendation-main/
├── frontend/                 # React application
│   ├── src/
│   │   ├── components/      # Reusable React components
│   │   │   ├── Header.js    # App header component
│   │   │   ├── MovieCard.js # Movie display card
│   │   │   └── Spinner.js   # Loading spinner
│   │   ├── App.js           # Main React component
│   │   └── index.js         # Entry point
│   ├── public/
│   │   ├── index.html
│   │   └── placeholder.svg  # Fallback poster
│   └── package.json
├── backend/                 # Flask API
│   ├── api.py              # REST API endpoints
│   └── requirements.txt     # Python dependencies
├── model/                   # ML models (gitignored)
│   ├── movie_list.pkl      # Movie dataset
│   └── similarity.pkl      # Similarity matrix
├── data/                    # Raw datasets
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
├── app.py                   # Streamlit application
├── notebook.ipynb           # Data processing & model training
└── .gitignore
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn

### Backend Setup

1. **Clone the repository**
```bash
git clone https://github.com/AbhiKumar797/movie_recommendation.git
cd movie_recommendation
```

2. **Install Python dependencies**
```bash
cd backend
pip install -r requirements.txt
```

3. **Run the Flask API**
```bash
python api.py
```
API will run on `http://localhost:5000`

### Frontend Setup

1. **Install Node dependencies**
```bash
cd frontend
npm install
```

2. **Start the React development server**
```bash
npm start
```
Frontend will run on `http://localhost:3000`

### Streamlit App (Alternative)

```bash
streamlit run app.py
```

## 📊 API Endpoints

### `GET /api/movies`
Get list of all available movies
```json
{
  "movies": ["Avatar", "The Dark Knight", ...]
}
```

### `POST /api/recommend`
Get movie recommendations
```json
{
  "movie": "The Dark Knight",
  "count": 10
}
```

**Response:**
```json
{
  "selected_movie": "The Dark Knight",
  "count": 10,
  "recommendations": [
    {
      "id": 155,
      "title": "The Dark Knight Rises",
      "poster": "https://image.tmdb.org/t/p/w500/...",
      "similarity_score": 0.89
    }
  ]
}
```

### `GET /api/health`
Health check endpoint
```json
{
  "status": "healthy",
  "message": "Movie Recommender API is running"
}
```

## 🎨 Features Showcase

### 1. Movie Selection
- Type-ahead search functionality
- Dropdown with 5000+ movies
- Autocomplete suggestions

### 2. Customizable Recommendations
- Slider to select 5, 10, 15, or 20 recommendations
- Real-time adjustment

### 3. Surprise Me Feature
- Randomly selects a movie
- Instantly shows recommendations
- Great for discovering new content

### 4. Movie Cards
- High-quality posters
- Movie titles
- Similarity scores
- Responsive grid layout

### 5. Loading States
- Animated spinner during API calls
- Disabled buttons during loading
- Smooth transitions

### 6. Error Handling
- Movie not found errors
- API failure messages
- Network error handling
- Fallback poster images

## 🧠 How It Works

1. **Data Processing**: Movie metadata from TMDb dataset is processed
2. **Feature Extraction**: Movie features (genres, keywords, cast, crew) are vectorized
3. **Similarity Calculation**: Cosine similarity matrix is computed
4. **Recommendation**: For a selected movie, top N most similar movies are retrieved
5. **Poster Fetching**: Real-time API calls to TMDb for movie posters

## 🔐 Environment Variables

Create a `.env` file for API keys (optional):
```
TMDB_API_KEY=your_api_key_here
```

## 📝 Future Enhancements

- [ ] User authentication and personalized recommendations
- [ ] Movie ratings and reviews integration
- [ ] Collaborative filtering algorithm
- [ ] Watch later list functionality
- [ ] Movie trailers integration
- [ ] Advanced filters (genre, year, rating)
- [ ] Social sharing features
- [ ] Docker containerization

## 🐛 Known Issues

- Large model files (`.pkl`) not included in repository (use Git LFS)
- Poster fetching may fail without internet connection
- TMDb API rate limits may apply

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Abhi Kumar**
- GitHub: [@AbhiKumar797](https://github.com/AbhiKumar797)

## 🙏 Acknowledgments

- [TMDb API](https://www.themoviedb.org/documentation/api) for movie data
- [Kaggle](https://www.kaggle.com/) for the dataset
- React and Flask communities

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

⭐ If you like this project, please give it a star on GitHub!
