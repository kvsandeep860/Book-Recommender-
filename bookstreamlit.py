import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os

def recommender(book_name):
    index = np.where(pivot.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_matrix[index])), key=lambda x: x[1], reverse=True)[1:6]
    data = []
    for i in similar_items:
        items = []
        temp_df = books[books["Book-Title"] == pivot.index[i[0]]]
        items.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        items.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        items.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(items)
    return data

# Title of the app
st.title("Book Recommendation System")

# Load data and models using relative paths
base_path = os.path.dirname(__file__)

books = pd.read_csv(os.path.join(base_path, "Books.csv"))
pivot = pickle.load(open(os.path.join(base_path, "piviot_dict"), "rb"))
similarity_matrix = pickle.load(open(os.path.join(base_path, "similarity_matrix"), "rb"))

# Convert pivot to DataFrame if it's not already
pivot = pd.DataFrame(pivot)

# Select box for book name
select_book_name = st.selectbox("Search for a book", list(pivot.index))

# Recommendation logic
if st.button("Recommend"):
    reco = recommender(select_book_name)
    cols = st.columns(5)
    for i in range(len(reco)):
        with cols[i]:
            st.image(reco[i][2])
            st.write(f"Book: **{reco[i][0]}**")
            st.write(f"Author: {reco[i][1]}")

