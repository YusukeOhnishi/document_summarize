from pypdf import PdfReader


def load_pdf(file_path):
    reader = PdfReader(file_path)
    texts = ""
    for page in reader.pages:
        texts += page.extract_text()
    return texts
