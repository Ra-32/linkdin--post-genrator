import streamlit as st
from fewshots import FewShotPosts
from process_post import process_post
from post_genrator import genrate_post
from llm_helper import llm
import os
from dotenv import load_dotenv
load_dotenv()


length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

def main():
    st.title("linkdIn Post Generator..✉️ ")
    fs=FewShotPosts()
    unique_tags=fs.get_tags()
    col1,col2,col3=st.columns(3)
    with col1:
        tag=st.selectbox("Select Tag",unique_tags)

    with col2:
        length=st.selectbox("Select Length",length_options)

    with col3:
        language=st.selectbox("Select Language",language_options)

    if st.button("Generate Post"):
        post=genrate_post(length,language,tag)
        st.subheader("Generated Post:")
        st.write(post)

if __name__ == "__main__":
    main()