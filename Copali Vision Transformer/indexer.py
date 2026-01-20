import os
from byaldi import RAGMultiModal

class ColPaliIndexer:
    def __init__(self, model_name="vidore/colpali-v1.2"):
        # Initializing the Vision Transformer-based RAG model
        self.rag = RAGMultiModal.from_pretrained(model_name)
        print(f"Model {model_name} loaded successfully.")

    def build_index(self, data_dir, index_name="document_index"):
        """
        Indexes a directory of PDFs directly from images, bypassing OCR.
        """
        if not os.path.exists(data_dir):
            raise ValueError(f"Directory {data_dir} does not exist.")
            
        print(f"Starting indexing for: {data_dir}")
        self.rag.index(
            input_path=data_dir,
            index_name=index_name,
            store_collection_with_index=True,
            overwrite=True
        )
        print(f"Index '{index_name}' built and saved.")

if __name__ == "__main__":
    indexer = ColPaliIndexer()
    indexer.build_index(data_dir="./data/reports")
