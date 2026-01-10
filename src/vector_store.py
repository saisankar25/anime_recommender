from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma

from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv()

class VectorStoreBuilder:
    def __init__(self, csv_path: str, persist_dir: str = "Chroma_db"):
        self.csv_path = csv_path
        self.persist_dir = persist_dir
        self.embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    def build(self):
        loader = CSVLoader(file_path=self.csv_path, encoding="utf-8", metadata_columns=[])
        data = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=20)
        texts = text_splitter.split_documents(data)

        db = Chroma.from_documents(texts, self.embedding, persist_directory=self.persist_dir)


    def load_vector_store(self):
        db = Chroma(persist_directory=self.persist_dir, embedding_function=self.embedding)
        return db
