from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import docx

embed_model = HuggingFaceEmbedding(model_name="intfloat/multilingual-e5-large")


def make_emb(text: str) -> list[float]:
    return embed_model.get_text_embedding(text)


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
