import streamlit as st
import pickle
import pandas as pd
import requests
st.title("Movie Recommendar")
def fetch(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=2e07f29f3ef59e73dc2b721de9757898&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)) , reverse=True,key= lambda x:x[1])[1:6]
    recommended_movies = []
    posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        posters.append(fetch(movie_id))
    return recommended_movies,posters

movies_dict = pickle.load(open('movie_dict.pkl' ,'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl' ,'rb'))

selected_movie =  st.selectbox(
    "how would you like to be contacted",movies["title"].values
)

if st.button('Recommend'):
    names,poster = recommend(selected_movie)
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])
    

    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])