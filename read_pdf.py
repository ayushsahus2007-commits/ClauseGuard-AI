import pymupdf
from chunk_text import create_chunks

pdf = pymupdf.open("sample_contract.pdf")

full_text = ""

for page in pdf:
    text = page.get_text()
    full_text += text

pdf.close()

chunks = create_chunks(full_text, 500, 50)

for index, chunk in enumerate(chunks):
    print(f"\nCHUNK {index + 1}")
    print(chunk)