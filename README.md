# document_summarize
## Launch
The created application can be used by starting it on a Docker container or by installing the library in the local environment.

Clone：

```bash
git clone https://github.com/YusukeOhnishi/document_summarize.git
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

After executing the above command, access ```http:localhost:8501```.

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

<img src="https://i.imgur.com/xeodDhU.png" width=300>

### Set output language
Specify in which language the summary results will be output (Default is English).
Currently, the following languages can be specified.

- English
- Japanese

<img src="https://i.imgur.com/uXAYxzC.png" width=300>

### Select file
Select the document you want to summarize.
You can select documents located locally or on the web.
The supported file formats are as follows.

- pdf

If you select a local file, please upload the file with URL Load Mode turned off.
<img src="https://i.imgur.com/rHLmb2P.png" width=400>

If you want to select a file on the web, please enter the URL in the text box with URL Load Mode turned on.
<img src="https://i.imgur.com/KugsDKQ.png" width=400>

When the file is successfully loaded, the number of tokens for the input file and the cost of the input prompt in the gpt model will be displayed in the sidebar.

<img src="https://i.imgur.com/KSNnL54.png" width=130>

### Click Summary button
Click the summary button.

<img src="https://i.imgur.com/ljPs8tc.png" width=70>

Once the summarization process is complete, the summary results will be output.
Also, the number of tokens used to output the results and the OpenAI API cost are output in the sidebar.

<img src="https://i.imgur.com/LfgGNqA.png" width=130>

<img src="https://i.imgur.com/dHGCfmx.png" width=400>
