import streamlit as st


class Setting:
    def __init__(self):
        self.model = None
        self.language = None
        self.content = None
        self.content_type = None

    def show_setting(self, model_list, language_list):
        col1, col2 = st.columns((1, 1))
        with col1:
            self.model = st.selectbox(
                'select model',
                model_list)
        with col2:
            self.language = st.selectbox(
                'select output language',
                language_list)

    def get_parameter(self):
        return self.model, self.language

    def show_upload_setting(self):
        url_mode = st.toggle('URL Load Mode')
        if url_mode:
            self.content = st.text_input('URL')
            self.content_type = "url"
        else:
            self.content = st.file_uploader("Upload pdf file", type='pdf')
            self.content_type = "pdf"

    def get_content(self):
        return self.content, self.content_type

    def stop():
        st.stop()


class Content:
    def __init__(self):
        self.is_summarize = False

    def show_summarize_button(self):
        self.is_summarize = st.button('summarize')

    def get_summarize_button(self):
        return self.is_summarize

    def show_result(self, text):
        st.write(text)
