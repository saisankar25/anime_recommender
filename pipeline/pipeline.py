from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.CustomException import CustomException
import sys

logger = get_logger(__name__)

class AnimeRecommenderPipeline:
    def __init__(self, persist_dir: str = "Chroma_db"):
        try:
            logger.info("Initializing AnimeRecommenderPipeline")
            vector_builder = VectorStoreBuilder(csv_path="", persist_dir=persist_dir)
            retriever = vector_builder.load_vector_store().as_retriever()
            self.recommender = AnimeRecommender(retriever=retriever, api_key=GROQ_API_KEY, model_name=MODEL_NAME)
            logger.info("AnimeRecommenderPipeline initialized successfully")
        except Exception as e:
            raise CustomException("Pipeline Initialization Failed", e)

    def recommend(self, query: str) -> str:
        try:
            logger.info("Recommendation started")
            return self.recommender.get_recommendation(query)
        except Exception as e:
            raise CustomException("Recommendation Failed", e)
