class ModelInfo:
    def get_model_info(model_name):
        model_list = {
            'gpt-3.5-turbo-16k': {
                'model_name': 'gpt-3.5-turbo-16k',
                'max_token': 16385,
                'input_price': 0.001,
                'output_price': 0.002,
            },
            'gpt-3.5-turbo': {
                'model_name': 'gpt-3.5-turbo',
                'max_token': 4096,
                'input_price': 0.001,
                'output_price': 0.002,
            },
            'gpt-4': {
                'model_name': 'gpt-4',
                'max_token': 8192,
                'input_price': 0.03,
                'output_price': 0.06,
            },
            'gpt-4-32k': {
                'model_name': 'gpt-4-32k',
                'max_token': 32768,
                'input_price': 0.03,
                'output_price': 0.06,
            },
            'gpt-4-1106-preview': {
                'model_name': 'gpt-4-1106-preview',
                'max_token': 128000,
                'input_price': 0.01,
                'output_price': 0.03,
            },
        }
        return model_list[model_name]
