import streamlit as st 
import pickle
import requests

st.title("Movie Recommendation System")


movies = pickle.load(open(r'C:\Users\ASUS\Desktop\DS\scikit-learn\project 2\movies.pkl','rb'))
movie_list = movies['title'].values

similarity = pickle.load(open(r'C:\Users\ASUS\Desktop\DS\scikit-learn\project 2\similarity.pkl','rb'))

option = st.selectbox(
    "Which movie do you like",
    movie_list,
)

recommend_movies = []
poster_url =[]
def recommend(name):
    movie_index = movies[movies['title'] == name].index[0]
    distaces = similarity[movie_index]
    movie_list = sorted(list(enumerate(distaces)),reverse=True , key=lambda x : x[1])[1:6]
    for i in movie_list:
        recommend_movies.append(movies.iloc[i[0],1])
    for i in recommend_movies:
        url = f'https://www.omdbapi.com/?t={i}&apikey=' # enter your API key
        response = requests.get(url).json()
        if response['Response'] == 'True' :
            poster_url.append(response['Poster'])
        else:
            poster_url.append(1) 
if st.button("Recommend"):
    recommend(option)
    col1, col2 , col3 = st.columns(3)

    with col1:
        if poster_url[0] == 1 :
            st.warning("Unable to load image")
        else:
            st.image(poster_url[0], use_container_width=True , caption= recommend_movies[0])
    with col2:
        if poster_url[1] == 1 :
            st.warning("Unable to load image")
        else:
            st.image(poster_url[1], use_container_width=True , caption= recommend_movies[1])
    with col3:
        if poster_url[2] == 1 :
            st.warning("Unable to load image")
        else:
            st.image(poster_url[2], use_container_width=True , caption= recommend_movies[2])

    col4 , col5 = st.columns(2)
    with col4:
        if poster_url[3] == 1 :
            st.warning("Unable to load image")
        else:
            st.image(poster_url[3], use_container_width=True , caption= recommend_movies[3])

    with col5:
        if poster_url[4] == 1 :
            st.warning("Unable to load image")
        else:
            st.image(poster_url[4], use_container_width=True , caption= recommend_movies[4])


