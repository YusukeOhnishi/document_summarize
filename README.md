# document_summarize
## Launch
The created application can be used by starting it on a Docker container or by installing the library in the local environment.

Clone：

```bash
git clone 
cd ./document_summarize
```

Requires OpenAI API Key for use.
Please obtain the KEY from the official website below.  
[https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

<img src="https://i.imgur.com/MdJpWHt.png" width=600>

### Docker
First, write your OpenAI API Key in the Dockerfile.
Enter the obtained OpenAI API Key in the following part of the Dockerfile and save it.

<img src="https://i.imgur.com/jPU1b3j.png" width=600>

After entering the OpenAI API Key, please build and run from the Dockerfile.

```bash
docker build -t document_summarize .
docker run -p 8501:8501 document_summarize
```

After executing the above command, access ```http:localhost:8501.```

### Local
Execute the following only when running in a virtual environment.

```bash
python venv venv
source ./source venv/bin/activate
```

Setting environment variables and install the necessary libraries.

```bash
export OPENAI_API_KEY='Your OpenAI API Key'
pip install -r requirement.txt
streamlit run main.py
```

After startup, a URL will be displayed on the console, so access this URL.

## Usage
### Overview
Outputs a summary of the selected file using OpenAI's gpt model.
You can choose the language and gpt model for the final output result.
Also, when summarizing a file, OpenAI will output how much it will cost. In addition, when outputting the results, it will output how much it will cost depending on the number of output tokens.

<img src="https://i.imgur.com/P5E6M0M.png" width=600>

### Set model
Select gpt model (Default is gpt-3.5-turbo-16k).
Currently, the following models are available.

- gpt-3.5-turbo-16k
- gpt-3.5-turbo
- gpt-4
- gpt-4-32k
- gpt-4-1106-preview

<img src="https://i.imgur.com/4JnuTRE.png" width=600>

### Set output language
Specify in which language the summary results will be output (Default is English).
Currently, the following languages can be specified.

- English
- Japanese

<img src="https://i.imgur.com/EBr6p78.png" width=600>

### Upload file
Upload the file.
You can upload by dragging and dropping, but you can also specify the file directly from Explorer by clicking. Currently, the supported file formats are as follows.

- pdf

<img src="https://i.imgur.com/IZNuLXq.png" width=600>

When the file is successfully uploaded, the number of tokens for the input file and the cost of the input prompt in the gpt model will be displayed in the sidebar.

<img src="https://i.imgur.com/YZxeAtU.png" width=600>

### Click Summary button
Click the summary button.

<img src="https://i.imgur.com/oEUhx2X.png" width=600>

Once the summarization process is complete, the summary results will be output.
Also, the number of tokens used to output the results and the OpenAI API cost are output in the sidebar.

<img src="https://i.imgur.com/0Vr2EGA.png" width=600>
