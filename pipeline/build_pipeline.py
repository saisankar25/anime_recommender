from src.data_loader import AnimeDataLoader
import sys
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.CustomException import CustomException

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting pipeline")
        loader = AnimeDataLoader(original_csv="data/anime_with_synopsis.csv",processed_csv="data/processed_anime.csv")
        processed_csv = loader.load_and_process() 
        logger.info("Data loaded and processed successfully")
        vector_builder = VectorStoreBuilder(csv_path=processed_csv,persist_dir="Chroma_db")
        vector_builder.build()
        logger.info("Vector store built successfully")
        logger.info("Pipeline built successfully")
    except Exception as e:
        raise CustomException(e,sys)

if __name__ == "__main__":
    main()
    


