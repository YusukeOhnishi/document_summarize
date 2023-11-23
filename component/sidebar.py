import streamlit as st


class Sidebar:
    def show_init(text):
        st.sidebar.write(text)

    def show_price_table(text_token, price, text):
        message_price = text_token * price / 1000
        message_price = '{:.5f}'.format(message_price)
        st.sidebar.write(f'''
        ## {text} message
        |tokens|cost($)|
        |---|---|
        |{text_token}|{message_price}|
        ''')
