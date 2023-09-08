import streamlit as st 
from main import main
    


# Define the Streamlit app
def app():
    st.title('Semantic Search Engine For movies')
    st.write('This app helps you to find the movie you\'re searching for')

    plot = st.text_input("Your plot of the movies", value="Two special agents, Aziz and Lemi, are tasked by the Sultan of the Ottoman Empire with delivering a diamond as a gift to the American president")
    K = st.number_input("K movies", min_value=2, max_value=20, value=5)
    release_year = st.number_input("The release Year", min_value=1900, max_value=2017, value=2010)
    genre = st.text_input("The movie genre", value='comedy')


    st.title(f'Here is your {K} nearest movies')

    top_movies = main(plot=plot, K=K, release_year=release_year, genre=genre)

    nb = 1
    for i in top_movies:
        st.header(f'Movies number {nb}')
        st.write(f'Title : {i["Title"]}')
        st.write(f'Release Year {i["year"]}')
        st.write(f'Genre : {i["genre"]}')
        nb +=1


app()

