# Movie Recommendation System

A content-based movie recommendation web app built with **Python** and **Streamlit**.
It recommends similar movies based on metadata features such as genres, keywords, cast, and crew.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [Model/Artifact Files](#modelartifact-files)
- [API Configuration](#api-configuration)
- [Current Limitations](#current-limitations)
- [Future Improvements](#future-improvements)

---

## Project Overview

This project builds a **content-based recommendation engine** using movie metadata from the TMDB 5000 dataset.
A Streamlit UI allows users to select a movie and get top similar movie recommendations with posters.

---

## Features

- Select a movie from a dropdown
- Get top 5 similar movie recommendations
- Display recommended movie posters via TMDB API
- Precomputed similarity matrix for fast recommendations
- Simple and clean Streamlit interface

---

## Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **NumPy**
- **Joblib / Pickle**
- **Requests**
- **Scikit-learn (used in notebook workflow for vectorization/similarity)**

---

## Dataset

Dataset files are located in:

- `movie-recommender-system/Dataset/tmdb_5000_movies.csv`
- `movie-recommender-system/Dataset/tmdb_5000_credits.csv`

These are used in the notebook to create processed movie metadata and similarity artifacts.

---

## How It Works

1. Merge and preprocess movie + credits datasets.
2. Extract useful features (genres, keywords, cast, crew, overview).
3. Build a combined text/tag representation.
4. Vectorize tags and compute movie-to-movie similarity.
5. Save artifacts:
   - `movie_dictionary.pkl`
   - `similarity_movies.pkl`
6. Streamlit app loads artifacts and recommends top 5 similar movies.

---

## Project Structure

```text
Movie-Recommendation-System/
├── README.md
├── .gitignore
└── movie-recommender-system/
    ├── app.py
    ├── requirements.txt
    ├── movie-recommendation-engine.ipynb
    ├── movie_dictionary.pkl
    ├── similarity_movies.pkl
    └── Dataset/
        ├── tmdb_5000_movies.csv
        └── tmdb_5000_credits.csv
```

---

## Installation

1. Clone the repository.
2. Go to the project app directory:

```bash
cd movie-recommender-system
```

3. (Optional but recommended) create and activate a virtual environment.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the App

From `movie-recommender-system/`:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal (usually `http://localhost:8501`).

---

## Model/Artifact Files

The app expects these files inside `movie-recommender-system/`:

- `movie_dictionary.pkl`
- `similarity_movies.pkl`

If these files are missing or outdated, regenerate them using the notebook:

- `movie-recommendation-engine.ipynb`

---

## API Configuration

The app fetches posters from TMDB API inside `app.py`.

> Important: The API key is currently hardcoded in the source.
> For production use, move it to an environment variable or Streamlit secrets.
---

## Current Limitations

- Depends on precomputed `.pkl` files
- Poster fetching fails if TMDB API is unavailable
- Recommendations are content-based only (no collaborative filtering)
- API key handling should be improved for security

---

## Future Improvements

- Add hybrid recommendations (content + collaborative filtering)
- Use environment variables/secrets for API keys
- Add filtering by genre/year/language
- Add evaluation metrics and model comparison
- Add automated tests and CI checks

---

If you find this project useful, feel free to star the repository and contribute.
