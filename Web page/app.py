# Import necessary libraries
import streamlit as st
import pickle
import pandas as pd
import requests

# Function to fetch movie poster from an API
def fetch_poster(movie_id):
    # Make an API request to get movie data
    response = requests.get('https://api.themoviedb.org/3/movie/{}'
                            '?api_key=e2ac6bab0c191a6b8fd26ddd7d0afc40&language=en-US'.format(movie_id))
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Function to recommend movies
def recommend(mov):
    movie_idx = movie[movie['title'] == mov].index[0]
    distance = similarity[movie_idx]
    movie_lst = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_lst:
        movie_id = movie.iloc[i[0]].movie_id
        recommended_movies.append(movie.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters, movie_lst

# Load movie data and similarity scores
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movie = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Create a Streamlit app and set the title
st.title('Movie Recommender System')

# Create a selectbox for users to choose a movie
selected_movie_name = st.selectbox('Enter Movie', movie['title'].values)

# Create a button to trigger movie recommendations
if st.button('Recommend'):
    names, posters, movie_lst = recommend(selected_movie_name)
    
    # Create columns to display recommended movies and their information
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.text(f"Movie ID: {movie.iloc[movie_lst[0][0]].movie_id}")
        st.image(posters[0])
        st.markdown(
            f'''
                <a target="_blank" href="https://autoembed.to/movie/tmdb/{movie.iloc[movie_lst[0][0]].movie_id}">
                    <button>
                        Go to Movie
                    </button>
                </a>
                ''',
            unsafe_allow_html=True
        )
    with col2:
        st.text(names[1])
        st.text(f"Movie ID: {movie.iloc[movie_lst[1][0]].movie_id}")
        st.image(posters[1])
        st.markdown(
            f'''
                <a target="_blank" href="https://autoembed.to/movie/tmdb/{movie.iloc[movie_lst[1][0]].movie_id}">
                    <button>
                        Go to Movie
                    </button>
                </a>
                ''',
            unsafe_allow_html=True
        )
    with col3:
        st.text(names[2])
        st.text(f"Movie ID: {movie.iloc[movie_lst[2][0]].movie_id}")
        st.image(posters[2])
        st.markdown(
            f'''
                <a target="_blank" href="https://autoembed.to/movie/tmdb/{movie.iloc[movie_lst[2][0]].movie_id}">
                    <button>
                        Go to Movie
                    </button>
                </a>
                ''',
            unsafe_allow_html=True
        )
    with col4:
        st.text(names[3])
        st.text(f"Movie ID: {movie.iloc[movie_lst[3][0]].movie_id}")
        st.image(posters[3])
        st.markdown(
            f'''
                <a target="_blank" href="https://autoembed.to/movie/tmdb/{movie.iloc[movie_lst[3][0]].movie_id}">
                    <button>
                        Go to Movie
                    </button>
                </a>
                ''',
            unsafe_allow_html=True
        )
    with col5:
        st.text(names[4])
        st.text(f"Movie ID: {movie.iloc[movie_lst[4][0]].movie_id}")
        st.image(posters[4])
        st.markdown(
            f'''
                <a target="_blank" href="https://autoembed.to/movie/tmdb/{movie.iloc[movie_lst[4][0]].movie_id}">
                    <button>
                        Go to Movie
                    </button>
                </a>
                ''',
            unsafe_allow_html=True
        )
