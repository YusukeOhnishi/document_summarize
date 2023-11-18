FROM python:3.11-slim

WORKDIR /app
COPY ./ /app/
RUN apt-get update && apt-get install -y curl
RUN pip install -r requirements.txt
# Set your OpenAI API Key
ENV OPENAI_API_KEY 'Your OpenAI API Key'

EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]