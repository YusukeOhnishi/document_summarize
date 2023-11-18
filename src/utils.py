import re


def clean_text(text):
    text = text.replace('-\n', '')
    text = re.sub(r'\s+', ' ', text)
    return text


def split_text(text, wc_max):
    words = text.split()
    chunks = [' '.join(words[i:i + wc_max])
              for i in range(0, len(words), wc_max)]
    return chunks
