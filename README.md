# 🎬 Movie Semantic Search Assignment

This repository contains my solution for the **semantic search on movie plots** assignment.  
The project demonstrates how to use **Sentence Transformers** (`all-MiniLM-L6-v2`) to find the most relevant movies for a natural language query such as:

"spy thriller in Paris"


Instead of keyword search, semantic embeddings allow retrieval based on **meaning** of the text.

---

## 📂 Repository Structure
```
movie-search-assignment/
├── movies.csv # Dataset (must contain 'title' and 'plot' columns)
├── movie_search.py # Main Python module with search function
├── movie_search_solution.ipynb # Jupyter notebook with implementation & demo
├── requirements.txt # Dependencies
├── README.md # Documentation
└── tests/
    └──test_movie_search.py # Unit tests
```
---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/movie-search-assignment.git
   cd movie-search-assignment
   ```
2. **Create a virtual environment**
 ```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```


3. **Install dependencies**
```bash
pip install -r requirements.txt
```

Run the notebook

jupyter notebook movie_search_solution.ipynb

4. Testing

Unit tests are provided in tests/test_movie_search.py.
Run them with:
```bash
python -m unittest tests/test_movie_search.py -v
```
<img width="1447" height="331" alt="Screenshot 2025-08-26 232507" src="https://github.com/user-attachments/assets/ae9f7042-e121-47a0-942a-ed6e5b51c2a5" />


✅ Tests cover:

Output format (returns DataFrame)

Correct number of results (top_n)

Presence of similarity scores

Query relevance ranking
