from byaldi import RAGMultiModal
from PIL import Image

class ColPaliRetriever:
    def __init__(self, index_path=".byaldi/finance_index"):
        # Loading the existing multi-vector index
        self.rag = RAGMultiModal.from_index(index_path)

    def search_and_display(self, query, top_k=3):
        """
        Performs MaxSim late interaction search and returns visual results.
        """
        results = self.rag.search(query, k=top_k)
        
        for i, res in enumerate(results):
            print(f"Result {i+1}: Page {res.page_num} from {res.doc_id} (Score: {res.score:.4f})")
            # In a real app, you would display res.base64_image or open the file
            # img = Image.open(res.image_path)
            # img.show()

if __name__ == "__main__":
    searcher = ColPaliRetriever(index_path=".byaldi/document_index")
    searcher.search_and_display("What is the quarterly revenue growth?")
