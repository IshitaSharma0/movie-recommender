import streamlit as st
import pickle
import pandas as pd
import requests

import gdown
import os

if not os.path.exists("similarity.pkl"):
    print("Downloading similarity.pkl from Google Drive...")
    url = 'https://drive.google.com/uc?id=1MHyqeQBEuZ2p44FdIH1dRxCMOFTFa14r'  # Your Google Drive file ID
    gdown.download(url, "similarity.pkl", quiet=False)


def fetch_poster(movie_id):
    response= requests.get('http://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data= response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id= movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies_dict= pickle.load(open('movie_dict.pkl','rb'))
movies= pd.DataFrame(movies_dict)

similarity= pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')

selected_movie_name= st.selectbox(
'How would you like to be contacted?',
movies['title'].values)

if st.button('Recommend'):
    names,posters= recommend(selected_movie_name)

    col1, col2, col3, col4,col5= st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])


# Google Drive file ID (Extract from your Google Drive link)
file_id = "1MHyqeQBEuZ2p44FdIH1dRxCMOFTFa14r"
output_path = "similarity.pkl"

# Download the file if it doesn't exist
if not os.path.exists(output_path):
    print("Downloading similarity.pkl from Google Drive...")
    gdown.download(f"https://drive.google.com/uc?id={file_id}", output_path, quiet=False)

# Load the file
with open(output_path, "rb") as f:
    similarity = pickle.load(f)

print("File loaded successfully!")

if __name__ == "__main__":
    import os
    os.system("streamlit run app.py")
