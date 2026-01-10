import streamlit as st
from pipeline.pipeline import AnimeRecommenderPipeline
from dotenv import load_dotenv
import os

# Set page config
st.set_page_config(page_title="Anime Recommender", layout="centered")

load_dotenv()

st.title("🎬 Anime Recommender")

@st.cache_resource
def init_pipeline():
    return AnimeRecommenderPipeline()

try:
    with st.spinner("Initializing Recommendation Engine..."):
        pipeline = init_pipeline()
    
    st.success("Engine Ready!")

    query = st.text_input(
        label="Enter your anime preferences:",
        placeholder="e.g., light hearted anime with school setting",
        key="anime_query"
    )

    if query:
        with st.spinner("Searching for the perfect anime..."):
            result = pipeline.recommend(query)
        
        st.subheader("Our Recommendation:")
        st.write(result)
        
except Exception as e:
    st.error(f"An error occurred: {e}")
    st.info("Check the logs for more details.")
