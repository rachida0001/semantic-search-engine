# Semantic Movie Search Engine using BERT

Welcome to the Semantic Movie Search Engine project! This repository contains an implementation of a semantic search engine for movies using the BERT-based text encoder. The search engine can retrieve the top K movies that are semantically similar to a given plot description. Additionally, it supports filtering by genre and release year

## Introduction

Semantic textual similarity forms the foundation of modern search engines, enabling retrieval of relevant information based on its similarity to the input query representation. This project demonstrates the implementation of a semantic movie search engine using a pretrained BERT model.

## Project Structure

Project Structure

The project is structured into several modules that work together to achieve the semantic search functionality:

    main.py: The main script that coordinates the search process.
    preprocessing_data.py: Contains the DataLoader class for loading and cleaning the dataset.
    bert_encoder.py: Defines the BERTTextEncoder class for encoding plot descriptions into embeddings using a BERT model.
    semantic_search.py: Implements the SemanticSearchEngine class to calculate cosine similarities and perform the search.

## Requirements

Install the required dependencies:
    pip install -r requirements.txt

## Running the Semantic Search

    1 - Run the script: streamlit run ui_app.py
