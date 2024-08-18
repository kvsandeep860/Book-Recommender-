import streamlit as st
import pickle
import pandas as pd
import numpy as np
def recommender(book_name):
    index=np.where(piviot.index==book_name)[0][0]
    similar_items=sorted(list(enumerate(similarity_matrix[index])),key=lambda x:x[1],reverse=True)[1:6]
    data=[]
    for i in similar_items:
        items=[]
        temp_df=books[books["Book-Title"]==piviot.index[i[0]]]
        items.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        items.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        items.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(items)
    return data
st.title("Book Recommendation.")
books=pd.read_csv("C:\\Users\\kvsan\\Desktop\\Ml projects\\Book Recomender\\Books.csv\\Books.csv")
piviot=pickle.load(open("C:\\Users\\kvsan\\Desktop\\Ml projects\\Book Recomender\\piviot_dict","rb"))
similarity_matrix=pickle.load(open("C:\\Users\\kvsan\\Desktop\\Ml projects\\Book Recomender\\similarity_matrix","rb"))
piviot= pd.DataFrame(piviot)
select_book_name = st.selectbox("Search for a book",list(piviot.index))
if st.button("Recommend"):
    reco=recommender(select_book_name)
    cols=st.columns(5)
    for i in range(len(reco)):
        with cols[i]:
            st.image(reco[i][2])
            st.write(f"Book:,**{reco[i][0]}**")
            st.write("Author:",reco[i][1])
            
        
