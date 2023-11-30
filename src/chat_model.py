import os
from openai import OpenAI, AzureOpenAI
import tiktoken


class ChatModel():
    def __init__(self, model_name):
        # Azure OpenAI Service のエンドポイントと API キーを設定します。
        api_type = os.getenv('API_TYPE')
        api_key = os.getenv('API_KEY')
        endpoint = os.getenv('API_ENDPOINT')
        api_version = os.getenv('API_VERSION')

        if api_type == 'azure':
            self.client = AzureOpenAI(
                azure_endpoint =endpoint,
                api_key=api_key,
                api_version=api_version,
                azure_deployment=model_name
            )
        elif api_type == 'openai':
            self.client = OpenAI(
                api_key=api_key
            )
        else:
            if api_type:
                raise Exception('API_TYPE is not azure or openai.')
            else:
                raise Exception('API_TYPE is not set.')
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
