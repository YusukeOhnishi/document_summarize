class CreatePrompt:
    def create_summary_prompt(text, language):
        return f"""
you are a scientist Please output a paper summary based on the following constraints and the input text.

%Constraints:
- Text is concise and easy to understand.
- Don't miss out on important keywords.
- Answer in two sections: conclusion and main text.
- The conclusion is about 150 characters.
- The main text is about 500 characters.
- The output format should follow the markdown format below.
- Please output the results in {language}.
%Output format
### conclusion  
(Output the conclusion here)
### main text  
(Output main text here)
##########################################
{text}
"""

    def create_part_summary_prompt(text):
        return f"""
you are a scientist Please output a paper summary based on the following constraints and the input text.

%%Constraints:
- Text is concise and easy to understand.
- Don't miss out on important keywords.
- Make it into one paragraph.
- Summarize within 400 words.
##########################################
{text}
"""
