from pypdf import PdfReader
from io import BytesIO
from urllib import request


class Loader:
    def load_pdf(file_path):
        reader = PdfReader(file_path)
        texts = ""
        for page in reader.pages:
            texts += page.extract_text()
        return texts

    def load_url(document_url):
        bit_data = request.urlopen(document_url).read()
        data = BytesIO(bit_data)
        return Loader.load_pdf(data)
