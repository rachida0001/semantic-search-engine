from sklearn.metrics.pairwise import cosine_similarity

class SemanticSearchEngine:
    def __init__(self, movies_df, movie_embeddings, bert_encoder):
        self.movies_df = movies_df
        self.movie_embeddings = movie_embeddings
        self.bert_encoder = bert_encoder

    def calculate_similarity(self, input_embedding, movie_embeddings):
        return cosine_similarity(input_embedding, movie_embeddings)

    def search(self, input_plot, K):
        input_embedding = self.bert_encoder.encode_plots([input_plot])[0]
        similarities = self.calculate_similarity(input_embedding.unsqueeze(0), self.movie_embeddings)

        # Get the indices of the top K most similar movies
        top_indices = similarities.argsort()[0][::-1][:K]

        # Retrieve the movie information for the top K movies
        top_movies = []
        for idx in top_indices:
            # Convert idx to integer before accessing the DataFrame
            idx = int(idx)
            movie_info = {
                "Title": self.movies_df.iloc[idx]["Title"],
                "year": self.movies_df.iloc[idx]["Release Year"],
                "genre": self.movies_df.iloc[idx]["Genre"]
            }
            top_movies.append(movie_info)

        return top_movies