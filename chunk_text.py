def create_chunks(text, chunk_size=100, overlap=20):

    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end]
        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks
    
if __name__ == "__main__":
    sample_text = "ClauseGuard AI is learning how to split documents into smaller chunks."

    result = create_chunks(sample_text, 20, 5)

    for chunk in result:
        print(chunk)
        print("----------")