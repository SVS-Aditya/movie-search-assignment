# movie_search.py
# This file contains the main logic for searching movies based on semantic similarity.

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Load the pre-trained MiniLM model (small and fast for sentence embeddings)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load movies dataset
def load_movies(csv_path='movies.csv'):
    """Load the movie dataset into a pandas DataFrame."""
    return pd.read_csv(csv_path)

# Create embeddings for all plots in the dataset
def create_embeddings(df):
    """Add a new column 'embedding' with sentence embeddings for each movie plot."""
    df['embedding'] = df['plot'].apply(lambda x: model.encode(x))
    return df

# Main search function
def search_movies(query, top_n=5, df=None):
    """Search for the most semantically similar movies to the query."""
    if df is None:
        df = load_movies()
        df = create_embeddings(df)
    
    # Encode the query using the same model
    query_embedding = model.encode(query)
    
    # Calculate cosine similarity between query and all movie plots
    similarities = cosine_similarity([query_embedding], list(df['embedding']))[0]
    
    # Store similarity scores in DataFrame
    df['similarity'] = similarities
    
    # Return top_n results sorted by similarity score
    return df.sort_values(by='similarity', ascending=False).head(top_n)[['title', 'plot', 'similarity']]
