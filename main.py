import streamlit as st
import os

from src.load import load_pdf
from src.create_prompt import (
    create_summary_prompt, create_part_summary_prompt)
from src.chat_model import chat_model
from src.utils import (clean_text, split_text)
from data.model_info import get_model_info
from data.selection import (get_model_list, get_language_list)

api_key = os.getenv('OPENAI_API_KEY')

st.sidebar.write('# Cost')

col1, col2 = st.columns((1, 1))
with col1:
    model = st.selectbox(
        'select model',
        get_model_list())
with col2:
    language = st.selectbox(
        'select output language',
        get_language_list())
pdf_file = st.file_uploader("Upload pdf file", type='pdf')
try:
    model_info = get_model_info(model)
    max_word = int(model_info["max_token"]/3)
    chat_model = chat_model(api_key, model_info["model_name"])

    text = load_pdf(pdf_file)
    text = clean_text(text)
    input_message_token_num = chat_model.get_message_token_num(text)
except:
    st.stop()


text_list = split_text(text, max_word)
input_message_price = input_message_token_num * \
    model_info["input_price"]/1000
input_message_price = '{:.5f}'.format(input_message_price)

st.sidebar.write(f'''
    ## Input message
    |tokens|cost($)|
    |---|---|
    |{input_message_token_num}|{input_message_price}|
    ''')

if st.button('summarize'):
    message = ""

    if len(text_list) <= 1:
        message = text_list[0]
    else:
        for text in text_list:
            result_tmp = chat_model.get_chat_message(
                create_part_summary_prompt(text))
            message += result_tmp.choices[0].message.content
    result = chat_model.get_chat_message(
        create_summary_prompt(message, language))
    result = result.choices[0].message.content

    st.write(result)

    output_message_token_num = chat_model.get_message_token_num(result)
    output_message_price = output_message_token_num * \
        model_info["output_price"]/1000
    output_message_price = '{:.5f}'.format(output_message_price)
    st.sidebar.write(f'''
        ## Output message
        |tokens|cost($)|
        |---|---|
        |{output_message_token_num}|{output_message_price}|
        ''')
