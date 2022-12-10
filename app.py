import pickle
import pandas as pd
import streamlit as st

blog_dict = pickle.load(open("blogsDict.pkl", "rb"))
blogs = pd.DataFrame(blog_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))


def recommend(blog):
    blog_index = blogs[blogs["title"] == blog].index[0]
    distances = similarity[blog_index]
    blog_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_blogs = []

    for i in blog_list:
        recommended_blogs.append(blogs.iloc[i[0]].title)

    return recommended_blogs


st.title("SOCO Blog Recommender")
selected_blog_name = st.selectbox(
    "Enter Blog that you want to get recommendation on",
    blogs["title"].values)

if st.button("Recommend"):
    recommendations = recommend(selected_blog_name)
    for blogs in recommendations:
        st.write(blogs)

# DONE
