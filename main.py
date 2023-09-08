from preprocessing_data import DataLoader
from bert_encoder import BERTTextEncoder
from semantic_search import SemanticSearchEngine

def main(K: int, plot : str, release_year : int, genre: str =None):

    # Load and preprocess the dataset
    data_loader = DataLoader('data/wiki_movie_plots_deduped.csv')
    movies_df = data_loader.cleanning_data(release_year, genre)

    # BERT-based text encoding
    bert_encoder = BERTTextEncoder()
    embeddings = bert_encoder.encode_plots(movies_df["Plot"])

    # Initialize the semantic search engine
    search_engine = SemanticSearchEngine(movies_df, embeddings, bert_encoder)

    # Perform the semantic search
    top_movies = search_engine.search(plot, K)

    # Print the top suggested movies
    return top_movies
