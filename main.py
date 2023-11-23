from src.load import Loader
from src.create_prompt import CreatePrompt
from src.chat_model import ChatModel
from src.utils import (clean_text, split_text)

from data.model_info import ModelInfo
from data.selection import GetList

from component.main_page import (Setting,Content)
from component.sidebar import Sidebar

Sidebar.show_init('# Cost')
setting = Setting()
setting.show_setting(GetList.get_model_list(), GetList.get_language_list())
model, language = setting.get_parameter()

model_info = ModelInfo.get_model_info(model)
max_word = int(model_info["max_token"]/3)
chat_model = ChatModel(model_info["model_name"])

setting.show_upload_setting()
content_source, content_type = setting.get_content()

try:
    match content_type:
        case "pdf":
            text=Loader.load_pdf(content_source)
        case "url":
            text=Loader.load_url(content_source)
        case _:
            raise Exception
    text = clean_text(text)
except:
    Setting.stop()

text_list = split_text(text, max_word)

input_message_token_num = chat_model.get_message_token_num(text)
Sidebar.show_price_table(input_message_token_num,model_info["input_price"],"Input")

content=Content()
content.show_summarize_button()
if content.get_summarize_button():
    message = ""

    if len(text_list) <= 1:
        message = text_list[0]
    else:
        for text in text_list:
            result_tmp = chat_model.get_chat_message(
                CreatePrompt.create_part_summary_prompt(text))
            message += result_tmp.choices[0].message.content
    result = chat_model.get_chat_message(
        CreatePrompt.create_summary_prompt(message, language))
    result = result.choices[0].message.content

    content.show_result(result)

    output_message_token_num = chat_model.get_message_token_num(result)
    Sidebar.show_price_table(output_message_token_num,model_info["output_price"],"Output")
