# tests/test_movie_search.py
# These are unit tests for the movie search functionality.

import unittest
import pandas as pd
from movie_search import load_movies, create_embeddings, search_movies

class TestMovieSearch(unittest.TestCase):

    def setUp(self):
        # Load small dataset for testing
        self.df = load_movies('movies.csv')
        self.df = create_embeddings(self.df)

    def test_output_format(self):
        # Check if output is a DataFrame with expected columns
        result = search_movies('spy thriller in Paris', top_n=2, df=self.df)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(all(col in result.columns for col in ['title', 'plot', 'similarity']))

    def test_top_n(self):
        # Ensure top_n parameter returns correct number of rows
        result = search_movies('spy thriller in Paris', top_n=3, df=self.df)
        self.assertEqual(len(result), 3)

    def test_similarity_scores(self):
        # Similarity scores should be between 0 and 1
        result = search_movies('spy thriller in Paris', top_n=2, df=self.df)
        for score in result['similarity']:
            self.assertGreaterEqual(score, 0)
            self.assertLessEqual(score, 1)

    def test_relevance(self):
        # The top result should have a higher similarity score than the last one
        result = search_movies('spy thriller in Paris', top_n=3, df=self.df)
        self.assertGreaterEqual(result.iloc[0]['similarity'], result.iloc[-1]['similarity'])

if __name__ == '__main__':
    unittest.main()
