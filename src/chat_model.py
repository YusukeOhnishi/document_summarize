from openai import OpenAI
import tiktoken


class chat_model():
    def __init__(self, openai_api_key, model_name):
        self.client = OpenAI(api_key=openai_api_key)
        self.model_name = model_name

    def get_chat_message(self, message):
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "user", "content": message},
            ],
        )
        return response

    def get_message_token_num(self, message):
        encoding = tiktoken.encoding_for_model(self.model_name)
        tokens = encoding.encode(message)
        tokens_count = len(tokens)
        return tokens_count
